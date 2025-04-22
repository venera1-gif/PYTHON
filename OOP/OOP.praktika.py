# class BankAccount:Инкапсуляция.
#     def __init__(self,account,fuul_name, account_type, balance = 0):
#         self.account = account
#         self.fuul_name =fuul_name 
#         self.account_type= account_type
#         self.balance  = balance 

#     def deposit(self, amount):
#        self.balance += amount
#        print(f'Ваш баланс: {self.balance}')
         
#     def withdraw(self, amount):
#        if self.balance < amount:
#         print(f'Недостаточно средств {amount - self.balance}')
#        else:
#         self.balance -= amount
#         print(f'Успешно сняли {amount}, ваш остаток {self.balance}')

#     def show_info(self):
#         print(f'Номер счета: {self.account},Имя владельца: {self.fuul_name}, тип счета {self.account_type} , текущий баланс {self.balance}')

# bank_account = BankAccount('10022523233423', 'Venera Joldosova', 'Текущий')
# account1 = BankAccount('221119881111', 'Raxat Maseitiva', 'Сберегательный' )
# account2 = BankAccount('151220012023','Nyriya Junusova', 'текущий')
# # print(f'Счет: {bank_account.account}\nФИО: {bank_account.fuul_name}\nТип счета: {bank_account.account_type}\nБаланс: {bank_account.balance} ')
# print(bank_account.balance)
# bank_account.deposit(1000)
# bank_account.withdraw(500) 
# bank_account.show_info()  
# account1.show_info()
# account2.show_info()
# account1.deposit(1000)
# account2.withdraw(500)

# class Cat:
#     def __init__(self, name,age):
#        self.name = name
#        self.age = age

#     def meow(self):
#        print(f' Кто мяукает: {self.name} ')

#     def brithday(Self):
#        Self.age += 1
#        print(f' Сколько лет: {Self.age}')
       
# Cat = Cat('Пушистик', 1)
# Cat.meow()
# Cat.brithday()

# class Counter:
#    def __init__(Self, count= 0 ):
#        Self.count = count
       
#    def add(self):
#       self.count += 1
#       print(f'Прибавлять 1, текущее значение: {self.count }')
      
#    def reset(self):
#       self.count = 0
#       print(f'Сбрасывать до 0 , текущее значение:{self.count }')

# counter = Counter()
# counter.add()
# counter.add()
# counter.reset() 



      


    





        