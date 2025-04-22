# def add(*numbers): #одна звездочка принимает пазиционные аргументы
#     amount = 0
#     for number in numbers:
#         if number% 2 == 0:
#          amount += number
#     return amount

# print(add(1,2,10,123,234,124,123,123,123123))
# result = add(5,2,10,123,234,124,123,123)
# # print(result)
# # # print(add(2,10,123,234,124,123,123)) 

# # def describe_person(**kwargs): # две звездочка принимает именные оргументы
# #     for key, value in kwargs.items():
# #         print(key, value)

# # describe_person(name="Venera", age=20, city="Batken")

# def is_even(number):
#     if number % 2 == 0:
#         return True
#     else:
#         return False
    
# numbers = range(1, 100)

# #написали сами
# filtered_numbers = []
# for number in numbers:
#     if is_even(number):
#         filtered_numbers.append(number)
# print(filtered_numbers)

# #используем .filter
# filtered_numbers = list(filter(is_even, numbers))
# # print(filtered_numbers)

# numbers = range(1, 100)

# #используем .filter
# filtered_numbers = list(filter(lambda number: number % 2 == 0, numbers))
# print(filtered_numbers)

#принимает функции и обьект map 

# numbers = range(1, 100)
# mapped_numbers = list(map(lambda number: number ** 2, numbers))
# print(mapped_numbers)

# names = ["Venera", "Aida", "Raxat"]
# filtered_names = list(filter(lambda x: len(x) < 5, names))
# print(filtered_names)

# mapped_names = list(map(lambda x: f"Ученик{x[0] + 1}: {x[1]}", enumerate(names)))
# print(mapped_names)


