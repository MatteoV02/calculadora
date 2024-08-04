import sys
from antlr4 import *
from dist.CalculantlrLexer import CalculantlrLexer
from dist.CalculantlrParser import CalculantlrParser
from dist.CalculantlrVisitor import CalculantlrVisitor

class CalcVisitor(CalculantlrVisitor):
    def visitAtomExpr(self, ctx:CalculantlrParser.AtomExprContext):
        if ctx.getText() == 'true':
            return True
        elif ctx.getText() == 'false':
            return False
        else:
            return int(ctx.getText())

    def visitParenExpr(self, ctx:CalculantlrParser.ParenExprContext):
        return self.visit(ctx.expr())

    def visitNotExpr(self, ctx:CalculantlrParser.NotExprContext):
        operand = self.visit(ctx.expr())
        return not operand

    def visitMulDivExpr(self, ctx:CalculantlrParser.MulDivExprContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))

        op = ctx.op.text
        if op == '*':
            return left * right
        elif op == '/':
            if right == 0:
                print('¡División por cero!')
                return 0
            return left / right

    def visitAddSubExpr(self, ctx:CalculantlrParser.AddSubExprContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))

        op = ctx.op.text
        if op == '+':
            return left + right
        elif op == '-':
            return left - right

    def visitComparisonExpr(self, ctx:CalculantlrParser.ComparisonExprContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))

        op = ctx.op.text
        if op == '>':
            return left > right
        elif op == '>=':
            return left >= right
        elif op == '<':
            return left < right
        elif op == '<=':
            return left <= right

    def visitEqualityExpr(self, ctx:CalculantlrParser.EqualityExprContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))

        op = ctx.op.text
        if op == '==':
            return left == right
        elif op == '!=':
            return left != right

    def visitAndExpr(self, ctx:CalculantlrParser.AndExprContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        return left and right

    def visitOrExpr(self, ctx:CalculantlrParser.OrExprContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        return left or right

    def visitNandExpr(self, ctx:CalculantlrParser.NandExprContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        return not (left and right)

    def visitXorExpr(self, ctx:CalculantlrParser.XorExprContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        return left != right

def calc(line) -> float:
    input_stream = InputStream(line)

    # Lexing
    lexer = CalculantlrLexer(input_stream)
    stream = CommonTokenStream(lexer)

    # Parsing
    parser = CalculantlrParser(stream)
    tree = parser.expr()

    # Utilizar el visitante personalizado para recorrer el AST
    visitor = CalcVisitor()
    return visitor.visit(tree)

if __name__ == '__main__':
    while True:
        print(">>> ", end='')
        line = input()
        if line.lower() == 'exit':
            break
        try:
            print(calc(line))
        except Exception as e:
            print("Error:", e)

