from lexer import tokens
import ply.yacc as yacc

class Node:
    def parts_str(self):
        st = []
        for part in self.parts:
            st.append(str(part))
        return "\n".join(st)

    def __repr__(self):
        return self.type + ":\n\t" + self.parts_str().replace("\n", "\n\t")

    def add_parts(self, parts):
        self.parts += parts
        return self

    def __init__(self, type, parts):
        self.type = type
        self.parts = parts

    scope = 'global'

def p_program(p):
    '''program : block'''

def p_block(p):
    '''block : vars_ beginstmt'''
def p_vars_(p):
    '''vars_ : VAR variables COLON types SEMI_COLON
             | '''

def p_variables(p):
    '''variables : VARIABLE COMMA VARIABLE
                 | VARIABLE '''

def p_types(p):
    '''types : INTEGER_TYPE
             | FLOAT_TYPE'''

def p_statement(p):
    '''statement : assign
                 | call
                 | print_
                 | if_
                 | while_
                 | break_cont
                 | function
                 '''

def p_assign(p):
    '''assign : VARIABLE EQUAL expression'''

def p_call(p):
    '''call : CALL NAME_FUNCTION OPEN_PAREN variables CLOSE_PAREN'''

def p_print_(p):
    '''print_ : PRINT_ OPEN_PAREN args_print CLOSE_PAREN'''

def p_args_print(p):
    '''args_print : variables'''

def p_function(p):
    '''function : FUNCTION NAME_FUNCTION OPEN_PAREN variables CLOSE_PAREN beginstmt'''

# def p_literal(p):
#     '''literal : STRING'''

def p_beginstmt(p):
    '''beginstmt : BEGIN statement SEMI_COLON END
                 | beginstmt BEGIN statement SEMI_COLON END'''

def p_if_(p):
    '''if_ : IF OPEN_PAREN condition CLOSE_PAREN beginstmt
           | IF OPEN_PAREN condition CLOSE_PAREN beginstmt ELSE beginstmt'''

def p_while_(p):
    '''while_ : WHILE_ OPEN_PAREN condition CLOSE_PAREN beginstmt'''

def p_break_cont(p):
    '''break_cont : BREAK
                  | CONTINUE'''

def p_condition(p):
    '''condition : expression compare_operators expression
                 | OPEN_PAREN expression CLOSE_PAREN compare_operators OPEN_PAREN expression CLOSE_PAREN'''

def p_and_or(p):
    '''and_or : AND
              | OR'''

def p_compare_operators(p):
    '''compare_operators : NEGEQ
                         | LOGIC_EQUAL
                         | LESS
                         | MORE_
                         | LESS_EQUAL
                         | MORE_EQUAL
                         '''

def p_expression(p):
    '''expression : term SUM term
                  | term MINUS term
                  |'''

def p_term(p):
    '''term : factor
            | factor MULTIPLY factor
            | factor DIVISION factor'''

def p_factor(p):
    '''factor : VARIABLE
              | digit
              | OPEN_PAREN expression CLOSE_PAREN'''

def p_digit(p):
    '''digit : INT_DIGIT
             | FLOAT_DIGIT'''

def p_error(p):
    print("Unexpected Token: ", p)

parser = yacc.yacc()

def result(code):
    return parser.parse(code)
