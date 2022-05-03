from lexer.lexer_ply_test import tokens
import ply.yacc as yacc

        
def p_program (p):
    '''program :
                | block colons body'''

def p_block (p):
    '''block :
              | vars'''

def p_vars (p):
    '''vars :
            | VAR vars variables colons types colons'''

def p_types (p):
    '''types :
              | INTEGER_TYPE
              | FLOAT_TYPE'''

def p_colons (p):
    '''colons :
              | COLON
              | SEMI_COLON'''

def p_variables (p):
    '''variables :
                 | VARIABLE
                 | VARIABLE COMMA variables
                 | OPEN_PAREN variables CLOSE_PAREN'''

def p_body (p):
    '''body :
            | BEGIN body lines colons END
            | lines colons'''

def p_lines (p):
    '''lines :
             | function
             | cycle
             | assign
             | expression
             | print
             | if
             | call'''
def p_assign (p):
    '''assign : variables EQUAL expression'''

def p_call (p):
    '''call : CALL NAME_FUNCTION variables'''

def p_function (p):
    '''function :
                | FUNCTION NAME_FUNCTION variables body'''

def p_cycle (p):
    '''cycle :
             | CYCLE condition body'''

def p_if (p):
    '''if : IF condition body else body'''

def p_else (p):
    '''else :
            | ELSE'''

def p_condition (p):
    '''condition : expression comparison expression
                 | OPEN_PAREN condition CLOSE_PAREN logic_op'''

def p_logic_op (p):
    '''logic_op : AND
                | OR
                | NEGATION'''

def p_comparison (p):
    '''comparison : MORE
                | LESS
                | LOGIC_EQUAL'''

def p_print (p):
    '''print : PRINT expression'''

def p_expression (p):
    '''expression :
                  | term SUM term
                  | term MINUS term
                  | CONTINUE
                  | BREAK'''

def p_term (p):
    '''term :
            | factor MULTIPLY factor
            | factor DIVISION factor'''

def p_factor (p):
    '''factor :
              | VARIABLE
              | FLOAT_DIGIT
              | INT_DIGIT
              | OPEN_PAREN expression CLOSE_PAREN'''

def p_error(p):
    print("Unexpected Token: ", p)

parser = yacc.yacc()

def result(code):
    return parser.parse(code)