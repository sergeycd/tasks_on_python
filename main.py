import calendar
#Это простые задачки на python, для моего pet-проекта

#Задачка №1

#В доме есть пять свободных квартир с номерами от 1 до 5. Нужно
# заселить их жильцами.Списки упорядочены по номерам квартир жильцов.

#Создай словарь, где ключ — номер квартиры, а значение — списки с
# именами жильцов. Каждая пара жильцов — это отдельный список.

new_neighbours = [['Вася', 'Катя'], ['Юра', 'Марина'], ['Лёша', 'Ира'], ['Петя', 'Надя'], ['Ваня', 'Света']]

house_dict = {}
number_of_flat = 0
for i in new_neighbours:
    number_of_flat+=1
    house_dict[number_of_flat] = i
print(house_dict)

#второй вариант решения
new_neighbours = [['Вася', 'Катя'], ['Юра', 'Марина'], ['Лёша', 'Ира'], ['Петя', 'Надя'], ['Ваня', 'Света']]

house_dict = {}

for i in range(1,6):
# твой код
   house_dict[i] = new_neighbours[i-1]
print(house_dict)

#Задание 2

#Есть много мнемонических правил, чтобы запомнить цвета радуги. Одно из них звучит так: каждый охотник желает знать где сидит фазан. Первая буква в каждом слове обозначает один из цветов радуги:
#к — красный;
#о — оранжевый;
#ж — жёлтый;
#з — зелёный;
#г — голубой;
#с — синий;
#ф — фиолетовый.
#Есть два списка./#Список со словами из мнемонической фразы. Слова идут по порядку: первая буква в слове соответствует цвету радуги в порядке, который записан выше. python
# mnemo = ['каждый', 'охотник', 'желает', 'знать', 'где', 'сидит', 'фазан']

#Список с цветами радуги. Цвета записаны не порядку, перемешаны.
#colors = ['оранжевый', 'голубой', 'фиолетовый', 'красный', 'желтый', 'синий', 'зеленый']
#Твоя задача — наполнить словарь rainbow_dict парами ключ-значение. Ключ — слово из списка mnemo, а значение — соответствующий слову цвет из списка colors.
#Выведи словарь. Должно получиться так:
#{'каждый': 'красный', 'охотник': 'оранжевый', 'желает': 'желтый', 'знать': 'зеленый', 'где': 'голубой', 'сидит': 'синий', 'фазан': 'фиолетовый'}

mnemo = ['каждый', 'охотник', 'желает', 'знать', 'где', 'сидит', 'фазан']

colors = ['оранжевый', 'голубой', 'фиолетовый', 'красный', 'желтый', 'синий', 'зеленый']
rainbow_dict = {}

for i in mnemo:
    for b in colors:
        if i[0] == b[0]:
            rainbow_dict[i] = b
            continue
print(rainbow_dict)

#Задание3
#Словарь movies состоит из пар Название фильма и его Оценка.
#movies = {'Игры разума': 8.3, 'Зеленая миля': 9.1, 'Леон': 8.5, 'Эффект бабочки': 8.2, 'Матрица': 8.6, 'Криминальное чтиво': 8.7}
#Твоя задача — отфильтровать фильмы по оценке. Оставь только те, у которых она больше или равна 8.5. Отфильтрованные пары запиши в новый словарь filtered_movies и выведи его на экран.

movies = {'Игры разума': 8.3, 'Зеленая миля': 9.1, 'Леон': 8.5, 'Эффект бабочки': 8.2, 'Матрица': 8.6, 'Криминальное чтиво': 8.7}
filtered_movies = {}
for key ,value in movies.items():
    if value >= 8.5:
        filtered_movies[key] = value
print(filtered_movies)


# Задание 4
# Строка содержит пять временных значений. Они записаны через запятую:
#
# '1h 45m,360s,25m,30m 120s,2h 60s'.
#
# Напиши цикл, который посчитает общее количество минут.
#
# Результат сохрани в переменную и выведи на экран.
#
# Используй в решении методы split(), replace() и оператор in.
#
# Обрати внимание: временное значение может состоять из одного, двух
# или трёх единиц времени.
#
# Значения расшифровываются так:
#
# часы — любое положительное целое число и символ h;
# минуты — любое положительное целое число и символ m;
# секунды — положительное целое число кратное 60 и символ s.


