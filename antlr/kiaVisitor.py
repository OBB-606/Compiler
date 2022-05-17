# Generated from kia.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .kiaParser import kiaParser
else:
    from kiaParser import kiaParser

# This class defines a complete generic visitor for a parse tree produced by kiaParser.

class kiaVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by kiaParser#program.
    def visitProgram(self, ctx:kiaParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by kiaParser#block.
    def visitBlock(self, ctx:kiaParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by kiaParser#vars_.
    def visitVars_(self, ctx:kiaParser.Vars_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by kiaParser#types.
    def visitTypes(self, ctx:kiaParser.TypesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by kiaParser#function.
    def visitFunction(self, ctx:kiaParser.FunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by kiaParser#statement.
    def visitStatement(self, ctx:kiaParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by kiaParser#assign.
    def visitAssign(self, ctx:kiaParser.AssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by kiaParser#call.
    def visitCall(self, ctx:kiaParser.CallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by kiaParser#print_.
    def visitPrint_(self, ctx:kiaParser.Print_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by kiaParser#literal.
    def visitLiteral(self, ctx:kiaParser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by kiaParser#beginstmt.
    def visitBeginstmt(self, ctx:kiaParser.BeginstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by kiaParser#if_.
    def visitIf_(self, ctx:kiaParser.If_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by kiaParser#while_.
    def visitWhile_(self, ctx:kiaParser.While_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by kiaParser#break_cont.
    def visitBreak_cont(self, ctx:kiaParser.Break_contContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by kiaParser#condition.
    def visitCondition(self, ctx:kiaParser.ConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by kiaParser#and_or.
    def visitAnd_or(self, ctx:kiaParser.And_orContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by kiaParser#compare_operators.
    def visitCompare_operators(self, ctx:kiaParser.Compare_operatorsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by kiaParser#expression.
    def visitExpression(self, ctx:kiaParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by kiaParser#term.
    def visitTerm(self, ctx:kiaParser.TermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by kiaParser#factor.
    def visitFactor(self, ctx:kiaParser.FactorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by kiaParser#variable.
    def visitVariable(self, ctx:kiaParser.VariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by kiaParser#digit.
    def visitDigit(self, ctx:kiaParser.DigitContext):
        return self.visitChildren(ctx)



del kiaParser