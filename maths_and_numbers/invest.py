# year 1: $105.00
# year 2: $110.25
# year 3: $115.76
# year 4: $121.55
principal_amount = int(input("Enter amount invested:  "))
interest = 0.05
years = 4
for year in range(4):
    annual_rate_of_return = principal_amount * interest
    new_principal = principal_amount + annual_rate_of_return
    principal_amount = new_principal
    print(f"year{year}:{principal_amount:,.2f}")



def invest(principal_amount, interest,):
        for year in range(4):
            annual_rate_of_return = principal_amount * interest
            new_principal = principal_amount + annual_rate_of_return
            principal_amount =  new_principal
            print(f"year{year}:{principal_amount:,.2f}")
