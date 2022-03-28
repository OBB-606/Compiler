from rply import LexerGenerator
import re

#for linux
with open ("/home/valery/PycharmProjects/Compiler_PA_6_sem/program") as read_file:
    tmp = read_file.read()

#for windows
# with open ("F:\Volery\Compiler_PA_6_sem\program") as read_file:
#     tmp = read_file.read()
# text_input = "".join(tmp.split())

lg = LexerGenerator()

lg.add('PRINT', r'print')
lg.add("OPEN_PAREN", r"\(")
lg.add("CLOSE_PAREN", r"\)")
lg.add("SEMI_COLON", r";")
lg.add("SUM", r"\+")
lg.add("MINUS", r"\-")
lg.add("VARIABLE", r"\$\w+")
lg.add("END", r"end|end\.")
lg.add("BEGIN", r"begin")
lg.add("COLON", r":")
lg.add("EQUAL", r"=")
lg.add("CYCLE", r"while")
lg.add("INTEGER_TYPE", r"integer")
lg.add("FLOAT_TYPE", r"float")
# lg.ignore(r"\s+")

l = lg.build()

for i in l.lex(text_input):
    print(i)


