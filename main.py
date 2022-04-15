from lexer import lexer_ply_test
from parser import parser

with open("program", "r") as read_file:
    tmp = read_file.read()

data = "".join(tmp.split())
result = parser.build_tree(data)
print(result)