# cтрока для разделения
times_string = '1h 45m,360s,25m,30m 120s,2h 60s'
# заменяем пробелы на запятую для того что бы потом применить сплит
times_string_replace = times_string.replace(' ',',')
# c помощью сплит создаем список с временными значениями
times_string_split = times_string_replace.split(',')
print(times_string_split)
# цикл который переводит эти значения в числа и считает сумму минут
sum_of_minutes = 0
for i in times_string_split:
    if 'h' in i:
        sum_of_minutes += int(i.replace('h',''))*60
    elif 's' in i:
        sum_of_minutes += int(i.replace('s',''))/60
    else:
        sum_of_minutes += int(i.replace('m', ''))

print(int(sum_of_minutes))


# Задание 5
# Исправь класс Tester так, чтобы:
# при вызове метода work_hard у экземпляра класса tester_1 печаталось
# 'tester_1 Можно отдыхать';
# при вызове метода work_hard у экземпляра класса tester_2 печаталось
# 'tester_2 Что ж, ещё часок поработаю!'.
# Вызовы менять не нужно.

# изначальный шаблон:
# class Tester:
#
#     def __init__(name):
#         name = name
#         deadline = True
#
#     def work_hard(self, deadline=True):
#         if self.deadline:
#             print(self.name, 'Что ж, ещё часок поработаю!')
#         else:
#             print(self.name, 'Можно отдыхать')
#
# tester_1 = Tester(name='tester_1')
# tester_1.work_hard(deadline=False)  # 'tester_1 Можно отдыхать'
# tester_2 = Tester(name='tester_2')
# tester_2.work_hard(deadline=True)   # 'tester_2 Что ж, ещё часок поработаю!'

# готовый вариант:
class Tester():

    def __init__(self, name):
        self.name = name

    def work_hard(self, deadline):
        self.deadline = deadline
        if self.deadline:
            print(self.name, 'Что ж, ещё часок поработаю!')
        else:
            print(self.name, 'Можно отдыхать')

tester_1 = Tester('tester_1')
tester_1.work_hard(deadline=False)  # 'tester_1 Можно отдыхать'
tester_2 = Tester('tester_2')
tester_2.work_hard(deadline=True)   # 'tester_2 Что ж, ещё часок поработаю!'


# Задание 6
# Над каждым файлом можно производить операции:
# запись — W
# чтение — R
# запуск — X
# Напиши функцию, которая обрабатывает действия с файлами.
# В словаре files ключ — это имя файла, а значение — список из операций, которые доступны для этого файла:
# files = {
#     'cool_movie.avi': ['X'],
#     'math_summary.docx': ['R', 'W'],
#     'war_and_peace.txt': ['R', 'W', 'X']
# }
# Обрати внимание: ключи 'cool_movie.avi', 'math_summary.docx' и 'war_and_peace.txt' даны для примера. Словарь files
# может содержать и другие файлы. Названия файлов могут быть случайными, но они всегда соответствуют записи '<имя_файла>.<формат>'.
# К каждому из файлов идут запросы в произвольном порядке. Запрос выглядит так: '<действие> <название файла>'.
# Например: 'write cool_movie.avi' или 'read war_and_peace.txt'.
# Например:
# 'write cool_movie.avi' выведет Access denied,
# 'execute cool_movie.avi' выведет ОК.
# Функция принимает на вход один запрос в виде строки — например, 'write cool_movie.avi' — и возвращает OK или Access denied.
# Вызывать функцию необязательно.

files = {
    'cool_movie.avi': ['X'],
    'math_summary.docx': ['R', 'W'],
    'war_and_peace.txt': ['R', 'W', 'X']
}


def check_files_action(string):
    # разделил строку на список
    split_string = string.split(' ')
    # вытащил значение из списка по ключу
    value_key = files[split_string[1]]
    # проверил доступ
    if split_string[0] == 'write' and 'W' in value_key:
        print('OK')
    elif split_string[0] == 'execute' and 'X' in value_key:
        print('OK')
    elif split_string[0] == 'read' and 'R' in value_key:
        print('OK')
    else:
        print('Access denied')

check_files_action('execute cool_movie.avi')

