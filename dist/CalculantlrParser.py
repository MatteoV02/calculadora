# Generated from Calculantlr.g4 by ANTLR 4.13.1
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
        4,1,21,46,2,0,7,0,2,1,7,1,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,3,0,13,
        8,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,
        1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,5,0,39,8,0,10,0,12,0,42,9,0,
        1,1,1,1,1,1,0,1,0,2,0,2,0,5,1,0,4,5,1,0,6,7,1,0,8,11,1,0,12,13,1,
        0,18,20,53,0,12,1,0,0,0,2,43,1,0,0,0,4,5,6,0,-1,0,5,6,5,1,0,0,6,
        7,3,0,0,0,7,8,5,2,0,0,8,13,1,0,0,0,9,10,5,3,0,0,10,13,3,0,0,10,11,
        13,3,2,1,0,12,4,1,0,0,0,12,9,1,0,0,0,12,11,1,0,0,0,13,40,1,0,0,0,
        14,15,10,8,0,0,15,16,7,0,0,0,16,39,3,0,0,9,17,18,10,7,0,0,18,19,
        7,1,0,0,19,39,3,0,0,8,20,21,10,6,0,0,21,22,7,2,0,0,22,39,3,0,0,7,
        23,24,10,5,0,0,24,25,7,3,0,0,25,39,3,0,0,6,26,27,10,4,0,0,27,28,
        5,14,0,0,28,39,3,0,0,5,29,30,10,3,0,0,30,31,5,15,0,0,31,39,3,0,0,
        4,32,33,10,2,0,0,33,34,5,16,0,0,34,39,3,0,0,3,35,36,10,1,0,0,36,
        37,5,17,0,0,37,39,3,0,0,2,38,14,1,0,0,0,38,17,1,0,0,0,38,20,1,0,
        0,0,38,23,1,0,0,0,38,26,1,0,0,0,38,29,1,0,0,0,38,32,1,0,0,0,38,35,
        1,0,0,0,39,42,1,0,0,0,40,38,1,0,0,0,40,41,1,0,0,0,41,1,1,0,0,0,42,
        40,1,0,0,0,43,44,7,4,0,0,44,3,1,0,0,0,3,12,38,40
    ]

