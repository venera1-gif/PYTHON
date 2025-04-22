# class Car:
#     make = 'Toyota'
#     model = 'Camry'
#     year = 2020

# car = Car()
# print(car.make)

# class Car:
#     def __init__(self,make,model,year):
#         self.make = make
#         self.model = model
#         self.year = year

# car3 = Car('Toyota', 'Camry', 2024)
# # print(car3.make, car3.model, car3.year) 

# class Car:
#     def __init__(self,make,model,year,color, type_):  # добавить новые атрибуты
#         self.make = make
#         self.model = model
#         self.year = year
#         self.fuel = 100
#         # присвоить обьекту атрибуты
#         self.color = color
#         self.type = type_

#     def on(self):
#         print('Машина заведена')

#     def off(self):
#         print('Машина выключена')

#     def drive(self):
#         print('Машина поехала')
#     def stop(self):
#         print("Машина остановилось")

#добавьте метод drive,который выводит на экран "Машина поехала"

# #добавьте метод stop,который выводит на экран "машина остановилось"


# car = Car('Mersedes', 'C100', '2005', 'silver', 'ringht')
# car2 = Car('BMW','e34','2010','blue','left')

# print(car.make,car.model, car.year,car.color,car.type)
# car.on()
# car.off()
# car.drive()
# car.stop()

# # print(car2.make, car.model, car.year, car2.color, car2.type)

class Person:
    def __init__(self, name,age,sex,birthday_date):
        self.name = name
        self.age = age
        self.sex=sex
        self.birthday_date = birthday_date

    def speak(self,sentence):
        print(sentence)

    def eat(self,food):
        print(f'Кушает {food}')

    def drink(self,drink_name):
        print(f'Пьет {drink_name}')

person = Person('Venera',36,'F','22.11.88')
print(f'Имя: {person.name}\Возраст: {person.age}\Пол: {person.sex}\День Рождения: {person.birthday_date}')
person.speak('Я знаю кыргызский язык')
person.eat('банан')
person.drink('кока-колу')

# student 
#1. Создайте Student, у него должны быть атрибуты:

class Student:
    def __init__(self,name,age,group,course):
        self.name = name
        self.age = age
        self.group = group
        self.course = course

    def study(self,subject):
        print(f'{self.name} учит {subject}')

    def sleep(self,hours):
        print(f'{self.name} Спит {hours} часов')

# 2.Создайте обьект класса Student-student,передайте свои аргументы.

student = Student("Венера", 36,'Группа 3' ,'5 курс')
print(student)
print(f'Имя: {student.name}\Возраст: {student.age}\Группа: {student.group}\Курс: {student.course}')
student.study('Информатика')
student.sleep('9')

class Animal:
    def __init__(self,species,name,age,habital):
        self.species = species
        self.name = name
        self.age = age
        self.habital = habital

    
    def speak(self,sound):
        print(f'{self.name} издает звук: {sound}')

    def eat(self,food):
        print(f'{self.name} ест {food}')

    def sleep(self,hours):
        print(f'{self.name} спит {hours} часов')


animal = Animal('Собака', 'Бобик', 2, 'Домашний')
print(animal)
print(f'Вид: {animal.species}\Имя: {animal.name}\Возраст: {animal.age}\Место обитания: {animal.habital}')
animal.speak('гав гав')
animal.eat('собачий корм')
animal.sleep(' 10')





        






        




    


        




        
        










        
    