"""
поток токенов в таком же порядке в каком их value встречается в исходном тексте программы
"""

from re import findall

#for linux
with open ("/home/valery/PycharmProjects/Compiler_PA_6_sem/program") as read_file:
    tmp = read_file.read()

#for windows
# with open ("F:\Volery\Compiler_PA_6_sem\program") as read_file:
#     tmp = read_file.read()



text_program = "".join(tmp.split())
print(text_program)
dict_of_tokens: dict = {}
int_template = r"[\+=\-:]\d+[\+=\-:;]|[\+=\-:]\d+;"
float_template = r"[\+=\-:]\d+\.\d+[\+=\-:;]|[\+=\-:]\d+\.\d+"
literals_template = r"[\(\)\.\+\-,:;=!]"
variables_template = r"\$\w+"
service_words_template = r"integer|var|begin|end\.|end|while|print|float"


int_flag = findall(r"\d+", "".join(findall(int_template, text_program)))
float_flag = findall(r"\d+\.\d+", "".join(findall(float_template, text_program)))
variables_flag = findall(variables_template, text_program)
service_words_flag = findall(service_words_template, text_program)
literals_flag = findall(literals_template, text_program)


semicolon_flag = findall(r";", "".join(literals_flag))
comma_flag = findall(r",", "".join(literals_flag))
equals_flag = findall(r"=", "".join(literals_flag))
minus_flag = findall(r"\-", "".join(literals_flag))
plus_flag = findall(r"\+", "".join(literals_flag))
multiplication_flag = findall(r"\*", "".join(literals_flag))
negation_flag = findall(r"!", "".join(literals_flag))
open_paren_flag = findall(r"\(", "".join(literals_flag))
close_paren_flag = findall(r"\)", "".join(literals_flag))
colon_flag = findall(r":", "".join(literals_flag))


integer_word_flag = findall(r"integer", "".join(service_words_flag))
begin_flag = findall(r"begin", "".join(service_words_flag))
end_flag = findall(r"end", "".join(service_words_flag))
cycle_flag = findall(r"while", "".join(service_words_flag))
print_flag = findall(r"print", "".join(service_words_flag))
float_word_flag = findall(r"float", "".join(service_words_flag))
declare_variables_flag = findall(r"var", "".join(service_words_flag))

if colon_flag:
    dict_of_tokens['colon'] = colon_flag
if float_flag:
    dict_of_tokens['float'] = float_flag
if int_flag:
    dict_of_tokens['int'] = int_flag
if semicolon_flag:
    dict_of_tokens['semicolon'] = semicolon_flag
if comma_flag:
    dict_of_tokens['comma'] = comma_flag
if equals_flag:
    dict_of_tokens['equals'] = equals_flag
if minus_flag:
    dict_of_tokens['minus'] = minus_flag
if plus_flag:
    dict_of_tokens['plus'] = plus_flag
if multiplication_flag:
    dict_of_tokens['multiplication'] = multiplication_flag
if negation_flag:
    dict_of_tokens['negation'] = negation_flag
if open_paren_flag:
    dict_of_tokens['open_paren'] = open_paren_flag
if close_paren_flag:
    dict_of_tokens['close_paren'] = open_paren_flag
if integer_word_flag:
    dict_of_tokens['integer_word'] = integer_word_flag
if begin_flag:
    dict_of_tokens['begin'] = begin_flag
if end_flag:
    dict_of_tokens['end'] = end_flag
if cycle_flag:
    dict_of_tokens['cycle'] = cycle_flag
if print_flag:
    dict_of_tokens['print'] = print_flag
if float_word_flag:
    dict_of_tokens['float_word'] = float_word_flag
if declare_variables_flag:
    dict_of_tokens['declare_variables'] = declare_variables_flag
if variables_flag:
    dict_of_tokens['variables'] = variables_flag

summ = []
for i in dict_of_tokens:
    summ.append(len("".join(dict_of_tokens[i])))
    print(f"{i} --> {dict_of_tokens[i]} --> len = {len(dict_of_tokens[i])}")

# print(f"len_program = {len(text_program)}, len_dict_tokens = {sum(summ)}")
# with open("table_of_symbols.json", "w") as json_file_write:
#     json.dump(dict_of_tokens, json_file_write, indent=2)

with open("file.txt", "w") as write_file:
    write_file.write("")
counter = 0
for i in dict_of_tokens:
    for j in dict_of_tokens[i]:
        with open("file.txt", "a") as write_file:
            write_file.write(f"{counter}, {i}, {j}\n")
            counter += 1

