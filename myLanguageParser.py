# Generated from myLanguage.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,10,46,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,1,0,1,0,1,0,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,3,1,32,8,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,42,8,2,1,3,
        1,3,1,3,0,0,4,0,2,4,6,0,0,44,0,8,1,0,0,0,2,31,1,0,0,0,4,41,1,0,0,
        0,6,43,1,0,0,0,8,9,3,2,1,0,9,10,5,0,0,1,10,1,1,0,0,0,11,12,5,6,0,
        0,12,13,5,1,0,0,13,14,3,4,2,0,14,15,5,2,0,0,15,16,3,2,1,0,16,32,
        1,0,0,0,17,18,5,6,0,0,18,19,5,1,0,0,19,20,3,4,2,0,20,21,5,2,0,0,
        21,22,3,2,1,0,22,23,5,7,0,0,23,24,3,2,1,0,24,32,1,0,0,0,25,26,5,
        8,0,0,26,27,5,1,0,0,27,28,3,6,3,0,28,29,5,2,0,0,29,30,5,3,0,0,30,
        32,1,0,0,0,31,11,1,0,0,0,31,17,1,0,0,0,31,25,1,0,0,0,32,3,1,0,0,
        0,33,34,3,6,3,0,34,35,5,4,0,0,35,36,3,6,3,0,36,42,1,0,0,0,37,38,
        3,6,3,0,38,39,5,5,0,0,39,40,3,6,3,0,40,42,1,0,0,0,41,33,1,0,0,0,
        41,37,1,0,0,0,42,5,1,0,0,0,43,44,5,9,0,0,44,7,1,0,0,0,2,31,41
    ]

class myLanguageParser ( Parser ):

    grammarFileName = "myLanguage.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "';'", "'<'", "'=='", "'if'", 
                     "'else'", "'print'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "IF", "ELSE", "PRINT", "INT", 
                      "WS" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_condition = 2
    RULE_expression = 3

    ruleNames =  [ "program", "statement", "condition", "expression" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    IF=6
    ELSE=7
    PRINT=8
    INT=9
    WS=10

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self):
            return self.getTypedRuleContext(myLanguageParser.StatementContext,0)


        def EOF(self):
            return self.getToken(myLanguageParser.EOF, 0)

        def getRuleIndex(self):
            return myLanguageParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = myLanguageParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 8
            self.statement()
            self.state = 9
            self.match(myLanguageParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return myLanguageParser.RULE_statement

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class IfElseStatContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a myLanguageParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def IF(self):
            return self.getToken(myLanguageParser.IF, 0)
        def condition(self):
            return self.getTypedRuleContext(myLanguageParser.ConditionContext,0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(myLanguageParser.StatementContext)
            else:
                return self.getTypedRuleContext(myLanguageParser.StatementContext,i)

        def ELSE(self):
            return self.getToken(myLanguageParser.ELSE, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfElseStat" ):
                return visitor.visitIfElseStat(self)
            else:
                return visitor.visitChildren(self)


    class IfStatContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a myLanguageParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def IF(self):
            return self.getToken(myLanguageParser.IF, 0)
        def condition(self):
            return self.getTypedRuleContext(myLanguageParser.ConditionContext,0)

        def statement(self):
            return self.getTypedRuleContext(myLanguageParser.StatementContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfStat" ):
                return visitor.visitIfStat(self)
            else:
                return visitor.visitChildren(self)


    class PrintStatContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a myLanguageParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def PRINT(self):
            return self.getToken(myLanguageParser.PRINT, 0)
        def expression(self):
            return self.getTypedRuleContext(myLanguageParser.ExpressionContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrintStat" ):
                return visitor.visitPrintStat(self)
            else:
                return visitor.visitChildren(self)



    def statement(self):

        localctx = myLanguageParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 31
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                localctx = myLanguageParser.IfStatContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 11
                self.match(myLanguageParser.IF)
                self.state = 12
                self.match(myLanguageParser.T__0)
                self.state = 13
                self.condition()
                self.state = 14
                self.match(myLanguageParser.T__1)
                self.state = 15
                self.statement()
                pass

            elif la_ == 2:
                localctx = myLanguageParser.IfElseStatContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 17
                self.match(myLanguageParser.IF)
                self.state = 18
                self.match(myLanguageParser.T__0)
                self.state = 19
                self.condition()
                self.state = 20
                self.match(myLanguageParser.T__1)
                self.state = 21
                self.statement()
                self.state = 22
                self.match(myLanguageParser.ELSE)
                self.state = 23
                self.statement()
                pass

            elif la_ == 3:
                localctx = myLanguageParser.PrintStatContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 25
                self.match(myLanguageParser.PRINT)
                self.state = 26
                self.match(myLanguageParser.T__0)
                self.state = 27
                self.expression()
                self.state = 28
                self.match(myLanguageParser.T__1)
                self.state = 29
                self.match(myLanguageParser.T__2)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return myLanguageParser.RULE_condition

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class EqualCondContext(ConditionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a myLanguageParser.ConditionContext
            super().__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(myLanguageParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(myLanguageParser.ExpressionContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEqualCond" ):
                return visitor.visitEqualCond(self)
            else:
                return visitor.visitChildren(self)


    class LessCondContext(ConditionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a myLanguageParser.ConditionContext
            super().__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(myLanguageParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(myLanguageParser.ExpressionContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLessCond" ):
                return visitor.visitLessCond(self)
            else:
                return visitor.visitChildren(self)



    def condition(self):

        localctx = myLanguageParser.ConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_condition)
        try:
            self.state = 41
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                localctx = myLanguageParser.LessCondContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 33
                localctx.left = self.expression()
                self.state = 34
                self.match(myLanguageParser.T__3)
                self.state = 35
                localctx.right = self.expression()
                pass

            elif la_ == 2:
                localctx = myLanguageParser.EqualCondContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 37
                localctx.left = self.expression()
                self.state = 38
                self.match(myLanguageParser.T__4)
                self.state = 39
                localctx.right = self.expression()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return myLanguageParser.RULE_expression

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class IntExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a myLanguageParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INT(self):
            return self.getToken(myLanguageParser.INT, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIntExpr" ):
                return visitor.visitIntExpr(self)
            else:
                return visitor.visitChildren(self)



    def expression(self):

        localctx = myLanguageParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_expression)
        try:
            localctx = myLanguageParser.IntExprContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 43
            self.match(myLanguageParser.INT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





