# 1)Дан лист:
#   list = [22, 3,5,2,8,2,-23, 8,23,5]
# - 1 найти min число в листе
# - 2 удалить все одинаковые значения
# - 3 заменить каждое четвертое значение на "Х"
#  - 4 вывести элемент листа, значение которого ближе всего к среднему арифметическому всех элементов этого же листа
# пример:
# [1, 2, 3, 4, 5, 6, 7, 8, 9] => 5
# [-1, -2, 3, 4, 555] => 4
# [5, 5, 5, 5] => 5
# [-10, 5, 5] => 5
# 2)вывести на экран пустой квадрат из "*" сторона которого указана в переменой:
# 3) переделать первое задание под меню с помощью цикла
# 4) вывести табличку умножения с помощью цикла while

# Забыл
# вам
# показать
# отрицание:
# в
# js
# у
# вас
# было:
# !true -> false
# в
# python:
# not True -> False
#
# так
# же
# вместо | | тут
# используется
# слово or, и
# вместо & & слово and

# реализовать записную книжку покупок:
# - каждая запись должна содержать название покупки и ее цену
# -сделать менюшку для работы с записной книжкой:
#     '1) Создать запись'
#     '2) Список все записей'
#     '3) Общая сумма всех покупок'
#     '4) Самая дорогая покупка'
#     '5) Поиск по названию покупки'
#     '9) Выход'
# - можете придумать свои пункты
# =======================================================================================================================


# 1.1 найти min число в листе
# list1 = [22, 3, 5, 2, 8, 2, -23, 8, 23, 5]
# варіант 1
# minInteger = list1[0]
# for i in list1:
#     if i < minInteger:
#         minInteger = i
#
# print(minInteger)

# варіант 2
# print(min(list1))
# =======================================================================================================================


# 1.2 удалить все одинаковые значения
# list1 = [22, 3, 5, 2, 8, 2, -23, 8, 23, 5]

# варіант видалення пар однакових чисел
# i = 0
# while i < len(list1):
#     current = list1[i]
#     if list1.count(current) > 1:
#         while list1.count(current) > 0:
#             list1.remove(current)
#     else:
#         i += 1
# print(list1)

# варіант видалення лише дублікатів
# list1 = [22, 3, 5, 2, 8, 2, -23, 8, 23, 5]
# i = 0
# while i < len(list1):
#     current = list1[i]
#     if list1.count(current) > 1:
#         while list1.count(current) > 1:
#             list1.remove(current)
#     else:
#         i += 1
# print(list1)

# =======================================================================================================================

# # 1.3 заменить каждое четвертое значение на "Х"
# list1 = [22, 3, 5, 2, 8, 2, -23, 8, 23, 5]
#
# for i in list1[::4]:
#     list1[list1.index(i)] = 'x'
#
# print(list1)

# TODO
# list1 = [22, 3, 5, 2, 8, 2, -23, 8, 23, 5]
# step = 4
# for i, e in enumerate(list1[3::step], 1):
#     list1[i * step - 1] = 'x'
#
# print(list1)

# 1.4 вывести элемент листа, значение которого ближе всего к среднему арифметическому всех элементов этого же листа
# пример:
# [1, 2, 3, 4, 5, 6, 7, 8, 9] => 5
# [-1, -2, 3, 4, 555] => 4
# [5, 5, 5, 5] => 5
# [-10, 5, 5] => 5

# list2 = [-1, -2, 3, 4, 555]
# sum_list2 = 0
#
# for i in list2:
#     sum_list2 += i
#
# avg = round(sum_list2 / len(list2))
# closest_element = None
# minimal_difference = list2[0] - avg
#
# if minimal_difference < 0:
#     minimal_difference = minimal_difference * -1
#
# for i in list2:
#     difference = i - avg
#     if difference < 0:
#         difference = difference * -1
#     if difference < minimal_difference:
#         minimal_difference = difference
#         closest_element = i
#
# print(avg)
# print(minimal_difference)
# print('Closest element:', closest_element)

# =======================================================================================================================

# 2)вывести на экран пустой квадрат из "*" сторона которого указана в переменой:

# side = input('Enter side length:')
# print('Side length:', side)
# a = int(side)
# i = 1
#
# while i <= a:
#     if i == 1 or i == a:
#         print('*' * (a + 2))
#     else:
#         print('*', ' ' * (a - 2), '*')
#     i += 1

# range
# for i in range(1, a + 1):
#     if i == 1 or i == a:
#         print('*' * (a + 2))
#     else:
#         print('*', ' ' * (a - 2), '*')

# =======================================================================================================================

# 3) переделать первое задание под меню с помощью цикла

# a = '1 найти min число в листе'
# b = '2 удалить все одинаковые значения'
# c = '3 заменить каждое четвертое значение на "Х'
# d = '4 вывести элемент листа, значение которого ближе всего к среднему арифметическому всех элементов этого же листа'
#
# menuList = [a, b, c, d]
#
# for i in menuList:
#     print(i)
# e = input('Choose task number:')
# chosenTask = int(e)
#
# if chosenTask == 1:
#     print('Your chosen task:', menuList[int(e) - 1])
#     list1 = [22, 3, 5, 2, 8, 2, -23, 8, 23, 5]
#     print('List:', list1)
#     print('Your result:', min(list1))
# elif chosenTask == 2:
#     print('Your chosen task:', menuList[int(e) - 1])
#     list1 = [22, 3, 5, 2, 8, 2, -23, 8, 23, 5]
#     i = 0
#     while i < len(list1):
#         current = list1[i]
#         if list1.count(current) > 1:
#             while list1.count(current) > 1:
#                 list1.remove(current)
#         else:
#             i += 1
#     print('List:', list1)
#     print('Your result:', list1)
# elif chosenTask == 3:
#     print('Your chosen task:', menuList[int(e) - 1])
#     list1 = [22, 3, 5, 2, 8, 2, -23, 8, 23, 5]
#     for i in list1[::4]:
#         list1[list1.index(i)] = 'x'
#
#     print('List:', list1)
#     print('Your result:', list1)
# elif chosenTask == 4:
#     print('Your chosen task:', menuList[int(e) - 1])
#     list2 = [22, 3, 5, 2, 8, 2, -23, 8, 23, 5]
#
#     sum_list2 = 0
#
#     for i in list2:
#         sum_list2 += i
#
#     avg = round(sum_list2 / len(list2))
#     closest_element = None
#     minimal_difference = list2[0] - avg
#
#     if minimal_difference < 0:
#         minimal_difference = minimal_difference * -1
#
#     for i in list2:
#         difference = i - avg
#         if difference < 0:
#             difference = difference * -1
#         if difference < minimal_difference:
#             minimal_difference = difference
#             closest_element = i
#
#     print('List:', list2)
#     print('Average:', avg)
#     print('Closest element:', closest_element)
# else:
#     print('No such task number.')


# =======================================================================================================================

# 4) вывести табличку умножения с помощью цикла while
# TODO
# i = 1
# max_number = 9
# while i <= max_number:
#     k = 1
#     while k <= max_number:
#         result = i * k
#         if result // 9:
#             print(result, end=' ')
#         else:
#             print(result, end='  ')
#         k += 1
#     print()
#     i += 1

