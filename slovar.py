# # 1. Создайте словарь books, где:
# books = {}
# # 2. Добавьте в каталог три книги:
# books.update(  
# {  
 
#     "Война и мир": "Лев Толстой",
#     "Преступление и наказание": "Федор Достоевский",
#     "Мастер и Маргарита": "Михаил Булгаков",
# }
# )
# for book in books:
# #     print(book)
# #     print(books[book])
# #     author = books[book]
#     print(f"книга:{book}, Автор:{author}")

# print(books)
# #3. Выведите на экран автора книги "Война и мир"
# print(books["Война и мир"])
# print(books.get("Война и мир"))

# books["Анна Каренина"] = "Лев Толстой"
# del books["Преступление и наказание"]
# print(books )


# cities = {}

# cities.update( 
#     { 
#         "Bishkek": 1000000,
#         "osh": 300000,
#         "Tokmok": 60000,
#     }
# )
# print(cities["osh"])
# print(cities["Bishkek"] + 50000)
# cities["Bishkek"] += 50000
# print(cities)
# del cities["Tokmok"]

# for city in cities:
#     population = cities[city]
# print(f"Город:{city},Население: {population}") 


