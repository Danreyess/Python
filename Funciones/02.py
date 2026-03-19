def calculate_tax(net_salary, tax = 0.13):
    tax_rate = (net_salary/100)*tax
    print(f"Tax rate: {tax_rate} of your salary {net_salary}")
    return tax_rate

calculate_tax(500)