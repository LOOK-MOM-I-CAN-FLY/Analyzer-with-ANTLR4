from MyLanguageLexer import MyLanguageLexer
from MyLanguageParser import MyLanguageParser
from MyLanguageVisitor import MyLanguageVisitor
from antlr4 import *

class MyTreeVisitor(MyLanguageVisitor):
    
    # Обработка: print( <выражение> );
    def visitPrintStat(self, ctx: MyLanguageParser.PrintStatContext):
        val = self.visit(ctx.expression())
        print(f"OUTPUT: {val}")
        return None

    # Обработка: if ( <условие> ) <оператор>
    def visitIfStat(self, ctx: MyLanguageParser.IfStatContext):
        condition_result = self.visit(ctx.condition())
        if condition_result:
            self.visit(ctx.statement())
        return None

    # Обработка: if ( <условие> ) <оператор> else <оператор>
    def visitIfElseStat(self, ctx: MyLanguageParser.IfElseStatContext):
        condition_result = self.visit(ctx.condition())
        if condition_result:
            self.visit(ctx.statement(0)) # Ветка if
        else:
            self.visit(ctx.statement(1)) # Ветка else
        return None

    # Обработка: <выражение> < <выражение>
    def visitLessCond(self, ctx: MyLanguageParser.LessCondContext):
        left = self.visit(ctx.left)
        right = self.visit(ctx.right)
        return left < right

    # Обработка: <выражение> == <выражение>
    def visitEqualCond(self, ctx: MyLanguageParser.EqualCondContext):
        left = self.visit(ctx.left)
        right = self.visit(ctx.right)
        return left == right

    # Обработка: I
    def visitIntExpr(self, ctx: MyLanguageParser.IntExprContext):
        return int(ctx.INT().getText())

# Запуск анализатора
def main():
    input_code = "if (1 < 2) if (3 == 4) print(0); else print(9);"
    
    lexer = MyLanguageLexer(InputStream(input_code))
    stream = CommonTokenStream(lexer)
    parser = MyLanguageParser(stream)
    
    tree = parser.program() # Строим дерево
    
    visitor = MyTreeVisitor()
    visitor.visit(tree) # Обходим дерево и выполняем семантику

if __name__ == '__main__':
    main()