from ExprParser import ExprParser
from ExprVisitor import ExprVisitor
import math

class MyExprVisitor(ExprVisitor):
    def __init__(self):
        super(MyExprVisitor, self).__init__()
        self.stack = []  # Stack to evaluate the expression

    # Visit a parse tree produced by ExprParser#prog.
    def visitProg(self, ctx: ExprParser.ProgContext):
        return self.visit(ctx.expr())  # Just visit the self expression

    # Visit a parse tree produced by ExprParser#infixExpr.
    def visitInfixExpr(self, ctx: ExprParser.InfixExprContext):
        self.visit(ctx.left)  # Evaluate the left  expression and push to stack
        self.visit(ctx.right)  # Evaluate the right expression and push to stack

        b = self.stack.pop()  # Why is ‘b’ the first popped item?
        a = self.stack.pop()
        c = None

        if ctx.OP_POW():
            c = pow(a, b)
        elif ctx.OP_ADD():
            c = a + b
        elif ctx.OP_SUB():
            c = a - b
        elif ctx.OP_MUL():
            c = a * b
        elif ctx.OP_DIV():
            c = a / b

        self.stack.append(c)
        return c

    # Visit a parse tree produced by ExprParser#numberExpr.
    def visitNumberExpr(self, ctx: ExprParser.NumberExprContext):
        c = int(str(ctx.INT()))  # Found a number, just insert to stack
        self.stack.append(c)
        return c

    # Visit a parse tree produced by ExprParser#parensExpr.
    def visitParensExpr(self, ctx: ExprParser.ParensExprContext):
        return self.visit(ctx.expr())  # Since enclosed by parents, just visit expr


    def visitLogExpr(self, ctx: ExprParser.LogExprContext):
        self.visit(ctx.expr())
        a = self.stack.pop()
        result = math.log10(a)
        self.stack.append(result)
        return result

    def visitSinExpr(self, ctx: ExprParser.SinExprContext):
        self.visit(ctx.expr())
        a = self.stack.pop()
        result = math.sin(a)
        self.stack.append(result)
        return result

    def visitCosExpr(self, ctx: ExprParser.CosExprContext):
        self.visit(ctx.expr())
        a = self.stack.pop()
        result = math.cos(a)
        self.stack.append(result)
        return result

    def visitTanExpr(self, ctx: ExprParser.TanExprContext):
        self.visit(ctx.expr())
        a = self.stack.pop()
        result = math.tan(a)
        self.stack.append(result)
        return result

    def visitAsinExpr(self, ctx: ExprParser.AsinExprContext):
        self.visit(ctx.expr())
        a = self.stack.pop()
        result = math.asin(a)
        self.stack.append(result)
        return result

    def visitAcosExpr(self, ctx: ExprParser.AcosExprContext):
        self.visit(ctx.expr())
        a = self.stack.pop()
        result = math.acos(a)
        self.stack.append(result)
        return result

    def visitAtanExpr(self, ctx: ExprParser.AtanExprContext):
        self.visit(ctx.expr())
        a = self.stack.pop()
        result = math.atan(a)
        self.stack.append(result)
        return result

    def visitFacExpr(self, ctx: ExprParser.FacExprContext):
        self.visit(ctx.expr())
        a = self.stack.pop()
        result = math.factorial(a)
        self.stack.append(result)
        return result

    def visitSqrtExpr(self, ctx: ExprParser.SqrtExprContext):
        self.visit(ctx.expr())
        a = self.stack.pop()
        result = math.sqrt(a)
        self.stack.append(result)
        return result

    def visitCmtoinExpr(self, ctx: ExprParser.CmtoinExprContext):
        self.visit(ctx.expr())
        a = self.stack.pop()
        result = a * 0.3937
        self.stack.append(result)
        return result

    def visitMtoftExpr(self, ctx: ExprParser.MtoftExprContext):
        self.visit(ctx.expr())
        a = self.stack.pop()
        result = a * 3.28084
        self.stack.append(result)
        return result

    def visitKgtolbExpr(self, ctx: ExprParser.MtoftExprContext):
        self.visit(ctx.expr())
        a = self.stack.pop()
        result = a * 2.2046
        self.stack.append(result)
        return result

