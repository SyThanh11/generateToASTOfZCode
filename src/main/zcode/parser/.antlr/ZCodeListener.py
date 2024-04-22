# Generated from d:/Bach Khoa/HKVI/PPL/BTL2_Update_2/src/main/zcode/parser/ZCode.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .ZCodeParser import ZCodeParser
else:
    from ZCodeParser import ZCodeParser

# This class defines a complete listener for a parse tree produced by ZCodeParser.
class ZCodeListener(ParseTreeListener):

    # Enter a parse tree produced by ZCodeParser#program.
    def enterProgram(self, ctx:ZCodeParser.ProgramContext):
        pass

    # Exit a parse tree produced by ZCodeParser#program.
    def exitProgram(self, ctx:ZCodeParser.ProgramContext):
        pass


    # Enter a parse tree produced by ZCodeParser#declist.
    def enterDeclist(self, ctx:ZCodeParser.DeclistContext):
        pass

    # Exit a parse tree produced by ZCodeParser#declist.
    def exitDeclist(self, ctx:ZCodeParser.DeclistContext):
        pass


    # Enter a parse tree produced by ZCodeParser#declared.
    def enterDeclared(self, ctx:ZCodeParser.DeclaredContext):
        pass

    # Exit a parse tree produced by ZCodeParser#declared.
    def exitDeclared(self, ctx:ZCodeParser.DeclaredContext):
        pass


    # Enter a parse tree produced by ZCodeParser#vardecl.
    def enterVardecl(self, ctx:ZCodeParser.VardeclContext):
        pass

    # Exit a parse tree produced by ZCodeParser#vardecl.
    def exitVardecl(self, ctx:ZCodeParser.VardeclContext):
        pass


    # Enter a parse tree produced by ZCodeParser#vardecl_1.
    def enterVardecl_1(self, ctx:ZCodeParser.Vardecl_1Context):
        pass

    # Exit a parse tree produced by ZCodeParser#vardecl_1.
    def exitVardecl_1(self, ctx:ZCodeParser.Vardecl_1Context):
        pass


    # Enter a parse tree produced by ZCodeParser#vardecl_2.
    def enterVardecl_2(self, ctx:ZCodeParser.Vardecl_2Context):
        pass

    # Exit a parse tree produced by ZCodeParser#vardecl_2.
    def exitVardecl_2(self, ctx:ZCodeParser.Vardecl_2Context):
        pass


    # Enter a parse tree produced by ZCodeParser#vardecl_3.
    def enterVardecl_3(self, ctx:ZCodeParser.Vardecl_3Context):
        pass

    # Exit a parse tree produced by ZCodeParser#vardecl_3.
    def exitVardecl_3(self, ctx:ZCodeParser.Vardecl_3Context):
        pass


    # Enter a parse tree produced by ZCodeParser#typ_lit.
    def enterTyp_lit(self, ctx:ZCodeParser.Typ_litContext):
        pass

    # Exit a parse tree produced by ZCodeParser#typ_lit.
    def exitTyp_lit(self, ctx:ZCodeParser.Typ_litContext):
        pass


    # Enter a parse tree produced by ZCodeParser#arraydecl.
    def enterArraydecl(self, ctx:ZCodeParser.ArraydeclContext):
        pass

    # Exit a parse tree produced by ZCodeParser#arraydecl.
    def exitArraydecl(self, ctx:ZCodeParser.ArraydeclContext):
        pass


    # Enter a parse tree produced by ZCodeParser#numberlist.
    def enterNumberlist(self, ctx:ZCodeParser.NumberlistContext):
        pass

    # Exit a parse tree produced by ZCodeParser#numberlist.
    def exitNumberlist(self, ctx:ZCodeParser.NumberlistContext):
        pass


    # Enter a parse tree produced by ZCodeParser#funcdecl.
    def enterFuncdecl(self, ctx:ZCodeParser.FuncdeclContext):
        pass

    # Exit a parse tree produced by ZCodeParser#funcdecl.
    def exitFuncdecl(self, ctx:ZCodeParser.FuncdeclContext):
        pass


    # Enter a parse tree produced by ZCodeParser#parameter_list.
    def enterParameter_list(self, ctx:ZCodeParser.Parameter_listContext):
        pass

    # Exit a parse tree produced by ZCodeParser#parameter_list.
    def exitParameter_list(self, ctx:ZCodeParser.Parameter_listContext):
        pass


    # Enter a parse tree produced by ZCodeParser#parameter.
    def enterParameter(self, ctx:ZCodeParser.ParameterContext):
        pass

    # Exit a parse tree produced by ZCodeParser#parameter.
    def exitParameter(self, ctx:ZCodeParser.ParameterContext):
        pass


    # Enter a parse tree produced by ZCodeParser#statement_list.
    def enterStatement_list(self, ctx:ZCodeParser.Statement_listContext):
        pass

    # Exit a parse tree produced by ZCodeParser#statement_list.
    def exitStatement_list(self, ctx:ZCodeParser.Statement_listContext):
        pass


    # Enter a parse tree produced by ZCodeParser#statement_prime.
    def enterStatement_prime(self, ctx:ZCodeParser.Statement_primeContext):
        pass

    # Exit a parse tree produced by ZCodeParser#statement_prime.
    def exitStatement_prime(self, ctx:ZCodeParser.Statement_primeContext):
        pass


    # Enter a parse tree produced by ZCodeParser#statement.
    def enterStatement(self, ctx:ZCodeParser.StatementContext):
        pass

    # Exit a parse tree produced by ZCodeParser#statement.
    def exitStatement(self, ctx:ZCodeParser.StatementContext):
        pass


    # Enter a parse tree produced by ZCodeParser#declaration_statement.
    def enterDeclaration_statement(self, ctx:ZCodeParser.Declaration_statementContext):
        pass

    # Exit a parse tree produced by ZCodeParser#declaration_statement.
    def exitDeclaration_statement(self, ctx:ZCodeParser.Declaration_statementContext):
        pass


    # Enter a parse tree produced by ZCodeParser#assignment_statement.
    def enterAssignment_statement(self, ctx:ZCodeParser.Assignment_statementContext):
        pass

    # Exit a parse tree produced by ZCodeParser#assignment_statement.
    def exitAssignment_statement(self, ctx:ZCodeParser.Assignment_statementContext):
        pass


    # Enter a parse tree produced by ZCodeParser#lhs.
    def enterLhs(self, ctx:ZCodeParser.LhsContext):
        pass

    # Exit a parse tree produced by ZCodeParser#lhs.
    def exitLhs(self, ctx:ZCodeParser.LhsContext):
        pass


    # Enter a parse tree produced by ZCodeParser#array_lhs.
    def enterArray_lhs(self, ctx:ZCodeParser.Array_lhsContext):
        pass

    # Exit a parse tree produced by ZCodeParser#array_lhs.
    def exitArray_lhs(self, ctx:ZCodeParser.Array_lhsContext):
        pass


    # Enter a parse tree produced by ZCodeParser#if_statement.
    def enterIf_statement(self, ctx:ZCodeParser.If_statementContext):
        pass

    # Exit a parse tree produced by ZCodeParser#if_statement.
    def exitIf_statement(self, ctx:ZCodeParser.If_statementContext):
        pass


    # Enter a parse tree produced by ZCodeParser#elif_list_part.
    def enterElif_list_part(self, ctx:ZCodeParser.Elif_list_partContext):
        pass

    # Exit a parse tree produced by ZCodeParser#elif_list_part.
    def exitElif_list_part(self, ctx:ZCodeParser.Elif_list_partContext):
        pass


    # Enter a parse tree produced by ZCodeParser#for_statement.
    def enterFor_statement(self, ctx:ZCodeParser.For_statementContext):
        pass

    # Exit a parse tree produced by ZCodeParser#for_statement.
    def exitFor_statement(self, ctx:ZCodeParser.For_statementContext):
        pass


    # Enter a parse tree produced by ZCodeParser#break_statement.
    def enterBreak_statement(self, ctx:ZCodeParser.Break_statementContext):
        pass

    # Exit a parse tree produced by ZCodeParser#break_statement.
    def exitBreak_statement(self, ctx:ZCodeParser.Break_statementContext):
        pass


    # Enter a parse tree produced by ZCodeParser#continue_statement.
    def enterContinue_statement(self, ctx:ZCodeParser.Continue_statementContext):
        pass

    # Exit a parse tree produced by ZCodeParser#continue_statement.
    def exitContinue_statement(self, ctx:ZCodeParser.Continue_statementContext):
        pass


    # Enter a parse tree produced by ZCodeParser#return_statement.
    def enterReturn_statement(self, ctx:ZCodeParser.Return_statementContext):
        pass

    # Exit a parse tree produced by ZCodeParser#return_statement.
    def exitReturn_statement(self, ctx:ZCodeParser.Return_statementContext):
        pass


    # Enter a parse tree produced by ZCodeParser#call_statement.
    def enterCall_statement(self, ctx:ZCodeParser.Call_statementContext):
        pass

    # Exit a parse tree produced by ZCodeParser#call_statement.
    def exitCall_statement(self, ctx:ZCodeParser.Call_statementContext):
        pass


    # Enter a parse tree produced by ZCodeParser#block_statement.
    def enterBlock_statement(self, ctx:ZCodeParser.Block_statementContext):
        pass

    # Exit a parse tree produced by ZCodeParser#block_statement.
    def exitBlock_statement(self, ctx:ZCodeParser.Block_statementContext):
        pass


    # Enter a parse tree produced by ZCodeParser#list_literal.
    def enterList_literal(self, ctx:ZCodeParser.List_literalContext):
        pass

    # Exit a parse tree produced by ZCodeParser#list_literal.
    def exitList_literal(self, ctx:ZCodeParser.List_literalContext):
        pass


    # Enter a parse tree produced by ZCodeParser#literal.
    def enterLiteral(self, ctx:ZCodeParser.LiteralContext):
        pass

    # Exit a parse tree produced by ZCodeParser#literal.
    def exitLiteral(self, ctx:ZCodeParser.LiteralContext):
        pass


    # Enter a parse tree produced by ZCodeParser#array_literal.
    def enterArray_literal(self, ctx:ZCodeParser.Array_literalContext):
        pass

    # Exit a parse tree produced by ZCodeParser#array_literal.
    def exitArray_literal(self, ctx:ZCodeParser.Array_literalContext):
        pass


    # Enter a parse tree produced by ZCodeParser#funcall.
    def enterFuncall(self, ctx:ZCodeParser.FuncallContext):
        pass

    # Exit a parse tree produced by ZCodeParser#funcall.
    def exitFuncall(self, ctx:ZCodeParser.FuncallContext):
        pass


    # Enter a parse tree produced by ZCodeParser#explist.
    def enterExplist(self, ctx:ZCodeParser.ExplistContext):
        pass

    # Exit a parse tree produced by ZCodeParser#explist.
    def exitExplist(self, ctx:ZCodeParser.ExplistContext):
        pass


    # Enter a parse tree produced by ZCodeParser#expression.
    def enterExpression(self, ctx:ZCodeParser.ExpressionContext):
        pass

    # Exit a parse tree produced by ZCodeParser#expression.
    def exitExpression(self, ctx:ZCodeParser.ExpressionContext):
        pass


    # Enter a parse tree produced by ZCodeParser#exp1.
    def enterExp1(self, ctx:ZCodeParser.Exp1Context):
        pass

    # Exit a parse tree produced by ZCodeParser#exp1.
    def exitExp1(self, ctx:ZCodeParser.Exp1Context):
        pass


    # Enter a parse tree produced by ZCodeParser#exp2.
    def enterExp2(self, ctx:ZCodeParser.Exp2Context):
        pass

    # Exit a parse tree produced by ZCodeParser#exp2.
    def exitExp2(self, ctx:ZCodeParser.Exp2Context):
        pass


    # Enter a parse tree produced by ZCodeParser#exp3.
    def enterExp3(self, ctx:ZCodeParser.Exp3Context):
        pass

    # Exit a parse tree produced by ZCodeParser#exp3.
    def exitExp3(self, ctx:ZCodeParser.Exp3Context):
        pass


    # Enter a parse tree produced by ZCodeParser#exp4.
    def enterExp4(self, ctx:ZCodeParser.Exp4Context):
        pass

    # Exit a parse tree produced by ZCodeParser#exp4.
    def exitExp4(self, ctx:ZCodeParser.Exp4Context):
        pass


    # Enter a parse tree produced by ZCodeParser#exp5.
    def enterExp5(self, ctx:ZCodeParser.Exp5Context):
        pass

    # Exit a parse tree produced by ZCodeParser#exp5.
    def exitExp5(self, ctx:ZCodeParser.Exp5Context):
        pass


    # Enter a parse tree produced by ZCodeParser#exp6.
    def enterExp6(self, ctx:ZCodeParser.Exp6Context):
        pass

    # Exit a parse tree produced by ZCodeParser#exp6.
    def exitExp6(self, ctx:ZCodeParser.Exp6Context):
        pass


    # Enter a parse tree produced by ZCodeParser#exp7.
    def enterExp7(self, ctx:ZCodeParser.Exp7Context):
        pass

    # Exit a parse tree produced by ZCodeParser#exp7.
    def exitExp7(self, ctx:ZCodeParser.Exp7Context):
        pass


    # Enter a parse tree produced by ZCodeParser#exp8.
    def enterExp8(self, ctx:ZCodeParser.Exp8Context):
        pass

    # Exit a parse tree produced by ZCodeParser#exp8.
    def exitExp8(self, ctx:ZCodeParser.Exp8Context):
        pass


    # Enter a parse tree produced by ZCodeParser#ignore.
    def enterIgnore(self, ctx:ZCodeParser.IgnoreContext):
        pass

    # Exit a parse tree produced by ZCodeParser#ignore.
    def exitIgnore(self, ctx:ZCodeParser.IgnoreContext):
        pass



del ZCodeParser