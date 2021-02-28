# strings
#
# 1)написати прогу яка вибирає зі введеної строки цифри і виводить їх через кому,
# наприклад:
# st = 'as 23 fdfdg544' введена строка
# 2,3,5,4,4        #вивело в консолі.
# #################################################################################
# 2)написати прогу яка вибирає зі введеної строки числа і виводить їх
# так як вони написані
# наприклад:
#   st = 'as 23 fdfdg544 34' #введена строка
#   23, 544, 34              #вивело в консолі
# #################################################################################
#
# list comprehension
#
# 1)есть строка:
# greeting = 'Hello, world'
# записать каждый символ в лист поменяв его на верхний регистр
# пример:
# ['H', 'E', 'L', 'L', 'O', ',', ' ', 'W', 'O', 'R', 'L', 'D']
#
# 2) с диапазона от 0-50 записать в лист только не парные числа, при этом возвести их в квадрат
# пример:
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, ...]
#
# function
#
# - створити функцію яка виводить ліст
# - створити функцію яка приймає три числа та виводить та повертає найменьше.
# - створити функцію яка приймає три числа та виводить та повертає найбільше.
# - створити функцію яка приймає будь-яку кількість чисел, повертає найменьше, а виводить найбільше
# - створити функцію яка виводить ліст
# - створити функцію яка повертає найбільше число з ліста
# - створити функцію яка повертає найменьше число з ліста
# - створити функцію яка приймає ліст чисел та складає значення елементів ліста та повертає його.
# - створити функцію яка приймає ліст чисел та повертає середнє арифметичне його значень.
#
# decorators
# - є функція:
# def pr():
#     return 'Hello_boss_!!!'
#  написати декоратор до цієї функції, який замінює нижні підчеркування на пробіли і повертає це значення

# =========================================================================================================================
# =========================================================================================================================
# =========================================================================================================================
# 1)написати прогу яка вибирає зі введеної строки цифри і виводить їх через кому,

# str_input = input('Enter your string:')
# result_string = ''
#
# for i in str_input:
#     if i.isdigit():
#         result_string += i
#
# result_string = ', '.join(result_string)
# print(result_string)
# =========================================================================================================================

# 2)написати прогу яка вибирає зі введеної строки числа і виводить їх
# # так як вони написані
# # наприклад:
#   st = 'as 23 fdfdg544 34' #введена строка
#   23, 544, 34              #вивело в консолі

# str_input = input('Enter your string:')
# res_string = ''
#
# for i in str_input:
#     if i.isdigit():
#         res_string += i
#     else:
#         res_string += ' '
#
# res_string = res_string.split()
# res_string = ', '.join(res_string)
# print(res_string)

# =========================================================================================================================
# 1)есть строка:
# greeting = 'Hello, world'
# записать каждый символ в лист поменяв его на верхний регистр
# пример:
# ['H', 'E', 'L', 'L', 'O', ',', ' ', 'W', 'O', 'R', 'L', 'D']

# greeting = 'Hello, world'
#
# res_list = [i.upper() for i in greeting]
#
# print(res_list)
# =========================================================================================================================

# 2) с диапазона от 0-50 записать в лист только не парные числа, при этом возвести их в квадрат
# пример:
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, ...]

# res_list = [i**2 for i in range(51) if i % 2 != 0]
#
# print(res_list)

# =========================================================================================================================
# - створити функцію яка виводить ліст

# list1 = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
#
#
# def my_func():
#     print(list1)
#
#
# my_func()

# =========================================================================================================================
# - створити функцію яка приймає три числа та виводить та повертає найменьше.

# def my_func(a=1, b=2, c=3):
#     minimal_value = a
#     if b < a and b < c:
#         minimal_value = b
#     elif c < a and c < b:
#         minimal_value = c
#     print(minimal_value)
#     return minimal_value
#
#
# my_func(-7, 6, 2)

# =========================================================================================================================
# - створити функцію яка приймає три числа та виводить та повертає найбільше.

# def my_func(a=1, b=2, c=3):
#     max_value = a
#     if b > a and b > c:
#         max_value = b
#     elif c > a and c > a:
#         max_value = c
#     print(max_value)
#     return max_value
#
#
# my_func(-1, 3, 44)

# =========================================================================================================================
# - створити функцію яка приймає будь-яку кількість чисел, повертає найменьше, а виводить найбільше

# def my_func(*args):
#     min_value = args[0]
#     max_value = args[0]
#
#     for i in args:
#         if i < min_value:
#             min_value = i
#         elif i > max_value:
#             max_value = i
#
#     print('Max value of your list:', max_value)
#     return min_value
#
#
# my_func(33, -55, 4, 7, 1, 444, 3)

# =========================================================================================================================
# - створити функцію яка виводить ліст
# - створити функцію яка повертає найбільше число з ліста
# - створити функцію яка повертає найменьше число з ліста


# list1 = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
#
#
# def my_func(my_list):
#     max_value = my_list[0]
#     min_value = my_list[0]
#
#     for i in my_list:
#         if i < min_value:
#             min_value = i
#         elif i > max_value:
#             max_value = i
#
#     print(my_list)
#     print('Max:', max_value)
#     print('Min:', min_value)
#
#     return {'Min': min_value, 'Max': max_value}
#
#
# my_func(list1)
# =========================================================================================================================
# - створити функцію яка приймає ліст чисел та складає значення елементів ліста та повертає його.
# - створити функцію яка приймає ліст чисел та повертає середнє арифметичне його значень.

# list1 = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
#
#
# def my_func(my_list):
#     list_sum = 0
#
#     for i in my_list:
#         list_sum += i
#
#     list_avg = list_sum / len(my_list)
#
#     print(my_list)
#     print('Sum:', list_sum)
#     print('Average:', list_avg)
#
#     return list_sum, list_avg
#
#
# my_func(list1)

# =========================================================================================================================

# - є функція:
# def pr():
#     return 'Hello_boss_!!!'
#  написати декоратор до цієї функції, який замінює нижні підчеркування на пробіли і повертає це значення

# def pr():
#     return 'Hello_boss_!!!'
#
#
# def decor(some_func):
#     result = some_func().replace('_', ' ')
#     return result
#
#
# print(decor(pr))
