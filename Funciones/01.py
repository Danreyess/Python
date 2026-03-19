#What is a function?
#In programming, a function is a reusable block of code that performs
#a specific action. Instead of writing the same code ten times, you
#write it once inside a def block and call it whenever u need it

def calculate_mean(data_list):
    total = sum(data_list)
    count = len(data_list)
    return total / count

#Using the function
scores = [80,90,100]
average = calculate_mean(scores)
print(f"The average is {average}")

def saludar_ingeniero(nombre):
    mensaje = f"Hola {nombre}, listo para procesar datos."
    return mensaje

#Asi la usas
print(saludar_ingeniero("Luis"))

def normalize_data(data):
    # 1. Get the min and max values
    minimum = min(data)
    maximum = max(data)

    # 2. Create the empty list to store results
    scaled_data = []

    # 3. Use a loop to process each number
    for x in data:
        normalized_value = (x - minimum) / (maximum - minimum)

        # We add the new value to our list
        scaled_data.append(normalized_value)

    # 4. Send the result back to the user
    return scaled_data

# --- HOW TO USE IT ---
prices = [200, 500, 900, 100, 400]

# We call the function and store its "return" in a new variable
clean_prices = normalize_data(prices)

print(clean_prices)

def calculate_tax(amount, tax_rate = 0.13): #We set a 'default' value
    return amount * tax_rate

salary = 4500
tax_to_pay = calculate_tax(salary)
net_salary = salary - tax_to_pay

print(f"Net salary: {net_salary}")