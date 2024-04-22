grammar ZCode;

@lexer::header {
from lexererr import *
}

options {
	language=Python3;
}

// ! --------------------------  Syntax structure ----------------------- //

// declare
program: declist EOF;
declist: declared declist | declared;
declared: vardecl | funcdecl | ignore;

// declare variables
vardecl: ( vardecl_1 | vardecl_2 | vardecl_3 ) ignore;
vardecl_1: VAR ID ASSIGN expression;
vardecl_2: typ_lit ID (LBRACKET numberlist RBRACKET)? (ASSIGN expression)?;
vardecl_3: DYNAMIC ID (ASSIGN expression)?;
typ_lit: BOOL | NUMBER | STRING;
arraydecl: ID LBRACKET numberlist RBRACKET;
numberlist: NUMBER_LIT COMMA numberlist | NUMBER_LIT;

// declare functions
funcdecl: FUNC ID LPAREN parameter_list? RPAREN (ignore? return_statement | ignore? block_statement | ignore);
parameter_list: parameter COMMA parameter_list | parameter;
parameter: typ_lit ID (LBRACKET numberlist RBRACKET)?;

// statement
statement_list: statement_prime | ;
statement_prime: statement ignore? statement_prime | statement;
statement: declaration_statement | assignment_statement 
            | if_statement | for_statement 
            | break_statement | continue_statement 
            | return_statement  | call_statement | block_statement;

declaration_statement: ( vardecl_1 | vardecl_2 | vardecl_3 ) ignore;

assignment_statement: lhs ASSIGN expression ignore;
lhs: array_lhs | ID;
array_lhs: ID LBRACKET explist RBRACKET;

if_statement: IF LPAREN expression RPAREN ignore? statement elif_list_part (ELSE ignore? statement)?;
elif_list_part: ELIF LPAREN expression RPAREN ignore? statement elif_list_part | ; 

for_statement: FOR ID UNTIL expression BY expression ignore? statement;

break_statement: BREAK ignore;
continue_statement: CONTINUE ignore;

return_statement: RETURN expression? ignore;

call_statement: ID LPAREN explist? RPAREN ignore;

block_statement: BEGIN ignore statement_list END ignore;

list_literal: literal COMMA list_literal | literal;
literal: NUMBER_LIT | STRING_LIT | TRUE | FALSE | array_literal;
array_literal: LBRACKET explist RBRACKET;

funcall: ID LPAREN explist? RPAREN;

explist: expression COMMA explist | expression;
expression: exp1 ELLIPSIS exp1 | exp1;
exp1: exp2 ( EQ | EQ_EQ | NOT_EQ | LT | GT | LTE | GTE ) exp2 | exp2;
exp2: exp2 ( AND | OR ) exp3 | exp3;
exp3: exp3 ( PLUS | MINUS ) exp4 | exp4;
exp4: exp4 ( MUL | DIV | MOD ) exp5 | exp5;
exp5: NOT exp5 | exp6;
exp6: (MINUS | PLUS) exp6 | exp7;
exp7: (ID | ID LPAREN explist? RPAREN) LBRACKET explist RBRACKET | exp8;
exp8: funcall | ID | literal | LPAREN expression RPAREN; 

// kí tự bỏ qua
ignore: NEWLINE+;

// ! --------------------------  Lexical structure ----------------------- //

// TODO Keyword
TRUE: 'true';
FALSE: 'false';
BOOL: 'bool';
STRING:'string';
NUMBER:'number';
RETURN: 'return';
VAR: 'var';
DYNAMIC: 'dynamic';
FUNC: 'func';
FOR: 'for';
UNTIL: 'until';
BY: 'by';
BREAK: 'break';
CONTINUE: 'continue';
IF: 'if';
ELSE: 'else';
ELIF: 'elif';
BEGIN: 'begin';
END: 'end';

// TODO Operations
PLUS: '+';
MINUS: '-';
MUL: '*';
DIV: '/';
MOD: '%';
NOT: 'not';
AND: 'and';
OR: 'or';
EQ: '=';
ASSIGN: '<-';
NOT_EQ: '!=';
LT: '<';
LTE: '<=';
GT: '>';
GTE: '>=';
ELLIPSIS: '...';
EQ_EQ: '==';

// TODO Seperator
LPAREN: '(';
RPAREN: ')';
LBRACE: '{';
RBRACE: '}';
LBRACKET: '[';
RBRACKET: ']';
COMMA: ',';

// TODO Identifier
ID: [_a-zA-Z] [_a-zA-Z0-9]*;

// TODO Number Literal
fragment DECIMAL: ('.' [0-9]*)?;
fragment EXPONENT: ('e' | 'E') ('+' | '-')? [0-9]+;
NUMBER_LIT: [0-9]+ DECIMAL? EXPONENT?;

// TODO Boolean
BOOL_LIT: TRUE | FALSE;

// TODO String
fragment LEGAL_LIT: ESC_LIT | ~[\n\r\f\\"] | ['] ["];
fragment ESC_LIT: '\\' [bfrnt'\\];
STRING_LIT : '"' LEGAL_LIT* '"' {self.text=self.text[1:-1];};

NEWLINE: '\n';
COMMENT: '##' (~[\f\r\n])* -> skip;
WS : [ \f\b\t\r]+ -> skip ; // skip spaces, tabs, newlines

ERROR_CHAR: . {raise ErrorToken(self.text)};
UNCLOSE_STRING: '"' LEGAL_LIT* ( '\r\n' | '\n' | EOF ) {
	if(len(self.text) >= 2 and self.text[-1] == '\n' and self.text[-2] == '\r'):
                raise UncloseString(self.text[1:-2])
	elif(self.text[-1] == '\n'):
		raise UncloseString(self.text[1:-1])
	else:
                raise UncloseString(self.text[1:])
};
ILLEGAL_ESC_LIT: [\r\f\\'] | '\\' ~ ( 'b' | 'f' | 'r' | 'n' | 't' | '\\' ) | '\'' ~["] ;
ILLEGAL_ESCAPE: '"' LEGAL_LIT* ILLEGAL_ESC_LIT {
    raise IllegalEscape(self.text[1:]);        
};
