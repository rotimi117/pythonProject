
def discount_price(price):
    discount = 0.1 * price
    return f"you have been given 10percent discount of {discount} your bill is {price - discount}"

price = int(input("Enter price of goods purchased:   "))

print(discount_price(price))