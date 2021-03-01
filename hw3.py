# 1)
# создать класс Human(имя и возраст)
# и два класса Prince и Cinderella которые наследуются от Human
# у принца должен быть размер туфельки и  метод который принимает лист золушек и выводит какой золушки подошла туфелька
#
# 2)
# Создать класс Rectangle:
# -конструктор принимает две стороны x,y
# -описать арифметические методы:
#   + сума площадей двух экземпляров класса
#   - разница площадей
#   == или площади равны
#   != не равны
#   >, < меньше или больше
#   при вызове метода len() подсчитывать сумму сторон

# ========================================================================================

# 1)
# создать класс Human(имя и возраст)
# и два класса Prince и Cinderella которые наследуются от Human
# у принца должен быть размер туфельки и  метод который принимает лист золушек и выводит какой золушки подошла туфелька


# class Human:
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def __info(self):
#         return f'{self.name} - {self.age}'
#
#
# class Prince(Human):
#     def __init__(self, name, age, shoe):
#         super().__init__(name, age)
#         self.shoe = shoe
#
#     def find(self, girls):
#         for girl in girls:
#             if self.shoe == girl.shoe_size:
#                 print(f'I found her: {girl.name},', f'Her shoe size: {girl.shoe_size}')
#
#
# class Cinderella(Human):
#     def __init__(self, name, age, shoe_size):
#         super().__init__(name, age)
#         self.shoe_size = shoe_size
#
#
# prince = Prince('Jack', 30, 15)
# cinderella = Cinderella('Ann', 20, 15)
# cinderella1 = Cinderella('Vik', 25, 12)
# cinderella2 = Cinderella('Li', 27, 17)
# cinderella3 = Cinderella('Vik', 25, 19)
#
# list_of_cinderellas = [cinderella, cinderella1, cinderella2, cinderella3]
#
# print('Prince:', prince.__dict__)
# print('Cinderella:', cinderella.__dict__)
#
# prince.find(list_of_cinderellas)

# ========================================================================================
# TODO
# 2)
# Создать класс Rectangle:
# -конструктор принимает две стороны x,y
# -описать арифметические методы:
#   + сума площадей двух экземпляров класса +
#   - разница площадей +
#   == или площади равны
#   != не равны
#   >, < меньше или больше
#   при вызове метода len() подсчитывать сумму сторон

class Rectangle:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def perimeter(self):
        return self.x + self.y

    def area(self):
        return self.x * self.y

    def __add__(self, other):
        return self.area() + other.area()

    def __sub__(self, other):
        return self.area() - other.area()

    def __eq__(self, other):
        return self.area() == other.area()   # google

    def __eq__(self, other):
        return self.area() != other.area()



rectangle1 = Rectangle(5, 2)
rectangle2 = Rectangle(2, 2)

print(rectangle1.area())
print(rectangle2.area())
print(rectangle1 + rectangle2)
print(rectangle1 - rectangle2)
print(rectangle1 == rectangle2)
print(rectangle1 != rectangle2)






