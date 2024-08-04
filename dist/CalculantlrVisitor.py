# Generated from Calculantlr.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .CalculantlrParser import CalculantlrParser
else:
    from CalculantlrParser import CalculantlrParser

# This class defines a complete generic visitor for a parse tree produced by CalculantlrParser.

class CalculantlrVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by CalculantlrParser#AndExpr.
    def visitAndExpr(self, ctx:CalculantlrParser.AndExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculantlrParser#NandExpr.
    def visitNandExpr(self, ctx:CalculantlrParser.NandExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculantlrParser#MulDivExpr.
    def visitMulDivExpr(self, ctx:CalculantlrParser.MulDivExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculantlrParser#EqualityExpr.
    def visitEqualityExpr(self, ctx:CalculantlrParser.EqualityExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculantlrParser#ComparisonExpr.
    def visitComparisonExpr(self, ctx:CalculantlrParser.ComparisonExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculantlrParser#XorExpr.
    def visitXorExpr(self, ctx:CalculantlrParser.XorExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculantlrParser#NotExpr.
    def visitNotExpr(self, ctx:CalculantlrParser.NotExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculantlrParser#ParenExpr.
    def visitParenExpr(self, ctx:CalculantlrParser.ParenExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculantlrParser#AtomExpr.
    def visitAtomExpr(self, ctx:CalculantlrParser.AtomExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculantlrParser#AddSubExpr.
    def visitAddSubExpr(self, ctx:CalculantlrParser.AddSubExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculantlrParser#OrExpr.
    def visitOrExpr(self, ctx:CalculantlrParser.OrExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculantlrParser#atom.
    def visitAtom(self, ctx:CalculantlrParser.AtomContext):
        return self.visitChildren(ctx)



del CalculantlrParser