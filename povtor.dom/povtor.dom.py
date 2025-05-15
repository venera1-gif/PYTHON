def calculate(n1,n2,n3):
    return n1+n2+n3

calculate(1, 2, 3)


amount = calculate(1, 2, 3)
print(calculate(1,2,3))
print(amount)

def substract(n1,n2,n3):
    return n1-n2-n3
result = substract(10,20,15)
print(substract(10,1,2))
print(result)

products = {
    'apple': 200,
}
def get_product_price_with_discount(name):
    price = products[name]
    return price -price * 0.10

product_price = get_product_price_with_discount("apple")
# print(product_price)




# задание по функциям
def is_even(number):
    return number % 2 == 0
print(is_even(4))
# print(is_even(7))

def repeat_string(text,count):
    return text * count
result = repeat_string("Python",3)
print(result)

def find_max(n1,n2,n3):
    return n1-n2-n3
max_value = find_max(10, 20, 15)
print(max_value)


# Домашнее задание 1.input
apple_count = int(input("Сколько яблок я купила?"))
print(apple_count)
apple_price = float(input("Сколько яблок стоили?"))
print(apple_price)
total_price = apple_count * apple_price
print("Общая стоимость: {total_price}")

# 1 Работа с индекцами в строках
word = input("Введите слово:")
print(word[0])
print(word[-1])
if len(word) > 2:
    print(word[2])
print(word[-2])



    
    





