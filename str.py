# # Конкатенация (обьединение): +
# print("Venera" +" "+ "Joldosova")
# Повторение:*
# print("Venera"* 3)

# name ="Venera"
# #      0123
# print(name[0])
# # print(name[6])-- ошибка
# print(name[-1])

# # Срезы: (start:end:step)
# print(name[1:3])
# print(name[1::2])
# print(name[::-1])

# book_name = "колобок и русалочка"
# # Изменение регистра
# print(book_name.title()) 
# print(book_name.capitalize()) 
# print(book_name.upper())
# print(book_name.lower())

# # citi_name = "Batken"
# # #            012345
# # print(citi_name[0])
# # print(citi_name[1])
# # print(citi_name[-1])
# # print(citi_name[1])
# # print(citi_name[2])
# # print(citi_name[-1])
# # print(citi_name[:3])
# # print(citi_name[:6:2])
# # print(citi_name[-4])
# # # print(citi_name[::-1])

# # school_name = "Школа лицей №13"
# # print(school_name.title())
# # print(school_name.capitalize())
# # print(school_name.upper())
# # print(school_name.lower())

# # Поиск и замена
# gadget_nameb= "Iphone 15 Pro Max"
# #              01234567
# #.replace(old, new): заменяет полстроку.
# print(gadget_nameb.replace("15", "16"))

# # пересоздание переменной
# gadget_name = gadget_nameb.replace("15", "16")
# print(gadget_name)

# # . find(substring): возвращает индекс первого вхождения
# # подстроки (или -1).
# index_ = gadget_name.find("15")
# print(gadget_name[index_:])
# print(gadget_name[:index_])
# # . count(substring): считает количество вхождений подстроки.
# print(gadget_name.count("0"))

# the_best_teacher = "Venera Joldosova 36 year"
# print(the_best_teacher.replace("36","35"))
# the_best_teacher = the_best_teacher.replace("36","35")
# # print(the_best_teacher) 

# str_1 = "text"
# str_2 = "one more text"

# print(str_1 + "" + str_2)
# print("str_1"* 3)

# str_3 = "Helloo World!"

# print(str_3[0])
# print(str_3[-1])
# print(str_3[::2])
# print(str_3[::-1])

# str_5 = "absd"
# print(str_5.upper())
# print(str_5.lower())

# str_6 = "Venera"
# print(str_6. strip())
# print(str_6)
# print("Venera")

# str_7 = "Batken"
# print(str_7.find("o"))
# print(str_7.find("a"))

# str_8 = "Biskek, Moskov 183"
# str_8 = str_8.replace("Moskov", "Toktogul")
# print(str_8)
# print(str_8.replace("Biskek", "Osh"))


# code = {
#     "A": "C",
#     "B": "Z",
#     "C": "E",
#     "D": "H",
#     "E": "L",
#     "F": "O",
# }

# text = "DCEEF"
# uncoded_text = ""
# for i in text:
#     print(i)
#     print(code[i])
#     uncoded_text += code[i]
#     print(uncoded_text)

# text="Venera jana raxat"   
# print(text)
# print(text.upper())
# print(text[::-1])

# print(text.split())
# # uncoded_text = ""
# # for i in text.split():
# #     print(i[0])
# #     uncoded_text += (i[0])
# # print(uncoded_text)


# # name = "Nargiza,Jumagul"
# # print(name.count("a"))

# # # print(name.replace(" ","_"))

# # name = "Nargiza,Jumagul"
# # litters = {

# # }

# # for i in name:

# # Проверка содержимого# Создаем строку и проверяем ее начало /конец
# text = "Школа гимназия №70"
# print(text.startswith("Школа"))  # Проверка: начинается ли строка с "Школа"
# print(text.endswith("№70"))      # Рроверка: заканчивается ли строка на "#70"
# print(text.endswith("гимназия")) # Проверка: заканчивается ли строка на "гимназия"

