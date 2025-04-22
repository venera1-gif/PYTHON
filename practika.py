# with open("names.txt", "w") as f:
#     f.write("Aida\nMyrzaim\nVenera\n")
#     f.writelines(["Aida\n", "Myrzaim\n", "Venera\n"])

# with open("names.txt", "a") as f:
#     f.write("Eliza\n")

# with open("names.txt", "r") as f:
#     print(f.read())

# products = {
#     "apple": 50,
#     "orange": 60,
#     "banana":100,
# }

# products_str = ""
# for name, value in products.items():
#     products_str += f"{name} - {value}\n"
# print(products_str)
# with open("products.txt", "w", encoding="UTF-8")as f:
#     f.write(products_str)

# with open("products.txt", "r") as f:
#     content = f.read()
#     print(content)

# # with open("products.txt", "a") as f:
# #     f.write("potapo - 40")

# with open("products.txt", "r") as f:
#     products = f.readlines()
#     amount = 0
#     for product in products:
#         product_data = product.split()
#         print(product_data)

    #     price = product_data[-1]
    #     amount += int(price)
    #     print(price)

#     # print(amount)

# with open("cities.txt", "w") as f:
#     f.write("Moskov - 120000\nOsh - 34000")
# # with open("cities.txt", "r") as f:
# #     print(f.read())
# with open("cities.txt", "a") as f:
#     f.write("\nKant - 25000")
# with open("cities.txt", "r") as f:
#     cities = f.readlines()
#     filtered_cities= []
#     for citi in cities:
#         population =int(citi.split() [-1])
#         print(population)
#         if population > 100000:
#             print(citi)
#             filtered_cities.append(citi)
# print("filtered_cities")
# with open("filtered_cities.txt", "w") as f:
#     f.writelines(filtered_cities) 

    







