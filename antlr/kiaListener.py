# Generated from kia.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .kiaParser import kiaParser
else:
    from kiaParser import kiaParser

# This class defines a complete listener for a parse tree produced by kiaParser.
class kiaListener(ParseTreeListener):

    # Enter a parse tree produced by kiaParser#program.
    def enterProgram(self, ctx:kiaParser.ProgramContext):
        pass

    # Exit a parse tree produced by kiaParser#program.
    def exitProgram(self, ctx:kiaParser.ProgramContext):
        pass


    # Enter a parse tree produced by kiaParser#block.
    def enterBlock(self, ctx:kiaParser.BlockContext):
        pass

    # Exit a parse tree produced by kiaParser#block.
    def exitBlock(self, ctx:kiaParser.BlockContext):
        pass


    # Enter a parse tree produced by kiaParser#vars_.
    def enterVars_(self, ctx:kiaParser.Vars_Context):
        pass

    # Exit a parse tree produced by kiaParser#vars_.
    def exitVars_(self, ctx:kiaParser.Vars_Context):
        pass


    # Enter a parse tree produced by kiaParser#types.
    def enterTypes(self, ctx:kiaParser.TypesContext):
        pass

    # Exit a parse tree produced by kiaParser#types.
    def exitTypes(self, ctx:kiaParser.TypesContext):
        pass


    # Enter a parse tree produced by kiaParser#function.
    def enterFunction(self, ctx:kiaParser.FunctionContext):
        pass

    # Exit a parse tree produced by kiaParser#function.
    def exitFunction(self, ctx:kiaParser.FunctionContext):
        pass


    # Enter a parse tree produced by kiaParser#statement.
    def enterStatement(self, ctx:kiaParser.StatementContext):
        pass

    # Exit a parse tree produced by kiaParser#statement.
    def exitStatement(self, ctx:kiaParser.StatementContext):
        pass


    # Enter a parse tree produced by kiaParser#assign.
    def enterAssign(self, ctx:kiaParser.AssignContext):
        pass

    # Exit a parse tree produced by kiaParser#assign.
    def exitAssign(self, ctx:kiaParser.AssignContext):
        pass


    # Enter a parse tree produced by kiaParser#call.
    def enterCall(self, ctx:kiaParser.CallContext):
        pass

    # Exit a parse tree produced by kiaParser#call.
    def exitCall(self, ctx:kiaParser.CallContext):
        pass


    # Enter a parse tree produced by kiaParser#print_.
    def enterPrint_(self, ctx:kiaParser.Print_Context):
        pass

    # Exit a parse tree produced by kiaParser#print_.
    def exitPrint_(self, ctx:kiaParser.Print_Context):
        pass


    # Enter a parse tree produced by kiaParser#literal.
    def enterLiteral(self, ctx:kiaParser.LiteralContext):
        pass

    # Exit a parse tree produced by kiaParser#literal.
    def exitLiteral(self, ctx:kiaParser.LiteralContext):
        pass


    # Enter a parse tree produced by kiaParser#beginstmt.
    def enterBeginstmt(self, ctx:kiaParser.BeginstmtContext):
        pass

    # Exit a parse tree produced by kiaParser#beginstmt.
    def exitBeginstmt(self, ctx:kiaParser.BeginstmtContext):
        pass


    # Enter a parse tree produced by kiaParser#if_.
    def enterIf_(self, ctx:kiaParser.If_Context):
        pass

    # Exit a parse tree produced by kiaParser#if_.
    def exitIf_(self, ctx:kiaParser.If_Context):
        pass


    # Enter a parse tree produced by kiaParser#while_.
    def enterWhile_(self, ctx:kiaParser.While_Context):
        pass

    # Exit a parse tree produced by kiaParser#while_.
    def exitWhile_(self, ctx:kiaParser.While_Context):
        pass


    # Enter a parse tree produced by kiaParser#break_cont.
    def enterBreak_cont(self, ctx:kiaParser.Break_contContext):
        pass

    # Exit a parse tree produced by kiaParser#break_cont.
    def exitBreak_cont(self, ctx:kiaParser.Break_contContext):
        pass


    # Enter a parse tree produced by kiaParser#condition.
    def enterCondition(self, ctx:kiaParser.ConditionContext):
        pass

    # Exit a parse tree produced by kiaParser#condition.
    def exitCondition(self, ctx:kiaParser.ConditionContext):
        pass


    # Enter a parse tree produced by kiaParser#and_or.
    def enterAnd_or(self, ctx:kiaParser.And_orContext):
        pass

    # Exit a parse tree produced by kiaParser#and_or.
    def exitAnd_or(self, ctx:kiaParser.And_orContext):
        pass


    # Enter a parse tree produced by kiaParser#compare_operators.
    def enterCompare_operators(self, ctx:kiaParser.Compare_operatorsContext):
        pass

    # Exit a parse tree produced by kiaParser#compare_operators.
    def exitCompare_operators(self, ctx:kiaParser.Compare_operatorsContext):
        pass


    # Enter a parse tree produced by kiaParser#expression.
    def enterExpression(self, ctx:kiaParser.ExpressionContext):
        pass

    # Exit a parse tree produced by kiaParser#expression.
    def exitExpression(self, ctx:kiaParser.ExpressionContext):
        pass


    # Enter a parse tree produced by kiaParser#term.
    def enterTerm(self, ctx:kiaParser.TermContext):
        pass

    # Exit a parse tree produced by kiaParser#term.
    def exitTerm(self, ctx:kiaParser.TermContext):
        pass


    # Enter a parse tree produced by kiaParser#factor.
    def enterFactor(self, ctx:kiaParser.FactorContext):
        pass

    # Exit a parse tree produced by kiaParser#factor.
    def exitFactor(self, ctx:kiaParser.FactorContext):
        pass


    # Enter a parse tree produced by kiaParser#variable.
    def enterVariable(self, ctx:kiaParser.VariableContext):
        pass

    # Exit a parse tree produced by kiaParser#variable.
    def exitVariable(self, ctx:kiaParser.VariableContext):
        pass


    # Enter a parse tree produced by kiaParser#digit.
    def enterDigit(self, ctx:kiaParser.DigitContext):
        pass

    # Exit a parse tree produced by kiaParser#digit.
    def exitDigit(self, ctx:kiaParser.DigitContext):
        pass



del kiaParser