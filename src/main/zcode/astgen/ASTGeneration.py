from ZCodeVisitor import ZCodeVisitor
from ZCodeParser import ZCodeParser
from AST import *


class ASTGeneration(ZCodeVisitor):

    # program: declist EOF;
    def visitProgram(self, ctx:ZCodeParser.ProgramContext):
        declist_result = self.visit(ctx.declist())
        declist_result = [decl for decl in declist_result if decl is not None]
        return Program(declist_result)

    # declist: declared declist | declared;
    def visitDeclist(self, ctx:ZCodeParser.DeclistContext):
        if ctx.declist():
            return [self.visit(ctx.declared())] + self.visit(ctx.declist())
        return [self.visit(ctx.declared())]

    # declared: vardecl | funcdecl | ignore;
    def visitDeclared(self, ctx:ZCodeParser.DeclaredContext):
        if ctx.vardecl():
            return self.visit(ctx.vardecl())
        elif ctx.funcdecl():
            return self.visit(ctx.funcdecl())
        return None

    # vardecl: ( ( vardecl_1 | vardecl_2 | vardecl_3 ) ignore ) | ignore;
    def visitVardecl(self, ctx:ZCodeParser.VardeclContext):
        if ctx.vardecl_1():
            return self.visit(ctx.vardecl_1())
        elif ctx.vardecl_2():
            return self.visit(ctx.vardecl_2())
        elif ctx.vardecl_3():
            return self.visit(ctx.vardecl_3())

    # vardecl_1: VAR ID ASSIGN expression;
    def visitVardecl_1(self, ctx:ZCodeParser.Vardecl_1Context):
        return VarDecl(Id(ctx.ID().getText()), None, ctx.VAR().getText(), self.visit(ctx.expression()))

    # vardecl_2: typ_lit ID (LBRACKET numberlist RBRACKET)? (ASSIGN expression)?;
    def visitVardecl_2(self, ctx:ZCodeParser.Vardecl_2Context):
        expr = None
        if ctx.expression():
            expr = self.visit(ctx.expression())
        typ = self.visit(ctx.typ_lit())
        if ctx.numberlist():
            typ = ArrayType(self.visit(ctx.numberlist()), typ)
        return VarDecl(Id(ctx.ID().getText()), typ, None, expr)

    # vardecl_3: DYNAMIC ID (ASSIGN expression)?;
    def visitVardecl_3(self, ctx:ZCodeParser.Vardecl_3Context):
        expr = None
        if ctx.expression():
            expr = self.visit(ctx.expression())
        return VarDecl(Id(ctx.ID().getText()), None, ctx.DYNAMIC().getText(), expr)

    # typ_lit: BOOL | NUMBER | STRING;
    def visitTyp_lit(self, ctx:ZCodeParser.Typ_litContext):
        if ctx.BOOL():
            return BoolType()
        elif ctx.NUMBER():
            return NumberType()
        elif ctx.STRING():
            return StringType()

    # arraydecl: ID LBRACKET numberlist RBRACKET;
    def visitArraydecl(self, ctx:ZCodeParser.ArraydeclContext):
        return self.visitChildren(ctx)

    # numberlist: NUMBER_LIT COMMA numberlist | NUMBER_LIT;
    def visitNumberlist(self, ctx:ZCodeParser.NumberlistContext):
        if ctx.getChildCount() == 3:
            return [float(ctx.NUMBER_LIT().getText())] + self.visit(ctx.numberlist())
        return [float(ctx.NUMBER_LIT().getText())]

    # funcdecl: FUNC ID LPAREN parameter_list? RPAREN (ignore? return_statement | ignore? block_statement | ignore);
    def visitFuncdecl(self, ctx:ZCodeParser.FuncdeclContext):
        func_id = ctx.ID().getText()
        param_list = self.visit(ctx.parameter_list()) if ctx.parameter_list() else []
        block_stmt = self.visit(ctx.block_statement()) if ctx.block_statement() else None
        return_stmt = self.visit(ctx.return_statement()) if ctx.return_statement() else None

        return FuncDecl(Id(func_id), param_list, block_stmt or return_stmt or None)

    # parameter_list: parameter COMMA parameter_list | parameter;
    def visitParameter_list(self, ctx:ZCodeParser.Parameter_listContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.parameter())]
        return [self.visit(ctx.parameter())] + self.visit(ctx.parameter_list())

    # parameter: typ_lit ID (LBRACKET numberlist RBRACKET)?;
    def visitParameter(self, ctx:ZCodeParser.ParameterContext):
        typ = self.visit(ctx.typ_lit()) 
        if ctx.numberlist():
            typ = ArrayType(self.visit(ctx.numberlist()), typ)

        return VarDecl(Id(ctx.ID().getText()), typ, None, None)

    # statement_list: statement_prime | ;
    def visitStatement_list(self, ctx:ZCodeParser.Statement_listContext):
        if ctx.statement_prime():
            return self.visit(ctx.statement_prime())
        return []
    
    # statement_prime: statement ignore? statement_prime | statement;
    def visitStatement_prime(self, ctx:ZCodeParser.Statement_primeContext):
        return [self.visit(ctx.statement())] if ctx.getChildCount() == 1 else [self.visit(ctx.statement())] + self.visit(ctx.statement_prime())

    # statement: declaration_statement | assignment_statement | if_statement | for_statement | break_statement | continue_statement | return_statement  | call_statement | block_statement;
    def visitStatement(self, ctx:ZCodeParser.StatementContext):
        if ctx.declaration_statement():
            return self.visit(ctx.declaration_statement())
        elif ctx.assignment_statement():
            return self.visit(ctx.assignment_statement())
        elif ctx.if_statement():
            return self.visit(ctx.if_statement())
        elif ctx.for_statement():
            return self.visit(ctx.for_statement())
        elif ctx.break_statement():
            return self.visit(ctx.break_statement())
        elif ctx.continue_statement():
            return self.visit(ctx.continue_statement())
        elif ctx.return_statement():
            return self.visit(ctx.return_statement())
        elif ctx.call_statement():
            return self.visit(ctx.call_statement())
        elif ctx.block_statement():
            return self.visit(ctx.block_statement())

    # declaration_statement: ( vardecl_1 | vardecl_2 | vardecl_3 ) ignore;
    def visitDeclaration_statement(self, ctx:ZCodeParser.Declaration_statementContext):
        if ctx.vardecl_1():
            return self.visit(ctx.vardecl_1())
        elif ctx.vardecl_2():
            return self.visit(ctx.vardecl_2())
        elif ctx.vardecl_3():
            return self.visit(ctx.vardecl_3())

    # assignment_statement: lhs ASSIGN expression ignore;
    def visitAssignment_statement(self, ctx:ZCodeParser.Assignment_statementContext):
        return Assign(self.visit(ctx.lhs()), self.visit(ctx.expression()))

    # lhs: array_lhs | ID;
    def visitLhs(self, ctx:ZCodeParser.LhsContext):
        if ctx.array_lhs():
            return self.visit(ctx.array_lhs())
        return Id(ctx.ID().getText())

    # array_lhs: ID LBRACKET explist RBRACKET;
    def visitArray_lhs(self, ctx:ZCodeParser.Array_lhsContext):
        return ArrayCell(Id(ctx.ID().getText()), self.visit(ctx.explist()))

    # if_statement: IF LPAREN expression RPAREN ignore? statement elif_list_part (ELSE ignore? statement)?;
    def visitIf_statement(self, ctx:ZCodeParser.If_statementContext):
        if not ctx.ELSE():
            return If(self.visit(ctx.expression()), 
                        self.visit(ctx.statement()[0]), 
                        self.visit(ctx.elif_list_part()),None)

        return If(self.visit(ctx.expression()), 
                  self.visit(ctx.statement()[0]), 
                  self.visit(ctx.elif_list_part()),
                  self.visit(ctx.statement()[1]))

    # elif_list_part: ELIF LPAREN expression RPAREN ignore? statement elif_list_part | ;
    def visitElif_list_part(self, ctx:ZCodeParser.Elif_list_partContext):
        if ctx.getChildCount() == 0:
            return []
        return [(self.visit(ctx.expression()), self.visit(ctx.statement()))] + self.visit(ctx.elif_list_part())

    # for_statement: FOR ID UNTIL expression BY expression ignore? statement;
    def visitFor_statement(self, ctx:ZCodeParser.For_statementContext):
        return For(Id(ctx.ID().getText()), self.visit(ctx.expression()[0]), self.visit(ctx.expression()[1]), self.visit(ctx.statement()))

    # break_statement: BREAK ignore;
    def visitBreak_statement(self, ctx:ZCodeParser.Break_statementContext):
        return Break()

    # continue_statement: CONTINUE ignore;
    def visitContinue_statement(self, ctx:ZCodeParser.Continue_statementContext):
        return Continue()

    # return_statement: RETURN expression? ignore;
    def visitReturn_statement(self, ctx:ZCodeParser.Return_statementContext):
        return Return(self.visit(ctx.expression()) if ctx.expression() else None)

    # call_statement: ID LPAREN explist? RPAREN ignore;
    def visitCall_statement(self, ctx:ZCodeParser.Call_statementContext):
        return CallStmt(Id(ctx.ID().getText()), self.visit(ctx.explist()) if ctx.explist() else [])

    # block_statement: BEGIN ignore statement_list? END ignore;
    def visitBlock_statement(self, ctx:ZCodeParser.Block_statementContext):
        return Block(self.visit(ctx.statement_list()) if ctx.statement_list() else [])

    # list_literal: literal COMMA list_literal | literal;
    def visitList_literal(self, ctx:ZCodeParser.List_literalContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.literal())]
        return [self.visit(ctx.literal())] + self.visit(ctx.list_literal())

    # literal: NUMBER_LIT | STRING_LIT | TRUE | FALSE | array_literal;
    def visitLiteral(self, ctx:ZCodeParser.LiteralContext):
        if ctx.NUMBER_LIT():
            return NumberLiteral(float(ctx.NUMBER_LIT().getText()))  
        elif ctx.STRING_LIT():
            return StringLiteral(ctx.STRING_LIT().getText())
        elif ctx.TRUE():
            return BooleanLiteral(True)
        elif ctx.FALSE():
            return BooleanLiteral(False)
        elif ctx.array_literal():
            return self.visit(ctx.array_literal())

    # array_literal: LBRACKET explist RBRACKET;
    def visitArray_literal(self, ctx:ZCodeParser.Array_literalContext):
        return ArrayLiteral(self.visit(ctx.explist()))

    # funcall: ID LPAREN explist? RPAREN;
    def visitFuncall(self, ctx:ZCodeParser.FuncallContext):
        return CallExpr(Id(ctx.ID().getText()), self.visit(ctx.explist()) if ctx.explist() else [])

    # explist: expression COMMA explist | expression;
    def visitExplist(self, ctx:ZCodeParser.ExplistContext):
        return [self.visit(ctx.expression())] if ctx.getChildCount() == 1 else [self.visit(ctx.expression())] + self.visit(ctx.explist())

    # expression: exp1 ELLIPSIS exp1 | exp1;
    def visitExpression(self, ctx:ZCodeParser.ExpressionContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.exp1()[0])
        op = ctx.ELLIPSIS().getText()
        left = self.visit(ctx.exp1()[0])
        right = self.visit(ctx.exp1()[1])
        return BinaryOp(op, left, right)

    # exp1: exp2 ( EQ | EQ_EQ | NOT_EQ | LT | GT | LTE | GTE ) exp2 | exp2;
    def visitExp1(self, ctx:ZCodeParser.Exp1Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.exp2()[0])
        op = ''
        if ctx.EQ():
            op = ctx.EQ().getText()
        elif ctx.EQ_EQ():
            op = ctx.EQ_EQ().getText()
        elif ctx.NOT_EQ():
            op = ctx.NOT_EQ().getText()
        elif ctx.LT():
            op = ctx.LT().getText()
        elif ctx.GT():
            op = ctx.GT().getText()
        elif ctx.LTE():
            op = ctx.LTE().getText()
        elif ctx.GTE():
            op = ctx.GTE().getText()
        left = self.visit(ctx.exp2()[0])
        right = self.visit(ctx.exp2()[1])
        return BinaryOp(op, left, right)

    # exp2: exp2 ( AND | OR ) exp3 | exp3;
    def visitExp2(self, ctx:ZCodeParser.Exp2Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.exp3())
        op = ''
        if ctx.AND():
            op = ctx.AND().getText()
        elif ctx.OR():
            op = ctx.OR().getText()
        left = self.visit(ctx.exp2())
        right = self.visit(ctx.exp3())
        return BinaryOp(op, left, right)

    # exp3: exp3 ( PLUS | MINUS ) exp4 | exp4;
    def visitExp3(self, ctx:ZCodeParser.Exp3Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.exp4())
        op = ''
        if ctx.PLUS():
            op = ctx.PLUS().getText()
        elif ctx.MINUS():
            op = ctx.MINUS().getText()
        left = self.visit(ctx.exp3())
        right = self.visit(ctx.exp4())
        return BinaryOp(op, left, right)

    # exp4: exp4 ( MUL | DIV | MOD ) exp5 | exp5;
    def visitExp4(self, ctx:ZCodeParser.Exp4Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.exp5())
        op = ''
        if ctx.MUL():
            op = ctx.MUL().getText()
        elif ctx.DIV():
            op = ctx.DIV().getText()
        elif ctx.MOD():
            op = ctx.MOD().getText()
        left = self.visit(ctx.exp4())
        right = self.visit(ctx.exp5())
        return BinaryOp(op, left, right)

    # exp5: NOT exp5 | exp6
    def visitExp5(self, ctx:ZCodeParser.Exp5Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.exp6())
        op = ctx.NOT().getText()
        operand = self.visit(ctx.exp5())
        return UnaryOp(op, operand)

    # exp6: (MINUS | PLUS) exp6 | exp7;
    def visitExp6(self, ctx:ZCodeParser.Exp6Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.exp7())
        op = ''
        if ctx.MINUS():
            op = ctx.MINUS().getText()
        elif ctx.PLUS():
            op = ctx.PLUS().getText()
        operand = self.visit(ctx.exp6())
        return UnaryOp(op, operand)

    # exp7: (ID | ID LPAREN explist? RPAREN) LBRACKET explist RBRACKET | exp8;
    def visitExp7(self, ctx:ZCodeParser.Exp7Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.exp8())
        elif ctx.getChildCount() == 4:
            return ArrayCell(Id(ctx.ID().getText()), self.visit(ctx.explist()[0]))
        elif len(ctx.explist()) == 2:
            return ArrayCell(CallExpr(Id(ctx.ID().getText()), self.visit(ctx.explist()[0])), self.visit(ctx.explist()[1]))
        return ArrayCell(CallExpr(Id(ctx.ID().getText()), []), self.visit(ctx.explist()[0]))

    # exp8: funcall | ID | literal | LPAREN expression RPAREN; 
    def visitExp8(self, ctx:ZCodeParser.Exp8Context):
        if ctx.funcall():
            return self.visit(ctx.funcall())
        elif ctx.ID():
            return Id(ctx.ID().getText())
        elif ctx.literal():
            return self.visit(ctx.literal())
        elif ctx.expression():
            return self.visit(ctx.expression())

    # Visit a parse tree produced by ZCodeParser#ignore.
    def visitIgnore(self, ctx:ZCodeParser.IgnoreContext):
        return None
