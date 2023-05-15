def get_digits(number):
    digits = [int(digit) for digit in str(number)]
    return digits


number = 2342
digit_list = get_digits(number)
print(digit_list)
