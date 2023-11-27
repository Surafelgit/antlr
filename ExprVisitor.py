# Generated from Expr.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .ExprParser import ExprParser
else:
    from ExprParser import ExprParser

# This class defines a complete generic visitor for a parse tree produced by ExprParser.

class ExprVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ExprParser#prog.
    def visitProg(self, ctx:ExprParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#acosExpr.
    def visitAcosExpr(self, ctx:ExprParser.AcosExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#sinExpr.
    def visitSinExpr(self, ctx:ExprParser.SinExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#sqrtExpr.
    def visitSqrtExpr(self, ctx:ExprParser.SqrtExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#numberExpr.
    def visitNumberExpr(self, ctx:ExprParser.NumberExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#facExpr.
    def visitFacExpr(self, ctx:ExprParser.FacExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#kgtolbExpr.
    def visitKgtolbExpr(self, ctx:ExprParser.KgtolbExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#parensExpr.
    def visitParensExpr(self, ctx:ExprParser.ParensExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#logExpr.
    def visitLogExpr(self, ctx:ExprParser.LogExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#atanExpr.
    def visitAtanExpr(self, ctx:ExprParser.AtanExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#infixExpr.
    def visitInfixExpr(self, ctx:ExprParser.InfixExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#cosExpr.
    def visitCosExpr(self, ctx:ExprParser.CosExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#asinExpr.
    def visitAsinExpr(self, ctx:ExprParser.AsinExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#mtoftExpr.
    def visitMtoftExpr(self, ctx:ExprParser.MtoftExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#cmtoinExpr.
    def visitCmtoinExpr(self, ctx:ExprParser.CmtoinExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#tanExpr.
    def visitTanExpr(self, ctx:ExprParser.TanExprContext):
        return self.visitChildren(ctx)



del ExprParser