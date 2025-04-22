# # dict
# journal = {
#     1: 'Aida',
#     2: 'Nazira',
#     3: 'Myrzaim',
# }

# # добавление или изменение
# journal.update({
#     4: 'Gulmira',
#     5: 'Jumagul',
# })
# journal[6] = 'Abagul'
# journal[4] = 'Gulnara'
# print(journal)

# dict
# student = {
#     'name': 'Aida',
#     'age': 35,
# }

# print(student['name'])
# print(student['age'])
# # изменение данных
# student['name'] = 'Nazira'
# student['age'] = 20
# print(student['name'])
# print(student['age'])
# print(student)

# -
# products = {
#     'orange': 500,
#     'apple': 400,
#     'banana': 600
# }

# получение
# print(products['orange'])
# print(products.get('potato'))  # None
# print(products.get('potato', 'Not found'))  # Not found

# удаление
# del products['banana']
# apple = products.pop('apple')
# print(products)
# print(apple)
# products.clear()  # очистка
# print(products)


# удаление ошибка
# del products['potato']
# products.pop('potato')

# методы
# print(products.keys())  # все ключи
# print(products.values())  # значения
# print(products.items())  # пара ключ-значение


# journal = {
#     1: 'Aida',
#     2: 'Nazira',
#     3: 'Myrzaim',
# }
# # if 2 in journal:
# #     print(f'Такой ученик есть - {journal[2]}')
# # else:
# #     print('Такого ученика нет')

# journal.clear()
# print(journal)

'''
1 Создать словарь с названием 

'''