# # Проверяем, состоят ли строки из цифр или букв
# int_text = "123123h"
# print(text.isdigit())      # Проверка: сожержит ли text тольео цифры
# print(int_text.isdigit())          # Проверка: содержит ли int_text тольео цифры
# print(int_text.isalpha())  # Проверка: содержит ли int_text только буквы
# print(text.isalpha())      # Проверка: содержит ли text только буквы

# # Преоброзование в чисо=ло, если строка состоит из цифр
# if int_text.isdigit():
#     int(int_text)
   
# # Разделение строки по разделителю
# products = "apple, banana, orange"
# print(products.split(", "))       # Разделение на список по ", "

# # Форматирование с помощью f-строк
# name = "Doka"
# age = 22
# # print(f",Меня зовут - {name}, мне {age} года")
# # print(f"5 + 5 ={5+5}")
# # print(f"5 * 3 = {5*3}")

# name = input( "как вас зовут ,?\n-")
# age = input("Сколько вам лет?\n_")
# if age.isdigit():
#     print(f"Пртвет,{name}! Тебе {age} лет.")
# # else:
# #    print("Ты неправильно ввел возраст")

# numbers = "16, 15"
# numbers= input(f"numbers -{numbers},{16*10} ")
# print(f"16+15 ={16+15}")
# # print(f"16*10 ={16*10}")

# num1 = input("Введите число\n- ")
# num2 = input("Введите число\n- ")

# if num1.isdigit() and num2.isdigit():
#     print(f"{num1}+ {num2} = {int(num1)+ int(num2)}")
#     print(f"{num1}- {num2} = {int(num1)- int(num2)}")
#     print(f"{num1} * {num2}= {int(num1) * int(num2)}")


# 5. startswith()
#  • Задание 1: Запросите у пользователя строку и проверьте, начинается ли она с буквы "A" (выведите True или False).
# #  • Задание 2: Дана строка "Hello, world!". Проверьте, начинается ли она с "Hello".
 
# string = input("как вас зовут?")
# print(string.startswith("A"))
# print(string.isdigit())

# greet_str = "Hello, world!"
# # print(greet_str.startswith("Hello"))

# 6. endswith()
#  • Задание 1: Запросите у пользователя строку и проверьте, заканчивается ли она на ".com" (выведите True или False).
#  • Задание 2: Дана строка "document.pdf". Проверьте, заканчивается ли она на ".pdf".

# string = "google.com"
# print(string.endswith("com"))

# string = "documents.pdf"
# print(string.endswith(".pdf"))

# Вот 5 легких заданий по .replace():
#  1. Замена пробелов на дефисы
#  • Запросите у пользователя строку и замените в ней все пробелы на "-".
# Пример ввода: "Привет мир"
# Вывод: "Привет-мир"

# str1= input("Введите строки\n:")
# print(str1.replace(" " ,"-"))

# str2="Я люблю Питон"
# print(str2.replace("Питон", "Pyiton"))

# #3. Форматирование номера телефона
# nomer = input("Введите номер в формате 123-456-789 :")
# print(nomer.replace("-"," "))

# #4. Удаление символа из строки
# str3=input("Венера Введите текст с точками:")
# print("спасибо я удалила все точки вот: " ,str3.replace(".", ""))

# #5. Цензура слова
# str4=input("Введите текст с *плохими* словами:")
# print("вот плохие заменила на *: ",str4.replace("плохие", "*"))

# 2. Фильтр адресов сайтов
#  • Запросите у пользователя веб-адрес. Проверьте, начинается ли он с "https" (для безопасных сайтов), и выведите соответствующее сообщение.
# Пример ввода: "https://example.com"
# # Вывод: "Это безопасный сайт."

# link = input( " Введите веб-адрес: ")
# print(link.startswith("https"))
# if link.startswith("https"):
# #     print("это безопасный сайт")

#  3. Проверка на правильный ввод команды
#  • Дана строка, содержащая команду "RUN_program".
#  • Напишите программу, которая проверяет, начинается ли команда со слова "RUN_" и выводит "Команда запущена", иначе "Ошибка команды".

# command = "RUN_program"
# if command.startswith("RUN_"):
#     print("команда запушена")
# else:
#     print("ошибка")











