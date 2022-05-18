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
    '''block : vars_
             | beginstmt'''
def p_vars_(p):
    '''VAR'''