class CalculantlrParser ( Parser ):

    grammarFileName = "Calculantlr.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "'!'", "'*'", "'/'", "'+'", 
                     "'-'", "'>'", "'>='", "'<'", "'<='", "'=='", "'!='", 
                     "'&&'", "'||'", "'~'", "'?'", "'true'", "'false'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "INT", "WS" ]

    RULE_expr = 0
    RULE_atom = 1

    ruleNames =  [ "expr", "atom" ]

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
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    INT=20
    WS=21

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CalculantlrParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class AndExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalculantlrParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CalculantlrParser.ExprContext)
            else:
                return self.getTypedRuleContext(CalculantlrParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAndExpr" ):
                listener.enterAndExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAndExpr" ):
                listener.exitAndExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAndExpr" ):
                return visitor.visitAndExpr(self)
            else:
                return visitor.visitChildren(self)


    class NandExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalculantlrParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CalculantlrParser.ExprContext)
            else:
                return self.getTypedRuleContext(CalculantlrParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNandExpr" ):
                listener.enterNandExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNandExpr" ):
                listener.exitNandExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNandExpr" ):
                return visitor.visitNandExpr(self)
            else:
                return visitor.visitChildren(self)


    class MulDivExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalculantlrParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CalculantlrParser.ExprContext)
            else:
                return self.getTypedRuleContext(CalculantlrParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMulDivExpr" ):
                listener.enterMulDivExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMulDivExpr" ):
                listener.exitMulDivExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMulDivExpr" ):
                return visitor.visitMulDivExpr(self)
            else:
                return visitor.visitChildren(self)


    class EqualityExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalculantlrParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CalculantlrParser.ExprContext)
            else:
                return self.getTypedRuleContext(CalculantlrParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEqualityExpr" ):
                listener.enterEqualityExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEqualityExpr" ):
                listener.exitEqualityExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEqualityExpr" ):
                return visitor.visitEqualityExpr(self)
            else:
                return visitor.visitChildren(self)


    class ComparisonExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalculantlrParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CalculantlrParser.ExprContext)
            else:
                return self.getTypedRuleContext(CalculantlrParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComparisonExpr" ):
                listener.enterComparisonExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComparisonExpr" ):
                listener.exitComparisonExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComparisonExpr" ):
                return visitor.visitComparisonExpr(self)
            else:
                return visitor.visitChildren(self)


    class XorExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalculantlrParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CalculantlrParser.ExprContext)
            else:
                return self.getTypedRuleContext(CalculantlrParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterXorExpr" ):
                listener.enterXorExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitXorExpr" ):
                listener.exitXorExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitXorExpr" ):
                return visitor.visitXorExpr(self)
            else:
                return visitor.visitChildren(self)


    class NotExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalculantlrParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(CalculantlrParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNotExpr" ):
                listener.enterNotExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNotExpr" ):
                listener.exitNotExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNotExpr" ):
                return visitor.visitNotExpr(self)
            else:
                return visitor.visitChildren(self)


    class ParenExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalculantlrParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(CalculantlrParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParenExpr" ):
                listener.enterParenExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParenExpr" ):
                listener.exitParenExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParenExpr" ):
                return visitor.visitParenExpr(self)
            else:
                return visitor.visitChildren(self)


    class AtomExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalculantlrParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def atom(self):
            return self.getTypedRuleContext(CalculantlrParser.AtomContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtomExpr" ):
                listener.enterAtomExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtomExpr" ):
                listener.exitAtomExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtomExpr" ):
                return visitor.visitAtomExpr(self)
            else:
                return visitor.visitChildren(self)


    class AddSubExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalculantlrParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CalculantlrParser.ExprContext)
            else:
                return self.getTypedRuleContext(CalculantlrParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAddSubExpr" ):
                listener.enterAddSubExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAddSubExpr" ):
                listener.exitAddSubExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAddSubExpr" ):
                return visitor.visitAddSubExpr(self)
            else:
                return visitor.visitChildren(self)


    class OrExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalculantlrParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CalculantlrParser.ExprContext)
            else:
                return self.getTypedRuleContext(CalculantlrParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOrExpr" ):
                listener.enterOrExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOrExpr" ):
                listener.exitOrExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOrExpr" ):
                return visitor.visitOrExpr(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CalculantlrParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 0
        self.enterRecursionRule(localctx, 0, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 12
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                localctx = CalculantlrParser.ParenExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 5
                self.match(CalculantlrParser.T__0)
                self.state = 6
                self.expr(0)
                self.state = 7
                self.match(CalculantlrParser.T__1)
                pass
            elif token in [3]:
                localctx = CalculantlrParser.NotExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 9
                self.match(CalculantlrParser.T__2)
                self.state = 10
                self.expr(10)
                pass
            elif token in [18, 19, 20]:
                localctx = CalculantlrParser.AtomExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 11
                self.atom()
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 40
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 38
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
                    if la_ == 1:
                        localctx = CalculantlrParser.MulDivExprContext(self, CalculantlrParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 14
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 15
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==4 or _la==5):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 16
                        self.expr(9)
                        pass

                    elif la_ == 2:
                        localctx = CalculantlrParser.AddSubExprContext(self, CalculantlrParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 17
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 18
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==6 or _la==7):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 19
                        self.expr(8)
                        pass

                    elif la_ == 3:
                        localctx = CalculantlrParser.ComparisonExprContext(self, CalculantlrParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 20
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 21
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 3840) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 22
                        self.expr(7)
                        pass

                    elif la_ == 4:
                        localctx = CalculantlrParser.EqualityExprContext(self, CalculantlrParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 23
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 24
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==12 or _la==13):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 25
                        self.expr(6)
                        pass

                    elif la_ == 5:
                        localctx = CalculantlrParser.AndExprContext(self, CalculantlrParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 26
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 27
                        self.match(CalculantlrParser.T__13)
                        self.state = 28
                        self.expr(5)
                        pass

                    elif la_ == 6:
                        localctx = CalculantlrParser.OrExprContext(self, CalculantlrParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 29
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 30
                        self.match(CalculantlrParser.T__14)
                        self.state = 31
                        self.expr(4)
                        pass

                    elif la_ == 7:
                        localctx = CalculantlrParser.NandExprContext(self, CalculantlrParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 32
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 33
                        self.match(CalculantlrParser.T__15)
                        self.state = 34
                        self.expr(3)
                        pass

                    elif la_ == 8:
                        localctx = CalculantlrParser.XorExprContext(self, CalculantlrParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 35
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 36
                        self.match(CalculantlrParser.T__16)
                        self.state = 37
                        self.expr(2)
                        pass

             
                self.state = 42
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class AtomContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(CalculantlrParser.INT, 0)

        def getRuleIndex(self):
            return CalculantlrParser.RULE_atom

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtom" ):
                listener.enterAtom(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtom" ):
                listener.exitAtom(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtom" ):
                return visitor.visitAtom(self)
            else:
                return visitor.visitChildren(self)




    def atom(self):

        localctx = CalculantlrParser.AtomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_atom)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 43
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1835008) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[0] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 7:
                return self.precpred(self._ctx, 1)
         




