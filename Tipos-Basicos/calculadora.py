n1 = input("Ingresa primer numero:")
n2 = input("Ingresa segundo numero:")

n1 = int(n1)
n2 = int(n2)

suma = n1 + n2
resta = n1 - n2
multiplicar = n1 * n2
dividir = n1 / n2

mensaje = f"""
Para el resultado de la suma es: {suma}
Para el resultado de la resta es: {resta}
Para el resultado de la multiplicacion es: {multiplicar}
Para el resultado de la dividir es: {dividir}
"""

print(mensaje)