from lexer.lexer_ply_test import tokens
import ply.yacc as yacc

class Node:
    def parts_str(self):
        st = [str(part) for part in self.parts]
        return "/n".join(st)

    def __repr__(self):
        return self.type + ":\n\t" + self.parts_str().replace("\n", "\n\t")

    def add_parts(self, parts):
        self.parts += parts
        return self

    def __init__(self, type, parts):
        self.type = type
        self.parts = parts

def p_var(p):
    '''var : VAR variable COLON type SEMI_COLON body'''
    p[0] = Node(p[4], [p[2]])
def p_type(p):
    '''type : INTEGER_TYPE
            | FLOAT_TYPE'''
def p_body(p):
    '''body :
            | body lines colons
            | BEGIN lines colons END'''
    if len(p) > 1:
        if p[1] is None:
            p[0] = Node('body', [])
        p[0] = p[1].add_parts([p[2]])
    else:
        p[0] = Node('body', [])

def p_colons(p):
    '''colons : SEMI_COLON
              | colons SEMI_COLON'''

def p_lines(p):
    '''lines : assign
             | while
             | PRINT args'''

    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = Node('print', [p[2]])

def p_assign(p):
    '''assign : VARIABLE EQUAL expr'''
    p[0] = Node("assign", [p[1], p[3]])

def p_expr(p):
    '''expr : fact
            | expr SUM fact
            | expr MINUS fact'''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = Node(p[2], [p[1], p[3]])

def p_fact(p):
    '''fact : term'''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = Node(p[2], [p[1], p[3]])

def p_term(p):
    '''term : arg
            | OPEN_PAREN expr CLOSE_PAREN'''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = p[2]

def p_while(p):
    '''while : CYCLE OPEN_PAREN args CLOSE_PAREN BEGIN lines END'''
    p[0] = Node('while', [p[1], p[3]])

def p_args(p):
    '''args :
            | expr
            | args COMMA expr'''

    if len(p) == 1:
        p[0] = Node('args', [])
    elif len(p) == 2:
        p[0] = Node('args', [p[1]])
    else:
        p[0] = p[1].add_parts([p[3]])

def p_arg(p):
    '''arg : variable
           | FLOAT_DIGIT
           | INT_DIGIT'''
    p[0] = Node('arg', [p[1]])

def p_variable(p):
    '''variable : VARIABLE
           | VARIABLE COMMA variable
           |'''
    if len(p) == 2:
        p[0] = Node('one_variable', [p[1]])
    elif len(p) == 4:
        p[0] = Node('many_variables', [p[1], p[3]])

def p_error(p):
    print("Unexpected Token: ", p)



parser = yacc.yacc()
def build_tree(code):
    return parser.parse(code)


