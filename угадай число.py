# number= 50
# attempt = 1
# while True:
# #    if attempt > 7:
# #       print("Вы исчерпали свои попытки!")
# #       break
# #    print(f" У вас {attempt} попытка")

# #    user_number =input("Введите число:")
# #    if user_number.isdigit():
# #       user_number = int(user_number)

# #       if user_number == number:
# #          print("Вы угадали число!")
# #          break
# #       else:
# #          print("Неверное число!")

# # #       attempt += 1
# # # else:
# # #    print("Вы не ввели число!")

# phone_book = {
#    "Venera": "774581558",
#    "Aida": "226581558",
# }

# def add_contact(name, phone_number):
#    if not phone_book.get(name):
#       phone_book[name] = phone_number
#       print(phone_book)

# def search_contact(name):
#    number = phone_book.get(name)
#    if number:
#       print(number)
#    else:
#       print("Контакт не найден")

# add_contact("Aidaa", "226581558")   
# search_contact("aida") 

# def print_all_contants():
#    text = ''
#    for name, phone_number in phone_book.items():
#       text += f'{name} - {phone_number}\n'
#       print(text)

# while True:
#    command = input("Какую команду вы хотите вызвать?\n1. Добавить контакт\n. 2Найти контакт\n.3 Вывести все контакты\n 4.Остановить программу")
#    if command == '1':
#       pass
#    if command == '2':
#       name = input("Введите имя:")
#       search_contact(name)
#    elif command == '3':
#       print_all_contants()
#    elif command == '4':
#       break 





