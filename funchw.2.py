# def sum_odds(*numbers):
#     amount = 0
#     for number in numbers:
#         if number% 2 != 0:
#           amount += number
#     return amount

# print(sum_odds(1,2,3,4,5,6,))
# print(sum_odds(10, 15, 25, 30))

# def describe_car(**kwargs):
#     print(kwargs)
#     for key, value in kwargs.items():
#         print(key, value)

#     for key in kwargs:
#         print(key, kwargs[key])

# # describe_car(mark="Toyota", year=2020, color="Синий")

# def user_info(**kwargs):
#     for key, value in kwargs.items():
#         print(key, value)

# user_info(name="Venera", age=36, city="Batken")
# # user_info(name="Максим", age=30, city="Москва", работа="Программист")

# def filter_positive_numbers(numbers):
#     # вариант 1
#     # positive_numbers = []
#     # for number in numbers:
#     #     if number > 0:
#     #         positive_numbers.append(number)
#     # return positive_numbers

# # вариант 2
#     positive_numbers = list(filter(lambda x: x > 0, numbers))
#     return positive_numbers

# print(filter_positive_numbers([-10, 15, -5, 20, 0, -3, 30]))

# def sguare_numbers(numbers):
#     return list(map(lambda x: x **2, numbers))

# print(sguare_numbers([1, 2, 3, 4, 5]))
# print(sguare_numbers([10,20,30]))

#  #задание 9
# def enumerate_students(students):
#     return list(
#         map(
#             lambda x: f"Студент {x[0] + 1}: {x[1]}",
#             enumerate(students),
#         )
#     )

# print(enumerate_students(["Алина", "Бекзат", "Диана"]))
# print(enumerate_students(["Саша","Петя","Настя","Олег"]))

# # задание 10
# def enumerate_product(products):
#     return list(map(lambda x: f"товар{x[0]+1}: {x[1]}",enumerate(products)))
# # print(enumerate_product(["молоко","хлеб","сыр"]))
# # print(enumerate_product(["Чай","Кофе","Какао"]))

# # задание 2 
# def find_max(*args):
#     return max(args)
# print(find_max(10,20,30,5,15))
# # print(find_max(100,50,200,150))

# # задание 6
# def filter_long_names(names):
#     return list(filter(lambda x:len(x) > 4, names))
    
# print((filter_long_names(["Tom","Aliya","Mark","Aisha",'Anna'])))
# # print((filter_long_names(["John","Robert","Kate","Mia","Alexander"])))

# # Задание 8
# # numbers = (100,200,300)
# # mapped_numbers = list(map(lambda number: number + (number * 0.1), numbers))
# # print(mapped_numbers)
# numbers = (50,75,125)
# mapped_numbers = list(map(lambda number: number + (number * 0.1),numbers))
# print(mapped_numbers)






                        











    