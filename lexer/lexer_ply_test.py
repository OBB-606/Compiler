import re

import ply.lex as lex



tokens = (
    'INT_DIGIT','FLOAT_DIGIT','BEGIN', 'END',
    'PRINT', "OPEN_PAREN","CLOSE_PAREN","SEMI_COLON",
    "SUM","MINUS","VARIABLE","COLON","EQUAL","CYCLE",
    "INTEGER_TYPE","FLOAT_TYPE", "VAR", "COMMA"

)
ident = r"[a-z]\w*"
t_INT_DIGIT = r"[^\.]\d+[^\.]"
t_FLOAT_DIGIT = r"\d+\.\d+"
t_COMMA = r","
t_VAR = r"var"
t_BEGIN = r"begin"
t_END = r"end|end[\.]"
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
r_ignore = '\n\r\t\f'

def t_error(t):
    print(f"Illegal character {t.value[0]}")
    t.lexer.skip(1)


lexer = lex.lex(reflags=re.UNICODE | re.DOTALL)


with open ("/home/mbluuka/Рабочий стол/Compiler/Compiler/program") as read_file:
    tmp = read_file.read()
data = "".join(tmp.split())

lexer.input(data)
lst = []
while True:
    token  = lexer.token()
    if not token:
        break
    lst.append(str(token))
    print(f"{str(token)}")
lst_final = []
for i in lst:
    tmp = i.replace("LexToken(", "")
    tmp_2 = tmp.replace(")", "")
    lst_final.append((tmp_2.replace("'", "")).split(","))

for i in lst_final:
    i.pop(-2)
    print(i)
with open("file_tockens.txt", "w") as write_file:
    for i in lst_final:
        write_file.writelines(f"{i}\n")