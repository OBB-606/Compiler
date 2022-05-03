grammar kia;

program
    : block
    ;

block
    : vars? function* beginstmt*
    ;

vars
    : VAR (variable (COMMA variable)* COLON (INTEGER_ | FLOAT_) SEMI_COLON)*
    ;

//types
//    : INTEGER
//    | FLOAT
//    ;

function
    : FUNCTION NAME_FUNCTION OPEN_PAREN variable CLOSE_PAREN beginstmt
    ;

statement
    : (assign | call | print | beginstmt | if_ | while_)?
    ;

assign
    : variable EQUAL expression SEMI_COLON
    ;

call
    : CALL NAME_FUNCTION OPEN_PAREN variable (COMMA variable)* CLOSE_PAREN
    ;

print
    : PRINT OPEN_PAREN (variable | literal)* CLOSE_PAREN
    ;

literal
    : STRING;

if_
    : IF OPEN_PAREN condition CLOSE_PAREN beginstmt
    ;

while_
    : WHILE OPEN_PAREN condition CLOSE_PAREN beginstmt
    ;

beginstmt
    : BEGIN statement (SEMI_COLON statement)* END
    ;

condition
    : expression compare_operators expression
    ;

compare_operators
        : NEGATION EQUAL
        | EQUAL EQUAL
        | LESS
        | MORE_
        ;

expression
   : (SUM | MINUS)? term ((SUM | MINUS) term)*
   ;

term
   : factor ((MULTIPLY | DIVISION) factor)*
   ;

factor
   : variable
   | digit
   | OPEN_PAREN expression CLOSE_PAREN
   ;

variable
    : VARIABLE
    ;

digit
    : INT_DIGIT
    | FLOAT_DIGIT
    ;


VAR : 'var';
COMMA : ',';
SEMI_COLON : ';';
MULTIPLY : '*';
DIVISION: '/';
SUM : '+';
MINUS : '-';
NEGATION : '!';
EQUAL : '=';
LESS : '<';
MORE_ : '>';
STRING : [a-zA-Z]+;
END : 'end' | 'END';
BEGIN : 'begin' | 'BEGIN';
WHILE : 'while';
INTEGER_ : 'integer';
FLOAT_ : 'float';
IF : 'if';
CALL : 'call';
COLON : ':';
FUNCTION : 'function';
NAME_FUNCTION : '#'[a-zA-Z]+;
VARIABLE : '$'[a-zA-Z]+([0-9])*;
INT_DIGIT : [0-9]+;
FLOAT_DIGIT : [0-9]+'.'[0-9]+;
OPEN_PAREN : '(';
CLOSE_PAREN : ')';
PRINT : 'print';

WS : [ \t\r\n] -> skip;



