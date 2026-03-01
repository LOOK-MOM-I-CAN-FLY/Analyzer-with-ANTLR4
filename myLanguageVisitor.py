# Generated from myLanguage.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .myLanguageParser import myLanguageParser
else:
    from myLanguageParser import myLanguageParser

# This class defines a complete generic visitor for a parse tree produced by myLanguageParser.

class myLanguageVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by myLanguageParser#program.
    def visitProgram(self, ctx:myLanguageParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by myLanguageParser#IfStat.
    def visitIfStat(self, ctx:myLanguageParser.IfStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by myLanguageParser#IfElseStat.
    def visitIfElseStat(self, ctx:myLanguageParser.IfElseStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by myLanguageParser#PrintStat.
    def visitPrintStat(self, ctx:myLanguageParser.PrintStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by myLanguageParser#LessCond.
    def visitLessCond(self, ctx:myLanguageParser.LessCondContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by myLanguageParser#EqualCond.
    def visitEqualCond(self, ctx:myLanguageParser.EqualCondContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by myLanguageParser#IntExpr.
    def visitIntExpr(self, ctx:myLanguageParser.IntExprContext):
        return self.visitChildren(ctx)



del myLanguageParser