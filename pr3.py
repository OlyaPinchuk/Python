# TASK 1
# 1)Створити пустий list
# 2)Створити клас Letter
# 3) створити змінну класу __count.
# 4) при створенні об'єкта має створюватись змінна об'єкта(пропертя) __text, для цієї змінної мають бути гетер і сетер
# TODO

# 5) при створені об'єкта __count має збільшуватися на 1
# 6) має бути метод(метод класу) для виводу __сount
# 7) має бути метод який записує в наш ліст текст з нашої змінної __text
#
# ###############################################################################
# TASK 2

# 1) написати програму для запису відомостей про пасажирські перевезення
# 2) перевезення відбувається трьома способами, літаком, машиною, поїздом,
# 3) дані які треба буде зберігати:
#   - вартість квитка(літак, поїзд)
#   - кількість пасажирів(машина)
#   - час в дорозі(всі)
#   - час реєстрації(літак)
#   - клас:перший,другий(літак)
#   - вартість пального(машина)
#   - км(машина)
#   - місце: купе,св(поїзд)
# 4) методи:
#   - розрахунок вартості доїзду(машина)
#   - загальний час перельоту(літак)
#   - порівняти час в дорозі між двома будь якими транспортними засобами(двома об'єктами) - наприклад"літак на 5 годин
#   швидше за поїзд"
#   - вивести всі дані про перевезення(поїзд)
# ===========================================================================================================
# TASK 1
#
# my_list = []
# 
# 
# class Letter:
#     __count = 0
# 
#     def __init__(self, text):
#         self.__text = text
#         self._increment_count()
# 
#     def __set_text(self, text):
#         self.__text = text
# 
#     def __get_text(self, text):
#         return self.__text
# 
#     def set_to_list(self):
#         my_list.append(self.__text)
# 
#     @classmethod
#     def _increment_count(cls):
#         cls.__count += 1
# 
#     @classmethod
#     def get_count(cls):
#         return cls.__count
# 
# 
# my_letter1 = Letter('This is letter 1')
# my_letter2 = Letter('This is letter 2')
# 
# my_letter1.set_to_list()
# my_letter2.set_to_list()
# 
# print(my_letter1.__dict__)
# print(my_letter2.__dict__)
# 
# print(my_list)
# 
# print(Letter.get_count())


# ===========================================================================================================
# TODO
# TASK 2

# class Vehicle:
#
#     def __init__(self, travel_time):
#         self.travel_time = travel_time
#
#     def show_info(self):
#         return dict(travel_time=self.travel_time, vehicle_type=self.vehicle_type)
#
#
# class Plane(Vehicle):
#
#     vehicle_type = 'plane'
#
#     def __init__(self, travel_time, class_type):
#         super().__init__(travel_time)
#         self.class_type = class_type
#
#     def show_info(self):
#         info = {**super().show_info(), **self.__dict__}
#
#         return info
#
#
# passenger1 = Plane('2hr', '1st class')
#
# print(passenger1.show_info())
#
