# def multiply(x, y):
#     try:
#         return x * y
#     except:
#         return f"the input must be a number"
#
#
# print(multiply(2, 4))


def invest(principal_amount, interest, ):
    try:
        if principal_amount < 0 and interest < 0:
            return f"input not a positive integer"
        for year in range(4):
                annual_rate_of_return = principal_amount * interest
                new_principal = principal_amount + annual_rate_of_return
                principal_amount = new_principal
                print(f"year{year}:{principal_amount:,.2f}")
    except:
            return f"input must be a positve integer"


print(invest(-1, -60))
