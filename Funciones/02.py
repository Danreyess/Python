def calculate_tax(net_salary, tax = 0.13):
    tax_rate = (net_salary/100)*tax
    print(f"Your salary is {net_salary}, your tax rate is {tax_rate}.")
    return tax_rate

calculate_tax(1500)