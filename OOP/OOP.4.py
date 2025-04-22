# Полиформизм. __str__ это магический метод.
class PaymentMethod:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self._balance = balance
        
    def process_payment(self, amount):
        pass

    def get_balance(self):
        return self._balance
    
    def withdraw(self, amount):
        self._balance -= amount
    
    def deposit(self, amount):
        self._balance += amount
        print(self._balance)

    

class MBank(PaymentMethod):
    def __init__(self, account_number, balance):
        super().__init__(account_number, balance)
        self.__currency = 'USD'

    def process_payment(self, amount):
        print(self.__currency)
        if amount <= self.get_balance():
            self.withdraw(amount)
            print(f'Произведен платеж на сумму {amount} через mbank')
        else:
            print('Недостаточно средств на счете')
       
    def __str__(self):
        return 'mbank'

class OptimaBank(PaymentMethod):
    def process_payment(self, amount):
        print(f'Произведен платеж на сумму {amount} через Optima')
            
    def __str__(self):
        return 'optuma'

mbank = MBank(100,200)
optima = OptimaBank(200 ,300)

mbank.deposit(100)
mbank.process_payment(350)


class A:
    def __init__(self):
        self.a = 10
        self.__b = 20

    def get_b(self):
        return self.__b
    
class AA(A):
    def get_a(self):
        return self.a

aa = AA()
print(aa.get_a())
print(aa.get_b())
    
        


        