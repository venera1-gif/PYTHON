# # домашнее задание 1
# задача:
class Book:
    def __init__(self,title,author):
        self.set_title(title)
        self.__author = author

    def set_title(self,title):
        if title.strip():
            self.__title = title
        else:
            print('Ошибка: Название книги не может быть пустым!')

    def get_title(self):
        return self.__title
    
    def set_author(self, author):
        self.__author = author

    def get_author(self):
        return self.__author
    
    def __str__(self):
        return f'Книга: {self.__title}, Автор: {self.__author}'
    
    
book1 = Book('Гарри Поттер', 'дж. К. Роулинг')
print(book1)

# Задание 2:
class Temperature:
    def __init__(self,celsius):
        self.set_temperature(celsius)

    def set_temperature(self,celsius):
        if celsius >= -273.15:
            self.__celsius = celsius
        else:
            print('Ошибка: температура не может быть ниже -273.15C!')

    def get_temperature(self):
        return self.__celsius
    
    def to_fahrenheit(self):
        return f'температура: {self.__celsius}'
    
temp = Temperature(20)
print('температура в Цельсиях:',temp.get_temperature() )
print('температура в Фаренгейтах:', temp.to_fahrenheit())
print('программа завершилось')


        



    