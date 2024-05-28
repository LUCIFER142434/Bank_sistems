class BankAccount:
    def __init__(self):
        self.balance = 0 
        self.__vso_balans = {} 
    def deposit(self,__number_chota,amount):
        self.__vso_balans[__number_chota] = amount + self.balance
        self.balance += amount
    def withdraw(self,__number_chota,amount):
        self.__vso_balans[__number_chota] = self.balance - amount
        self.balance -= amount
    def get_balance(self,__number_chota):
        return f"Текущий Баланс : {self.__vso_balans[__number_chota]}"
    def get_account_number(self,__number_chota):
        return f"Номер счета : {__number_chota}"
        
a = BankAccount()
a.deposit(1, 33)
a.withdraw(1, 30)
print(a.get_account_number(1))
print(a.get_balance(1))
# print(a.__dict__)