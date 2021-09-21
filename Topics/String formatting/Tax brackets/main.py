income = int(input())
percent = (0, 15, 25, 28)
income_limits = (15528, 42708, 132407)


def count_tax(income_money, tax_percent):
    calculated_tax = round(income_money * tax_percent / 100)
    print(f'The tax for {income_money} is {tax_percent}%. That is {calculated_tax} dollars!')


if income < income_limits[0]:
    count_tax(income, percent[0])
elif income < income_limits[1]:
    count_tax(income, percent[1])
elif income < income_limits[2]:
    count_tax(income, percent[2])
else:
    count_tax(income, percent[3])
