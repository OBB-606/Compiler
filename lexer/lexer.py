from re import findall

with open ("/home/valery/PycharmProjects/Compiler_PA_6_sem/program") as read_file:
    tmp = read_file.read()

text_program = "".join(tmp.split())
print(text_program)
dict_of_lexems: dict = {}
print('Rock')

int_template = r"[\+=\-:]\d+[\+=\-:;]|[\+=\-:]\d+;"
float_template = r"[\+=\-:]\d+\.\d+[\+=\-:;]|[\+=\-:]\d+\.\d+"
literals_template = r"[\.\+\-,:;=!]"
variables_template = r"\$\w+"
service_words_template = r"integer|var|begin|end\.|end|while|print"
int_flag = findall(r"\d+", "".join(findall(int_template, text_program)))
float_flag = findall(r"\d+\.\d+", "".join(findall(float_template, text_program)))
variables_flag = findall(variables_template, text_program)
service_words_flag = findall(service_words_template, text_program)
literals_flag = findall(literals_template, text_program)

if float_flag:
    dict_of_lexems['float'] = float_flag
if int_flag:
    dict_of_lexems['int'] = int_flag
if literals_flag:
    dict_of_lexems['literals'] = literals_flag
if variables_flag:
    dict_of_lexems['variables'] = variables_flag
if service_words_flag:
    dict_of_lexems['service_words'] = service_words_flag

for i in dict_of_lexems:
    print(f"{i} --> {dict_of_lexems[i]} --> len = {len(dict_of_lexems[i])}")