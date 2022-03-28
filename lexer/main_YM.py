from lexer_YM import Lexer


with open ("/home/valery/PycharmProjects/Compiler_PA_6_sem/program") as read_file:
    text_input = read_file.read()

lexer = Lexer()
lexer.get_lexer()
tokens = lexer.lex(text_input)
for i in lexer.lex(text_input):
    print(i)

