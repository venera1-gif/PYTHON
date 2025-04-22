# numbers = [10,20,30]

# try:
#     print(numbers[3])
# except IndexError:
#     print("Такого индекса нет в списке.")

# try:
#     result = 10/ 0
# except ZeroDivisionError:
#     print("На ноль делить нельзя.")

# try:
#     num = int(input("Введите число:")) # Ощибка, если ввести не число
#     result = 10/ num  # Ошибка при вводе 0
#     print(result)
# except ZeroDivisionError:
# #     print("На ноль делить нельзя.")
# # except ValueError:
# #     print("Вы ввели не число.")
# except ValueError:
#       print("Произошла ошибка.")
# finally:
#       print("Это блок выполняется всегда")

# # print("Конец программы")

# try:
#     num = int(input("Введите число:")) # Все ошибки уловливаем здесь 
#     result = 10/ num
#     print("Результат:", result)
# except Exception as e:
#     print(f"Произошла ошибок: {e}") 
# finally:
#     print("Этот блок выполняется всегда.")

# try:
#     num = int(input("Введите число:"))
#     num2 = int(input("Введите второе число:"))
#     result = num/ num2
#     print("Результат:", result)
# except ZeroDivisionError:
#     print("не делиться на ноль:")
# except ValueError:
#     print("текс нельзя вводить")
# finally:
#     print("Завершение программы.")


# try:
#     num1 = int(input("Введите первое число:"))
#     num2 = int(input("Введите второе число:"))
#     operation =input("Введите операцию (+,-,*,/):")
#     if operation == "+":
#         result = num1 - num2
#     elif operation == "-":
#         result = num1 - num2
#     elif operation == "*":
#         result = num1 * num2
#     elif operation == "/":
#         result = num1/ num2
#     else:
#         result = "Некоррекная операция"
#     print("Результат:", result)
# except ZeroDivisionError:
#     print("Ошибка: Деление на ноль!")
# except ValueError:
#     print("Ошибка :Введите корректное число!")
# except Exception as e:
#     print("Ошибка:", e)
# # finally:
# #     print("Операция завершена.")

# try:
#     password = input('Vvedite password:')  
#     if not password.isalpha():
#        raise ValueError('Пароль должен быть строкой!')
#     elif len(password) < 6:
#        raise ValueError('Пароль должен быть строкой!')
#     print('ok')
# except ValueError:
#     print('not ok')
# finally:
#     print("Проверка завершена")

# try:
#     file_name = input('Введите имя файла:')

#     with open(file_name, "r") as f:
#         read_file=f.read()
#         print('Содержимое файла:')
#         print(read_file)
# except FileNotFoundError:
#     print('файл не найден.')
# finally:
#     print('Операция завершена.')
    

    
    







