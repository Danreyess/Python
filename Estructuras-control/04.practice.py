#Tenga una lista de numeros por ejemplo([10,50,120,80,200])
#Use un ciclo for para recorrerla
#Use un if para imprimir solo los numeros que sean mayores a 100

# temperatura = [10,50,120,80,200]
# for temp in temperatura:
#     if temp > 100:
#         print(f"El numero es mayor que 100 {temp}")


# Reto 1: El Validador de Datos (Uso de while e if)
# En ingeniería de datos, a veces recibes datos basura. Imagina que estás pidiendo la temperatura de un reactor, pero solo aceptas valores entre 0 y 100.
# Tu tarea:
# Usa un ciclo while para pedir un número infinitamente.
# Si el número es -1, el programa debe detenerse (break).
# Si el número está fuera del rango (menor a 0 o mayor a 100), imprime "Dato inválido".
# Si es válido, imprime "Dato registrado".

# while True:
#     n1 = int(input("Introduce un numero:"))
#     if n1 == -1:
#         break
#     elif n1 > 100 or n1 < 0:
#         print(f"Dato invalido: {n1}")
#     else:
#         print(f"Data registrado: {n1}")


# Reto 2 (El Contador)
# Este es clave para tu carrera de Data Science. En lugar de solo imprimir, vas a almacenar información en variables mientras el ciclo corre.
# Aquí tienes la lista para copiar y pegar:
# scores = [0.2, 0.8, 0.9, 0.4, 0.5, 0.95, 0.1]
# Tu misión:
# Declara dos variables: buenos = 0 y malos = 0.
# Recorre la lista con un for.
# Si el score es mayor a 0.7, suma 1 a buenos.
# Si no, suma 1 a malos.
# Al final (fuera del for), imprime cuántos hubo de cada uno.

scores = [0.2, 0.8, 0.9, 0.4, 0.5, 0.95, 0.1]
buenos = 0
malos = 0
for score in scores:
    if score > 0.7:
        buenos += 1
    else:
        malos += 1
print(buenos)
print(malos)