# Задание 7
# Есть два пустых списка: word_list и marks_list. Напиши функцию, которая принимает на вход строку и наполняет списки:
# word_list — словами из строки;
# marks_list — знаками препинания из строки.
# Строка всегда состоит из слов и знаков препинания ,, !, ., ?. Слова разделяются одиночным пробелом.
# Подряд идёт только один знак препинания.
# Каждое предложение начинается с заглавной буквы и заканчивается знаком препинания.
# Например, в функцию передали строку с цитатой из сериала Breaking Bad
# 'Мне не грозит опасность, Скайлер, я сам опасность! Кто-то откроет дверь и схватит пулю. Думаешь, им буду я? Нет. Это я' \
# ' постучу в дверь.'.
# Результат будет таким:
# word_list = ['Мне', 'не', 'грозит', 'опасность', 'Скайлер', 'я', 'сам', 'Кто-то', 'откроет', 'дверь', 'и', 'схватит',
#              'пулю', 'Думаешь', 'им', 'буду', 'Нет', 'Это', 'постучу', 'в']
# marks_list = [',', '!', '.', '?']
# Ты можешь тестировать функцию на любой другой строке. Но убедись, что она соответствует условиям.
# Требования к результату обработки:
# Значения в списках идут по порядку и не повторяются.
# Если в строке несколько одинаковых значений, функция добавляет в список только первое вхождение.
# Регистр символов важен. Одинаковые слова, которые начинаются с маленькой и заглавной букв, — это разные слова.
# Например, «Мне» и «мне».
# В решении используй метод split(). Импортировать и применять дополнительные библиотеки и функции не нужно.
# Задача решается без регулярных выражений.

word_list =[]
marks_list = []
def prepair_string(string):

    # разделили строку по пробелал и создали лист
    list_of_string = string.split(' ')
    # print(list_of_string)
    # создали список знаков припенаний
    punctuation_mark=['!', ',', '.', '?']
    global word_list
    global marks_list
    # вытаскиваем знак припенания из списка
    for word in list_of_string:
        if word[-1] == punctuation_mark[0] or word[-1] == punctuation_mark[1] or word[-1] == punctuation_mark[2] or word[-1] == punctuation_mark[3]:
            if word[:-1] not in word_list:
                word_list.append(word[:-1])
            if word[-1] not in marks_list:
                marks_list.append(word[-1])
        elif word not in word_list:
            word_list.append(word)


    print(word_list)
    print(marks_list)


prepair_string('Мне не грозит опасность, Скайлер, я сам опасность! Кто-то откроет дверь и схватит пулю. Думаешь, им буду я? Нет. Это я постучу в дверь.')
print(len(word_list))

# Задание 8
# Реализуй класс TestCase, в котором будут:
# Конструктор, внутри которого устанавливаются атрибуты:
# id тест-кейса — рандомное трёхзначное число;
# name название тест-кейса — передаётся при создании объекта TestCase;
# steps — словарь, куда будут добавляться шаги тест-кейса;
# result — ожидаемый результат тест-кейса.
# Метод set_step — добавляет в словарь steps шаг тест-кейса. Принимает два параметра:
# step_number и step_text. Ключ — это step_number (номер шага), а значение — step_text (текстовое описание шага).
# Метод delete_step — удаляет шаг из steps по переданному в метод ключу step_number.
# Метод get_steps — возвращает текущий список шагов.
# Метод set_result — устанавливает ожидаемый результат в атрибут result по переданному параметру result.
# Метод get_test_case — печатает текущее состояние тест-кейса.
import random as r

class TestCase():

    # создал конструктор класса
    def __init__(self, name):
        self.name = name
        self.id = r.randint(100, 999)
        self.steps = {}
        self.result = {}
    #     создаем тест план
    def set_step(self, step_number, step_text):
        self.step_num = step_number
        self.text = step_text
        self.steps[self.step_num] = self.text
        print(first_test_case.__dict__)
    # удаляем шаги из тестплана
    def delete_step(self, step_num):
        self.steps.pop(step_num, "Такого шага в этом тест-кейсе нет!")
        print(first_test_case.__dict__)

    def get_steps(self):
        actuali_steps = list(self.steps.values())
        print(actuali_steps)

    def set_result(self, result):
        self.result_case = result
        self.result.update({'Ожидаемый результат':self.result_case})
        print(first_test_case.__dict__)

    def get_test_case(self):
        dfg = {
            'id': self.id,
            'Название': self.name,
            'Шаги': self.steps
        }
        dfg.update(self.result)
        print(dfg)









first_test_case = TestCase('мой первый тест кейс')
print(first_test_case.__dict__)
first_test_case.set_step('1', 'открыть сайт')
first_test_case.set_step('2', 'закрыть сайт')
first_test_case.set_step('3', 'пойти спать')
first_test_case.delete_step('3')
first_test_case.get_steps()
first_test_case.set_result('Сайт закроется!')
first_test_case.get_test_case()



# Простейшие арифметические операции:
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

# Високосный год
#
# Написать функцию is_year_leap , принимающую 1 аргумент — год, и возвращающую True, если год високосный, и False иначе.


# первый способ
def is_year_leap(year):
    if '.0' in str(year/4):
        return True
    else:
        return False

print(is_year_leap(2020))

# второй способ с использованием модуля calendar
def is_year_leap_second_v(year):
    if calendar.isleap(year):
        return True
    else:
        return False
print(is_year_leap_second_v(2023))
