from lexer import lexer_ply_test
from parser import parser_new

with open("program_2", "r") as read_file:
    tmp = read_file.read()

data = "".join(tmp.split())
result = parser_new.result(data)
print(result)

