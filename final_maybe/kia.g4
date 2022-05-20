grammar kia;

program
    : block
    ;

block
    : vars_? beginstmt
    ;

vars_
    : VAR (variable (COMMA variable)* COLON types SEMI_COLON)*
    ;

types
    : FLOAT
    | INTEGER
    ;

function
    : FUNCTION NAME_FUNCTION OPEN_PAREN variable CLOSE_PAREN beginstmt
    ;

statement
    : (assign | vars_ | call | print_ | beginstmt | if_ | while_ | break_cont | function)*
    ;

assign
    : variable EQUAL expression
    ;

call
    : CALL NAME_FUNCTION OPEN_PAREN factor (COMMA factor)* CLOSE_PAREN
    ;

print_
    : PRINT OPEN_PAREN (variable | literal)* CLOSE_PAREN
    ;

literal
    : STRING;

beginstmt
    : BEGIN statement (SEMI_COLON statement)* END
    ;

if_
    : IF OPEN_PAREN condition CLOSE_PAREN beginstmt
    ;

while_
    : CYCLE OPEN_PAREN condition CLOSE_PAREN beginstmt
    ;

break_cont
    : BREAK
    | CONTINUE
    ;

condition
    : (OPEN_PAREN* expression CLOSE_PAREN* compare_operators OPEN_PAREN* expression CLOSE_PAREN*)*
    ;


and_or
    : AND
    | OR
    ;

compare_operators
        : NEGEQ
        | EQUAL EQUAL
        | LESS
        | MORE_
        | LESS_EQUAL
        | MORE_EQUAL
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

MORE_EQUAL : '>=';
LESS_EQUAL : '<=';
AND : 'and';
OR : 'or';
NEGEQ : '!=';
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
STRING : '"'[a-zA-Z]+'"';
END : 'end' | 'END';
BEGIN : 'begin' | 'BEGIN';
CYCLE : 'while';
INTEGER : 'integer';
FLOAT : 'float';
IF : 'if';
CALL : 'call';
COLON : ':';
FUNCTION : 'function';
NAME_FUNCTION : '#'[a-zA-Z]+;
VARIABLE : '$'[a-zA-Z]+[0-9]*;
INT_DIGIT : [0-9]+;
FLOAT_DIGIT : [0-9]+'.'[0-9]+;
OPEN_PAREN : '(';
CLOSE_PAREN : ')';
PRINT : 'print';
BREAK : 'break';
CONTINUE : 'continue';
WS : [ \t\r\n] -> skip;



