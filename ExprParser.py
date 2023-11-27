# Generated from Expr.g4 by ANTLR 4.13.1
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
        4,1,22,78,2,0,7,0,2,1,7,1,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,
        1,62,8,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,5,1,73,8,1,10,1,12,
        1,76,9,1,1,1,0,1,2,2,0,2,0,2,1,0,15,16,1,0,17,18,91,0,4,1,0,0,0,
        2,61,1,0,0,0,4,5,3,2,1,0,5,6,5,0,0,1,6,1,1,0,0,0,7,8,6,1,-1,0,8,
        9,5,1,0,0,9,10,3,2,1,0,10,11,5,2,0,0,11,62,1,0,0,0,12,13,5,3,0,0,
        13,14,3,2,1,0,14,15,5,2,0,0,15,62,1,0,0,0,16,17,5,4,0,0,17,18,3,
        2,1,0,18,19,5,2,0,0,19,62,1,0,0,0,20,21,5,5,0,0,21,22,3,2,1,0,22,
        23,5,2,0,0,23,62,1,0,0,0,24,25,5,6,0,0,25,26,3,2,1,0,26,27,5,2,0,
        0,27,62,1,0,0,0,28,29,5,7,0,0,29,30,3,2,1,0,30,31,5,2,0,0,31,62,
        1,0,0,0,32,33,5,8,0,0,33,34,3,2,1,0,34,35,5,2,0,0,35,62,1,0,0,0,
        36,37,5,9,0,0,37,38,3,2,1,0,38,39,5,2,0,0,39,62,1,0,0,0,40,41,5,
        10,0,0,41,42,3,2,1,0,42,43,5,2,0,0,43,62,1,0,0,0,44,45,5,11,0,0,
        45,46,3,2,1,0,46,47,5,2,0,0,47,62,1,0,0,0,48,49,5,12,0,0,49,50,3,
        2,1,0,50,51,5,2,0,0,51,62,1,0,0,0,52,53,5,13,0,0,53,54,3,2,1,0,54,
        55,5,2,0,0,55,62,1,0,0,0,56,62,5,21,0,0,57,58,5,14,0,0,58,59,3,2,
        1,0,59,60,5,2,0,0,60,62,1,0,0,0,61,7,1,0,0,0,61,12,1,0,0,0,61,16,
        1,0,0,0,61,20,1,0,0,0,61,24,1,0,0,0,61,28,1,0,0,0,61,32,1,0,0,0,
        61,36,1,0,0,0,61,40,1,0,0,0,61,44,1,0,0,0,61,48,1,0,0,0,61,52,1,
        0,0,0,61,56,1,0,0,0,61,57,1,0,0,0,62,74,1,0,0,0,63,64,10,17,0,0,
        64,65,5,19,0,0,65,73,3,2,1,18,66,67,10,16,0,0,67,68,7,0,0,0,68,73,
        3,2,1,17,69,70,10,15,0,0,70,71,7,1,0,0,71,73,3,2,1,16,72,63,1,0,
        0,0,72,66,1,0,0,0,72,69,1,0,0,0,73,76,1,0,0,0,74,72,1,0,0,0,74,75,
        1,0,0,0,75,3,1,0,0,0,76,74,1,0,0,0,3,61,72,74
    ]

