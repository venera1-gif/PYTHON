# Работа с файлами
'''
    r (чтение),
    w (запись, удаляет содержимое файла,если он существует),
    a (добавление данных в файл),
    r+ (запись и чтение, файл перезаписывается).
'''

# students = open("students.txt", "w", encoding="UTF-") 
# students.write("aida") 
# students.close() 

# students =open("students.txt", "a", encoding='UTF-8')
# students.write("\n Мырзайым")
# students.close()

# students = open("students.txt", "r", encoding="UTF-8")
# text = students.read()
# print(text)
# students.close()



# список 2 работы с файлами
# with open("students.txt", "w", encoding="UTF-8") as f:
#     f.write("Наргиза\nВенера\nжамиля")

# with open("students.txt", "a", encoding="UTF-8") as f:
#     f.write("\nРахат\nЖазгул\nНурия")
    
# with open("students.txt", "w", encoding="UTF-8") as f:
#     f.writelines(["1\n","2\n","3\n","4"])

# with open("students.txt", "r", encoding="UTF-8") as f:
#     names = f.readlines()
#     for name in names:
#         print(name)


# with open("cars.txt","w", encoding="UTF-8") as f:
#     f.write('Honda,2004\n',)
#     f.write("mers,2010\n",)

# with open("cars.txt", "r") as f:
#     names = f.readlines()
#     for name in names:
#         print 


# N = int(input("Введите чтсло N:"))
# for i in range(1, N + 1):
#     print(i)

# amount = 0
# N = int(input("Ввведите число N:"))
# print("Сумма четных чисел:",)
# for i in range(1, N + 1):
#  if i % 2 == 0:
#     amount += i
#     print(amount)

# n = int(input("Введите число N:"))
# factorial = 1
# for i in range(1, n+ 1):
#     print(factorial,i)
#     factorial *= i
# print(factorial)


# k = int(input("Ввудите число:"))
# for i in range(1, 11):
#     result = k * i
#     print(f"{k}* {i}= {result}")    

# H = 10
# for i in range (1, H+1):
#     print("*" * i)


# n =[3,5,2,4,]
# amount = 0
# for i in n:
#     amount += i
#     print(amount)
# averege = amount/len(n)
# print(averege)
# for i in n:
#     if i> averege:
#         print(i)

# N = input("Введите число N:")
# amount = 0
# for i in N:
#     amount += int(i)
# print(amount)





