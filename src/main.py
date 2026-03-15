from MyLanguageLexer import myLanguageLexer
from myLanguageParser import myLanguageParser
from myLanguageVisitor import myLanguageVisitor
from antlr4 import InputStream, CommonTokenStream
from antlr4.error.ErrorListener import ErrorListener
import sys

class ThrowingErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        raise SyntaxError(f"line {line}:{column} {msg}")

def strip_comments(code: str) -> str:
    cleaned_lines = []
    for line in code.splitlines():
        if "#" in line:
            line = line.split("#", 1)[0]
        cleaned_lines.append(line)
    return "\n".join(cleaned_lines)

class MyTreeVisitor(myLanguageVisitor):
    
    def visitPrintStat(self, ctx: myLanguageParser.PrintStatContext):
        val = self.visit(ctx.expression())
        print(f"OUTPUT: {val}")
        return None


    def visitIfStat(self, ctx: myLanguageParser.IfStatContext):
        condition_result = self.visit(ctx.condition())
        if condition_result:
            self.visit(ctx.statement())
        return None


    def visitIfElseStat(self, ctx: myLanguageParser.IfElseStatContext):
        condition_result = self.visit(ctx.condition())
        if condition_result:
            self.visit(ctx.statement(0)) 
        else:
            self.visit(ctx.statement(1)) 
        return None

    def visitLessCond(self, ctx: myLanguageParser.LessCondContext):
        left = self.visit(ctx.left)
        right = self.visit(ctx.right)
        return left < right

    def visitEqualCond(self, ctx: myLanguageParser.EqualCondContext):
        left = self.visit(ctx.left)
        right = self.visit(ctx.right)
        return left == right

    def visitIntExpr(self, ctx: myLanguageParser.IntExprContext):
        return int(ctx.INT().getText())

def main():
    if len(sys.argv) != 2:
        print("Usage: python -m src.main <source_file>", file=sys.stderr)
        sys.exit(1)

    source_path = sys.argv[1]

    try:
        with open(source_path, "r", encoding="utf-8") as f:
            input_code = f.read()
    except OSError as e:
        print(f"ERROR: cannot read file '{source_path}': {e}", file=sys.stderr)
        sys.exit(1)

    try:
        input_code = strip_comments(input_code)
        lexer = myLanguageLexer(InputStream(input_code))
        lexer.removeErrorListeners()
        lexer.addErrorListener(ThrowingErrorListener())
        stream = CommonTokenStream(lexer)
        parser = myLanguageParser(stream)
        parser.removeErrorListeners()
        parser.addErrorListener(ThrowingErrorListener())

        tree = parser.program()

        visitor = MyTreeVisitor()
        visitor.visit(tree)
    except Exception as e:
        print(f"ERROR: {e}", file=sys.stderr)
        sys.exit(1)

    sys.exit(0)

if __name__ == '__main__':
    main()
