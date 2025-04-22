# # # class BankAccount:
# # #     def __init__(self, owner, balance, account_type):
# # #        self.owner = owner         # Публичный атрибут
# # #        self.__balance = balance   # Приватный атрибут (нельзя изменить извне)
# # #        self._account_type = account_type     # Защищенный атрибут (можно изменить извне)

# # #     # добавьте метод deposit, который добавляет сумму к приватному атрибуту __balance
# # #     def get_balance(self):
# # #         return self.__balance
    
# # # #     def deposit(self, amount):
# # # #         self.__balance += amount
# # # #         return self.__balance
# # # # bank_account = BankAccount('Venera', 200, 'saving')    # создаем обьект класса BankAccount
# # # # print(bank_account.owner)         # можно обратиться к приватному атрибуту
# # # # print(bank_account.get_balance())   # можно обратиться к приватному атрибуту через метод
# # # # print(bank_account._account_type)
# # # # print(bank_account.get_balance())
# # # # print(bank_account.__balance)  # нельзя обратиться к приватному атрибуту     # можно обратиться к защищенному атрибуту

# # # class Animal:
# # #     def __init__(self, name, species):
# # #         self.name = name
# # #         self.species = species

# # #     def make_sound(self):
# # #         print('ничего')

# # # class Dog(Animal):

# # #     def __init__(self, name, species, breed):
# # #         super().__init__(name, species)
# # #         self.breed = breed

# # #     def make_sound(self):
# # #         print('гав')

# # # class Cat(Animal):
# # #     def make_sound(self):
# # #         print('мяу')

# # # dog = Dog('рекс', 'собачьи', 'лабрадор')
# # # cat = Cat('корнишон рекс', 'кошачья')
# # # print(dog.name, dog.species, dog.breed)
# # # dog.make_sound()
# # # print(cat.name, cat.species)
# # # cat.make_sound()


# # class OnlineCourse:
# #     def __init__(self,course_name,students=[]):
# #             self.__course_name = course_name
# #             self.__students=students
    
# #     def add_student(self,name):
# #         self.__students.append(name)
# #         print(self.__students)

# #     def remove_student(self,name):
# #         self.__student.remove(name)
# #         print(self.__students)

# #     def get_students(self,name):
# #         return self.__students
    
# #     def get_course_name(self):
# #          return self.__course_name
        
# # course = OnlineCourse('python')
# # course.add_student('venera')
# # course.add_student('Aida')
# # print(course.get_students())
# # course.remove_student('Aida')
# # print(course.get_students())

# class User:
#     def __init__(self, password, balance):
#         self.__password = password
#         self.__balance = balance

#     def set_password(self,new_password):
#         print(self.__password)
#         self._password= new_password
#         print(self.__password)
    
#     def check_password(self, password):
#         if self.__password == password:
#            return True
#         else:
#             return False
        
    
    
#     def deposit(self, amount):
#         self.__balance += amount
#         print(self.__balance)

#     def get_balamce(self,password):
#         if self.check_password (password):
#             return self.__balance
#         else:
#             return 'доступ запрещен!'
        
# # user = User('1222', 0)
# # user.set_password('7uj8h8y8y')
# # print(user.check_password('7uj8y8y'))
# # user.deposit(500)
# # print(user.__balance('7uj8h8sd'))

# class Book:
#     def __init__(self, title, author):
#         self.title = title
#         self.author = author

#     def get_info(self):
#         return f'{self.title} - {self.author}'
# class EBook(Book):
#     def __init__(self, title, author, file_size):
#         super().__init__(title, author)
#         self.file_size = file_size

#     def get_info(self):
#         return f'{self.title} - {self.author}, Файл: {self.file_size}  PD'
    
# class PaperBook(Book):
#     def __init__(self, title, author, pages):
#         super().__init__(self,title, author, pages)
#         self.pages = pages 


# ebook = EBook('Гарри Поттер', 'Дж.К.Роулинг', 5)
# paperbook = PaperBook('История','Т.Н.Омурбеков', 200)
# print(ebook.get_info())
# print(paperbook.get_info())


        


        








        
    


