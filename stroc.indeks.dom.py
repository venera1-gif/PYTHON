# # # 1 Работа с индекцами в строках
word = input("Введите слово:")
print(word[0])
print(word[-1])
if len(word) > 2:
    print(word[2])
print(word[-2])

#2. Извлечение подстроки:
word = input("Введите слова:")
print(word[:3])
print(word[-3:])