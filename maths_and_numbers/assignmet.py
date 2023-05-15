def computeTax(status, taxableIncome):
    RATE_1 = 0.15
    RATE_2 = 0.25
    RATE_3 = 0.28
    RATE_4 = 0.33
    RATE_5 = 0.35

    if status == "Single":
        brackets = [8350, 33950, 82250, 171550, 372950]
    elif status == "Married Jointly":
        brackets = [16700, 67900, 137050, 208850, 372950]
    elif status == "Married Separately":
        brackets = [8350, 33950, 68525, 104425, 186475]
    elif status == "Head of Household":
        brackets = [11950, 45500, 117450, 190200, 372950]
    else:
        raise ValueError("Invalid filing status")

    if taxableIncome <= brackets[0]:
        tax = taxableIncome * RATE_1
    elif taxableIncome <= brackets[1]:
        tax = brackets[0] * RATE_1 + (taxableIncome - brackets[0]) * RATE_2
    elif taxableIncome <= brackets[2]:
        tax = brackets[0] * RATE_1 + (brackets[1] - brackets[0]) * RATE_2 + (taxableIncome - brackets[1]) * RATE_3
    elif taxableIncome <= brackets[3]:
        tax = (
            brackets[0] * RATE_1
            + (brackets[1] - brackets[0]) * RATE_2
            + (brackets[2] - brackets[1]) * RATE_3
            + (taxableIncome - brackets[2]) * RATE_4
        )
    else:
        tax = (
            brackets[0] * RATE_1
            + (brackets[1] - brackets[0]) * RATE_2
            + (brackets[2] - brackets[1]) * RATE_3
            + (brackets[3] - brackets[2]) * RATE_4
            + (taxableIncome - brackets[3]) * RATE_5
        )

    return tax
print(computeTax("tax",55_000))