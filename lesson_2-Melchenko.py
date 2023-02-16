print("Задание 1")



'''
Задание 1
Создать список и заполнить его элементами 
различных типов данных. 
Реализовать скрипт проверки типа данных каждого элемента.
Использовать функцию type() для проверки типа. 
Элементы списка можно не запрашивать у пользователя, 
а указать явно, в программе.
'''

test_list = [45, "text", 14.5, [1.2, 2], False, None, ('о', ' ', 'ы'),
                  {'a', 'k', 'b', 'd', 'r'}, {'key_1': 1, 'key_2': 2}]
print(test_list)

for el in test_list:
    print(f"Элемент: {el} Тип: {type(el)}")

print("Задание 2")

'''
Задание 2
Для списка реализовать обмен значений соседних элементов. 
Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т. д. 
При нечётном количестве элементов последний сохранить на своём месте. 
Для заполнения списка элементов нужно использовать функцию input()
'''

el_count = int(input("Введите число элементов списка: "))
test_list = []
i = 0

while i < el_count:
    test_list.append(input("Введите элемент списка: "))
    i = i + 1
#    print(test_list)
#    print(len(test_list))
#    print(len(test_list)//2)

el = 0
for el1 in range((len(test_list)//2)):
        test_list[el], test_list[el + 1] = test_list[el + 1], test_list[el]
        el = el + 2
print(test_list)

print("Задание 3")

'''
Задание 3
Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна,
лето, осень).
Напишите решения через list и через dict.
'''

seas_list = ['зима', 'весна', 'лето', 'осень']
seas_dict = {1: 'зима', 2: 'зима', 3: 'весна', 4: 'весна', 5: 'весна',
             6: 'лето', 7: 'лето', 8: 'лето', 9: 'осень',
             10: 'осень', 11: 'осень', 12: 'зима'}
month = int(input("Введите номер месяца: "))
print(seas_dict.get(month))

if month in [1, 2, 12]:
    print(seas_list[0])
elif month in [3, 4, 5]:
    print(seas_list[1])
elif month in [6, 7, 8]:
    print(seas_list[2])
elif month in [9, 10, 11]:
    print(seas_list[3])
else:
    print("Введен некоректный номер месяца")

print("Задание 4")

'''
Задание 4
Пользователь вводит строку из нескольких слов, разделённых
пробелами. Вывести каждое слово с новой строки.
Строки необходимо пронумеровать. Если слово длинное,
выводить только первые 10 букв в слове.
'''

my_str = input("Введите строку из нескольких слов, разделённых пробелами: ")
my_str_list = my_str.split()
#    print(my_str_list)
for ind, el in enumerate(my_str_list, 1):
    print(ind, el[:10])


print("Задание 5")

'''
Задание 5
Реализовать структуру «Рейтинг», представляющую собой
не возрастающий набор натуральных чисел.
У пользователя необходимо запрашивать новый элемент рейтинга.
Если в рейтинге существуют элементы с одинаковыми значениями,
то новый элемент с тем же значением должен разместиться
после них.
Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
Набор натуральных чисел можно задать непосредственно в коде, 
например, my_list = [7, 5, 3, 3, 2].
'''
my_list = [7, 5, 3, 3, 2]
number = int(input("Введите целое число: "))
for el in range(len(my_list)):
    if my_list[el] == number:
        my_list.insert(el + 1, number)
        break
    elif my_list[0] < number:
        my_list.insert(0, number)
    elif my_list[-1] > number:
        my_list.append(number)
    elif my_list[el] > number and my_list[el + 1] < number:
        my_list.insert(el + 1, number)
print(f"Cписок - {my_list}")

