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

# print('hello world')

list1 = [22, 3, 5, 2, 8, 2, -23, 8, 23, 5]


# 1.1 print(min(list1))

# list1.remove(2)
# print(list1)
# print(list1.count(22))
# print(list1[3::4])

# 1.2 ?????????????
# list1 = [22, 3, 5, 2, 8, 2, -23, 8, 23, 5]
# listOfDuplicates = {}
# toDelete = []
# print(list1)
#
# for i in list1:
#     for k in list1:
#         if i == k:
#             if i in listOfDuplicates:
#                 listOfDuplicates[i] = 2
#             else:
#                 listOfDuplicates[i] = 1
#
# print(listOfDuplicates)
#
# for k in listOfDuplicates:
#     if listOfDuplicates[k] > 1:
#         toDelete.append(k)
#
# print(toDelete)

# for i in list1:
#     for k in toDelete:
#         if i == k:
#             print(i)
#             list1.remove(i)
#

# for i in toDelete:
#     list1.remove()
#     print(i)

# print(list1)

#1111111111111111
# i = 0
# l = [3, 4, 3, 5, 6, 4]
# while i < len(l):
#     if l.count(l[i]) > 1:
#         while l.count(l[i]) > 1:
#             l.remove(l[i])
#         l.remove(l[i])
#     else:
#         i += 1
# print(list1)

#2222222222222222222222222222222222222222
# i = 0
# l = [3, 4, 3, 5, 6, 4]
# while i < len(l):
#     current = l[i]
#     if l.count(current) > 1:
#         while l.count(current) > 0:
#             l.remove(current)
#     else:
#         i += 1
# print(list1)

#33333333333333333333333333333
# i = 0
# l = [3, 4, 3, 5, 6, 4]
# while i < len(l):
#     current = l[i]
#     if l.count(current) > 1:
#         while l.count(current) > 1:
#             l.remove(current)
#     else:
#         i += 1
# print(list1)




# # 1.3
# for i in list1[::4]:
#     list1[list1.index(i)] = 'x'
#     print(i)
# print(list1)

# 2)вывести на экран пустой квадрат из "*" сторона которого указана в переменой:
# side = input('Enter side length:')
# print('Side length:', side)
# a = int(side)
# i = 1
#
# while i <= a:
#     if i == 1:
#         print('*' * (a+2))
#     print('*', ' ' * (a-2), '*')
#     if i == a:
#         print('*' * (a+2))
#     i += 1

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
# e = input('Choose an option:')
# print('Your chosen task:', e)
#
# chosenTask = int(e)
# print(menuList[int(e) - 1])
#
# if chosenTask == 1:
#     print(min(list1))
#
# if chosenTask == 3:
#     for i in list1[::4]:
#         list1[list1.index(i)] = 'x'
#     print(i)
# print(list1)
