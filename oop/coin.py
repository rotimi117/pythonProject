class Coin:
    def __init__(self,two_euro,one_euro,fifty_euro,twenty_euro,ten_euro):
        self.two_euro = two_euro
        self.one_euro = one_euro
        self.fifty_euro = fifty_euro
        self.twenty_euro = twenty_euro
        self.ten_euro = ten_euro

    def universal_str(self):
        return f" 2 Euros: {self.two_euro}, 1 Euro: {self.one_euro}, 50 Euros: {self.fifty_euro}, 20 Euros: {self.twenty_euro}, 10 Euros: {self.ten_euro} "

    def total_amount(self):
        return (self.two_euro)+(self.one_euro)+(self.fifty_euro)+(self.twenty_euro)+(self.ten_euro)




my_coin = Coin(two_euro=5,one_euro=7,fifty_euro=6,twenty_euro=2,ten_euro=4)
print(f"Coins in wallet: {my_coin.universal_str}")
print(f"Total amount of money: {my_coin.total_amount()} Euro")
