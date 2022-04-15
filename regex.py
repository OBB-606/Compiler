"""
var$a,$b,$c:integer;$d:float;begin$a=28;$b=$a+45;$c=$b-14;$d=11.1345;while($a!=0.1)begin$a=$a-1;print($a)endend


\d - числа ~ [0-9]
\D - не числа ~ [^0-9]
\w - буквы, числа.
\W - не буквы и числа
\s - пустые символы ~ [\f\n\r\t\v]
\S - непустые символы

Специальные символы:

[] - перечисление символов
{} - диапазон символов
() - область действия
\ - специальные символы в виде обычных (экранирование) 
| - или
^ - начало текста или исключения (в перечислениях символов)
$ - конец текста
. - любой символ
? - символ встречается 0 или 1 раз
* - символ встречается 0 или более раз
+ - символ встречается 1 или более раз
"""

from re import findall, template
from typing import Text

template = r"\w{1,12}@\w{1,10}\.\w{1,3}"
text = input("write email: ")
flag = findall(template, text)
if flag:
    print("is valid")
else:
    print("not valid")

'''var : VAR variable COLON INTEGER_TYPE SEMICOLON body
           | VAR variable COLON FLOAT_TYPE SEMICOLON body
    body :
            | body lines colons
            | BEGIN lines colons END
    colons : SEMI_COLON
              | colons SEMI_COLON
    lines : assign
             | while
             | PRINT args
    assign : VARIABLE EQUAL expr
    expr : fact
            | expr SUM fact
            | expr MINUS fact
    fact : term
    term : arg
            | OPEN_PAREN expr CLOSE_PAREN
    while : CYCLE OPEN_PAREN args CLOSE_PAREN BEGIN lines END
    args :
            | expr
            | args COMMA expr
    arg : variable
           | FLOAT_DIGIT
           | INT_DIGIT
    variable : VARIABLE
           | VARIABLE COMMA variable
           |'''