# # 1. f-string: Форматированный вывод:
# num1 = input("Введите число\n")
# num2 = input("Введите второе число\n")
# print(f"{num1}+ {num2}= {int(num1)*int(num2)}")

# # 2. split(): Разделение строки:
# products =("alma,banana,orange,")
# print(products.split(","))

# # 3.startswith(): Проверка начала строки:
# string = input("Введите название страны:")
# print("начинается с:", string[0])
# print(string.startswith("К"))
# print(string.isdigit())

# greet_str = "Кыргызстан"
# print(greet_str.startswith("К")) 

# # 4. endswith():Проверка окончания строки:
# string = "documents.jpg"
# print(string.endswith("jpg"))
# string = "documents.png"
# print(string.endswith("png"))

# # 5. isdigit(): Проверка на числа:
# password = input("Введите пароль:")

# if password.isdigit(): 
#     print("Пароль состоит из цифр? True")
# else:
#    print(password.isdigit())

# # 6. isalpha(): Проверка на буквы:
# name = "Venera123"
# print("Имя состоит только из букв?",name.isalpha())

# # 7.replace(): Замена подстроки:
# text= input("Введите текст:")
# new_text= text.replace("не","очень")
# print("Измененный текст:",new_text)

# # 8. Проверка формата телефонного номера:
# nomer = input("Введите номер телефона:")
# if nomer.startswith("+996"):
#   print("Это кыргызстанский номер? True")

# # 9. Разделение полного имени:
# full_name=input ("Введите полное имя:")
# full_name = input("Вввести фамилию:")
# print(full_name.split(" ")) 
# print("Фамилия состоит только из букв?",full_name.isalpha())

# # 10. Проверка домена почты:
# string= "example@gmail.com"
# print(string.endswith("com")) 
# user_input = input("Введите строку\n")
# print("Это gmail-фдрес?", user_input.endswith("gmail.com"))
