print("Задание 1")

'''
Задание 1
Создать программный файл в текстовом формате, записать в него построчно данные,
вводимые пользователем. Об окончании ввода данных будет 
свидетельствовать пустая строка.
'''

my_list = []
while True:
    line = input("Введите значения или пустую строку для завершения: ")
    if line == '':
        break
    else:
        newline = line + '\n'
        my_list.append(newline)

with open("task_1.txt", "w", encoding="utf-8") as file_obj:
    file_obj.writelines(my_list)

print("Задание 2")

'''
Задание 2
Создать текстовый файл (не программно),
сохранить в нём несколько строк, 
выполнить подсчёт строк и слов в каждой строке.
'''

with open("task_2.txt", "r", encoding="utf-8") as file_obj:
    content = file_obj.readlines()
    print(content)


def count_lines(arg1):
    lines = 0
    for line in arg1:
        lines += 1
        words = len(line.split())
        print(f"{words} слов в строке {lines}")
    print(f"Количество строк: {lines}")


count_lines(content)

print("Задание 3")

'''
Задание 3
Создать текстовый файл (не программно). Построчно записать фамилии сотрудников
и величину их окладов (не менее 10 строк). Определить, кто из сотрудников 
имеет оклад менее 20 тысяч, вывести фамилии этих сотрудников.
Выполнить подсчёт средней величины дохода сотрудников.
Пример файла:

Иванов 23543.12
Петров 13749.32
'''

with open("task_3.txt", "r", encoding="utf-8") as file_obj:
    all_ = []
    less = []
    my_list = file_obj.read().split('\n')
    for i in my_list:
        el = i.split()
        all_.append(el[1])
        if float(el[1]) < 20000:
            less.append(el[0])
    print(f'Оклад меньше 20 000 {less}, средний оклад '
          f'{sum(map(float, all_)) / len(all_)}')

print("Задание 4")

'''
Задание 4
Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Напишите программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские. Новый блок
строк должен записываться в новый текстовый файл.
'''

dic = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
new_file = []
with open("task_4.txt", "r", encoding="utf-8") as file_obj:
    content = file_obj.readlines()
    for i in content:
        el = i.split(' ', 1)
        new_file.append(dic[el[0]] + '  ' + el[1])
    print(new_file)

with open("task_4_new.txt", "w", encoding="utf-8") as file_obj_2:
    file_obj_2.writelines(new_file)

print("Задание 5")

'''
Задание 5
Создать (программно) текстовый файл, записать в него программно набор чисел,
разделённых пробелами. Программа должна подсчитывать сумму чисел в файле 
и выводить её на экран.
'''


def summary():
    try:
        with open("task_5.txt", "w+", encoding="utf-8") as file_obj:
            line = input("Введите цифры через пробел: ")
            file_obj.write(line)
            file_obj.seek(0)
            content = file_obj.readlines()
            for i in content:
                el = i.split()
            my_i = [float(e) for e in list(el)]
            print(f"Cумма: {sum(my_i)}")
    except IOError:
        print('Ошибка в файле')
    except ValueError:
        print('Неправильно набран номер. Ошибка ввода-вывода')


summary()

print("Задание 6")

'''
Задание 6
Сформировать (не программно) текстовый файл. В нём каждая строка должна 
описывать учебный предмет и наличие лекционных, практических и лабораторных 
занятий по предмету. Сюда должно входить и количество занятий. Необязательно,
чтобы для каждого предмета были все типы занятий.
Сформировать словарь, содержащий название предмета и общее количество занятий
по нему. Вывести его на экран.
Примеры строк файла: Информатика: 100(л) 50(пр) 20(лаб).
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) —
Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
'''

subjects = {}

try:
    with open("task_6.txt", "r", encoding="utf-8") as file_obj:
        lines = file_obj.readlines()

    for line in lines:
        data = line.replace('(', ' ').split()

        subjects[data[0][:-1]] = sum(
            int(i) for i in data if i.isdigit()
        )
except IOError as e:
    print(e)
except ValueError:
    print("Неконсистентные данные")

print(subjects)

print("Задание 7")

'''
Задание 7
Создать вручную и заполнить несколькими строками текстовый файл, в котором 
каждая строка будет содержать данные о фирме: название, форма собственности,
 выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.

Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а 
также среднюю прибыль. Если фирма получила убытки, в расчёт средней прибыли 
её не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями,
 а также словарь со средней прибылью. Если фирма получила убытки, также 
 добавить её в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000},
 {“average_profit”: 2000}].

Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
Подсказка: использовать менеджер контекста.
'''
from json import dumps

results = [{}, {}]

try:
    with open("task_7.txt", "r", encoding="utf-8") as fhs:
        lines = fhs.readlines()
    for line in lines:
        name, _, proceeds, expenses = line.split()
        results[0][name] = int(proceeds) - int(expenses)
    results[1]['average_profit'] = round(
        sum(
            profit for _, profit in results[0].items() if profit > 0
        ) / len(results[0])
    )
    with open("task_7_new.json", "w", encoding="utf-8") as fhd:
        fhd.write(dumps(results))
except IOError as e:
    print(e)
except ValueError:
    print("Неконсистентные данные")