class ExprParser ( Parser ):

    grammarFileName = "Expr.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'log('", "')'", "'sin('", "'cos('", "'tan('", 
                     "'asin('", "'acos('", "'atan('", "'fac('", "'sqrt('", 
                     "'cmtoin('", "'mtoft('", "'kgtolb('", "'('", "'+'", 
                     "'-'", "'*'", "'/'", "'^'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "OP_ADD", "OP_SUB", 
                      "OP_MUL", "OP_DIV", "OP_POW", "NEWLINE", "INT", "WS" ]

    RULE_prog = 0
    RULE_expr = 1

    ruleNames =  [ "prog", "expr" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    OP_ADD=15
    OP_SUB=16
    OP_MUL=17
    OP_DIV=18
    OP_POW=19
    NEWLINE=20
    INT=21
    WS=22

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(ExprParser.ExprContext,0)


        def EOF(self):
            return self.getToken(ExprParser.EOF, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProg" ):
                return visitor.visitProg(self)
            else:
                return visitor.visitChildren(self)




    def prog(self):

        localctx = ExprParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 4
            self.expr(0)
            self.state = 5
            self.match(ExprParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ExprParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class AcosExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(ExprParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAcosExpr" ):
                listener.enterAcosExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAcosExpr" ):
                listener.exitAcosExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAcosExpr" ):
                return visitor.visitAcosExpr(self)
            else:
                return visitor.visitChildren(self)


    class SinExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(ExprParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSinExpr" ):
                listener.enterSinExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSinExpr" ):
                listener.exitSinExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSinExpr" ):
                return visitor.visitSinExpr(self)
            else:
                return visitor.visitChildren(self)


    class SqrtExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(ExprParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSqrtExpr" ):
                listener.enterSqrtExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSqrtExpr" ):
                listener.exitSqrtExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSqrtExpr" ):
                return visitor.visitSqrtExpr(self)
            else:
                return visitor.visitChildren(self)


    class NumberExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INT(self):
            return self.getToken(ExprParser.INT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumberExpr" ):
                listener.enterNumberExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumberExpr" ):
                listener.exitNumberExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumberExpr" ):
                return visitor.visitNumberExpr(self)
            else:
                return visitor.visitChildren(self)


    class FacExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(ExprParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFacExpr" ):
                listener.enterFacExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFacExpr" ):
                listener.exitFacExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFacExpr" ):
                return visitor.visitFacExpr(self)
            else:
                return visitor.visitChildren(self)


    class KgtolbExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(ExprParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterKgtolbExpr" ):
                listener.enterKgtolbExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitKgtolbExpr" ):
                listener.exitKgtolbExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitKgtolbExpr" ):
                return visitor.visitKgtolbExpr(self)
            else:
                return visitor.visitChildren(self)


    class ParensExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(ExprParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParensExpr" ):
                listener.enterParensExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParensExpr" ):
                listener.exitParensExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParensExpr" ):
                return visitor.visitParensExpr(self)
            else:
                return visitor.visitChildren(self)


    class LogExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(ExprParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogExpr" ):
                listener.enterLogExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogExpr" ):
                listener.exitLogExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogExpr" ):
                return visitor.visitLogExpr(self)
            else:
                return visitor.visitChildren(self)


    class AtanExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(ExprParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtanExpr" ):
                listener.enterAtanExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtanExpr" ):
                listener.exitAtanExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtanExpr" ):
                return visitor.visitAtanExpr(self)
            else:
                return visitor.visitChildren(self)


    class InfixExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExprContext
            super().__init__(parser)
            self.left = None # ExprContext
            self.op = None # Token
            self.right = None # ExprContext
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(ExprParser.ExprContext,i)

        def OP_POW(self):
            return self.getToken(ExprParser.OP_POW, 0)
        def OP_ADD(self):
            return self.getToken(ExprParser.OP_ADD, 0)
        def OP_SUB(self):
            return self.getToken(ExprParser.OP_SUB, 0)
        def OP_MUL(self):
            return self.getToken(ExprParser.OP_MUL, 0)
        def OP_DIV(self):
            return self.getToken(ExprParser.OP_DIV, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInfixExpr" ):
                listener.enterInfixExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInfixExpr" ):
                listener.exitInfixExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInfixExpr" ):
                return visitor.visitInfixExpr(self)
            else:
                return visitor.visitChildren(self)


    class CosExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(ExprParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCosExpr" ):
                listener.enterCosExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCosExpr" ):
                listener.exitCosExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCosExpr" ):
                return visitor.visitCosExpr(self)
            else:
                return visitor.visitChildren(self)


    class AsinExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(ExprParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAsinExpr" ):
                listener.enterAsinExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAsinExpr" ):
                listener.exitAsinExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAsinExpr" ):
                return visitor.visitAsinExpr(self)
            else:
                return visitor.visitChildren(self)


    class MtoftExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(ExprParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMtoftExpr" ):
                listener.enterMtoftExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMtoftExpr" ):
                listener.exitMtoftExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMtoftExpr" ):
                return visitor.visitMtoftExpr(self)
            else:
                return visitor.visitChildren(self)


    class CmtoinExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(ExprParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCmtoinExpr" ):
                listener.enterCmtoinExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCmtoinExpr" ):
                listener.exitCmtoinExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCmtoinExpr" ):
                return visitor.visitCmtoinExpr(self)
            else:
                return visitor.visitChildren(self)


    class TanExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(ExprParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTanExpr" ):
                listener.enterTanExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTanExpr" ):
                listener.exitTanExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTanExpr" ):
                return visitor.visitTanExpr(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ExprParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 2
        self.enterRecursionRule(localctx, 2, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 61
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                localctx = ExprParser.LogExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 8
                self.match(ExprParser.T__0)
                self.state = 9
                self.expr(0)
                self.state = 10
                self.match(ExprParser.T__1)
                pass
            elif token in [3]:
                localctx = ExprParser.SinExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 12
                self.match(ExprParser.T__2)
                self.state = 13
                self.expr(0)
                self.state = 14
                self.match(ExprParser.T__1)
                pass
            elif token in [4]:
                localctx = ExprParser.CosExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 16
                self.match(ExprParser.T__3)
                self.state = 17
                self.expr(0)
                self.state = 18
                self.match(ExprParser.T__1)
                pass
            elif token in [5]:
                localctx = ExprParser.TanExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 20
                self.match(ExprParser.T__4)
                self.state = 21
                self.expr(0)
                self.state = 22
                self.match(ExprParser.T__1)
                pass
            elif token in [6]:
                localctx = ExprParser.AsinExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 24
                self.match(ExprParser.T__5)
                self.state = 25
                self.expr(0)
                self.state = 26
                self.match(ExprParser.T__1)
                pass
            elif token in [7]:
                localctx = ExprParser.AcosExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 28
                self.match(ExprParser.T__6)
                self.state = 29
                self.expr(0)
                self.state = 30
                self.match(ExprParser.T__1)
                pass
            elif token in [8]:
                localctx = ExprParser.AtanExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 32
                self.match(ExprParser.T__7)
                self.state = 33
                self.expr(0)
                self.state = 34
                self.match(ExprParser.T__1)
                pass
            elif token in [9]:
                localctx = ExprParser.FacExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 36
                self.match(ExprParser.T__8)
                self.state = 37
                self.expr(0)
                self.state = 38
                self.match(ExprParser.T__1)
                pass
            elif token in [10]:
                localctx = ExprParser.SqrtExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 40
                self.match(ExprParser.T__9)
                self.state = 41
                self.expr(0)
                self.state = 42
                self.match(ExprParser.T__1)
                pass
            elif token in [11]:
                localctx = ExprParser.CmtoinExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 44
                self.match(ExprParser.T__10)
                self.state = 45
                self.expr(0)
                self.state = 46
                self.match(ExprParser.T__1)
                pass
            elif token in [12]:
                localctx = ExprParser.MtoftExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 48
                self.match(ExprParser.T__11)
                self.state = 49
                self.expr(0)
                self.state = 50
                self.match(ExprParser.T__1)
                pass
            elif token in [13]:
                localctx = ExprParser.KgtolbExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 52
                self.match(ExprParser.T__12)
                self.state = 53
                self.expr(0)
                self.state = 54
                self.match(ExprParser.T__1)
                pass
            elif token in [21]:
                localctx = ExprParser.NumberExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 56
                self.match(ExprParser.INT)
                pass
            elif token in [14]:
                localctx = ExprParser.ParensExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 57
                self.match(ExprParser.T__13)
                self.state = 58
                self.expr(0)
                self.state = 59
                self.match(ExprParser.T__1)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 74
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 72
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
                    if la_ == 1:
                        localctx = ExprParser.InfixExprContext(self, ExprParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 63
                        if not self.precpred(self._ctx, 17):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 17)")
                        self.state = 64
                        localctx.op = self.match(ExprParser.OP_POW)
                        self.state = 65
                        localctx.right = self.expr(18)
                        pass

                    elif la_ == 2:
                        localctx = ExprParser.InfixExprContext(self, ExprParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 66
                        if not self.precpred(self._ctx, 16):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 16)")
                        self.state = 67
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==15 or _la==16):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 68
                        localctx.right = self.expr(17)
                        pass

                    elif la_ == 3:
                        localctx = ExprParser.InfixExprContext(self, ExprParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 69
                        if not self.precpred(self._ctx, 15):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 15)")
                        self.state = 70
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==17 or _la==18):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 71
                        localctx.right = self.expr(16)
                        pass

             
                self.state = 76
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[1] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 17)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 16)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 15)
         




