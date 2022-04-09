# @TOKEN(float_first)
# def t_FLOAT_DIGIT(t):
#     tmp = findall(r"\d+\.\d+", str(t.value))
#     if tmp:
#         t.value = str(tmp[0])
#         t.type = "FLOAT_DIGIT"
#     return t

from re import findall
import re
import ply.lex as lex
from ply.lex import TOKEN
from prettytable import PrettyTable
table_tokens = PrettyTable()
table_tokens.field_names = ["ID Token", "Type token", "Value token", "Position token"]

tokens = (
    'INT_DIGIT','FLOAT_DIGIT','BEGIN', 'END',
    'PRINT', "OPEN_PAREN","CLOSE_PAREN","SEMI_COLON",
    "SUM","MINUS","VARIABLE","COLON","EQUAL","CYCLE",
    "INTEGER_TYPE","FLOAT_TYPE", "VAR", "COMMA", "POINT",
    "NEGATION"
)
# int_first = r"[=\+\-\*]\d+[=\+\-;\)\*]"
# float_first = r"[=\+\-\*\(]\d+\.\d+[=\+\-\*;\)]"
t_INT_DIGIT = r"\d+"
t_FLOAT_DIGIT = r"\d+\.\d+"
ident = r"[a-z]\w*"
t_NEGATION = r"\!"
t_POINT = r"\."
t_COMMA = r","
t_VAR = r"var"
t_BEGIN = r"begin"
t_END = r"end"
t_PRINT = r'print'
t_OPEN_PAREN = r"\("
t_CLOSE_PAREN = r"\)"
t_SEMI_COLON = r";"
t_COLON = r":"
t_SUM = r"\+"
t_MINUS = r"\-"
t_VARIABLE = r"\$\w+"
t_EQUAL = r"="
t_CYCLE = r"while"
t_INTEGER_TYPE = r"integer"
t_FLOAT_TYPE = r"float"
# r_ignore = '\n\r\t\f'

def t_error(t):
    print(f"Illegal character {t.value[0]}")
    t.lexer.skip(1)

lexer = lex.lex(reflags=re.UNICODE | re.DOTALL)

with open ("/media/valery/F/Volery/Compiler_PA_6_sem/program") as read_file:
    tmp = read_file.read()
data = "".join(tmp.split())
print(data)
lst_final = []
lexer.input(data)
counter = 0
while True:
    token  = lexer.token()
    if not token:
        break
    counter += 1
    # print(f"{counter}, {str(token)}")
    table_tokens.add_row([str(counter), str(token.type), str(token.value), str(token.lexpos)])
    lst_final.append(token.type)
    lst_final.append(token.value)
    lst_final.append(token.lexpos)
print(table_tokens)
with open("file_tockens.txt", "w") as write_file:
    # write_file.write(f"Type_token, value_token, position_token, id_token\n")
    # for i in range(0, len(lst_final)-2, 3):
    #     write_file.write(f"{lst_final[i]}\t\t{lst_final[i+1]}\t\t{lst_final[i+2]}\n")
    for i in table_tokens:
        write_file.writelines(f"{i}")

