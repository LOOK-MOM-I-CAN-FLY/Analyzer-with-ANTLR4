from MyLanguageLexer import myLanguageLexer
from myLanguageParser import myLanguageParser
from myLanguageVisitor import myLanguageVisitor
from antlr4 import InputStream, CommonTokenStream

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
    input_code = "if (1 < 2) if (3 == 4) print(0); else print(9);"
    
    lexer = myLanguageLexer(InputStream(input_code))
    stream = CommonTokenStream(lexer)
    parser = myLanguageParser(stream)
    
    tree = parser.program() 

    visitor = MyTreeVisitor()
    visitor.visit(tree) 

if __name__ == '__main__':
    main()
