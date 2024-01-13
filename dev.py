
# Простейшие арифметические операции (1)
#
# Написать функцию arithmetic , принимающую 3 аргумента: первые 2 - числа, третий - операция, которая должна  быть
# произведена над ними. Если третий аргумент + , сложить их; если — , то вычесть; * — умножить; / — разделить  (первое
# на второе). В остальных случаях вернуть строку "Неизвестная операция ".
#

def arithmetic(first_int, second_int, operator):
    if operator == '+':
        return first_int+second_int
    elif operator == '-':
        return first_int - second_int
    elif operator == '*':
        return first_int * second_int
    elif operator == '/':
        return first_int / second_int
    else:
        return "Неизвестная операция "






