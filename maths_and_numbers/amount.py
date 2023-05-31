from decimal import Decimal


class Account:
    def _init_(self, name: str, balance: Decimal):
        self.name = name
        self.balance = balance

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, amount):
        if amount < 0:
            raise ValueError("Balance cannot be negative..")
        self.__balance = amount

    def deposit(self, amount):
        if amount < 0:
            raise ValueError("Amount to deposit cannot be negative ")
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Insufficient Balance")
        self.balance -= amount

    # def _str_(self):
    #     return f"Name Of Account: {self.name} \nAccount Balance: {self.balance}"

    @classmethod
    def torin(cls, amount):
        cls.bonus = 100


account2 = Account()
Account.torin(100)
print(account2.bonus)
