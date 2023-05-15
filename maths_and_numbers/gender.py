def gender():
    list_of_genders = ["male", "female", "female", "male", "MALE", "MALE", "FEMALE"]
    number_of_male = 0
    number_of_female = 0
    for i in list_of_genders:
        if i.lower()==("male"):
            number_of_male += 1
        if i.lower()==("female"):
            number_of_female += 1
    totalNumber = [("male", number_of_male), ("female", number_of_female)]

    return f"{totalNumber}"


print(gender())