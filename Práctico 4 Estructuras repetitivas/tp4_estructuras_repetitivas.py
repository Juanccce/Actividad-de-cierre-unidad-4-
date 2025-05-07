
# TP4 - Estructuras Repetitivas
# [Juan Galati]

# 1) Imprimir todos los números enteros desde 0 hasta 100 (uno por línea)
print("Ejercicio 1:")
for i in range(101):
    print(i)

# 2) Determinar la cantidad de dígitos de un número ingresado por el usuario
print("\nEjercicio 2:")
numero = int(input("Ingrese un número entero: "))
contador = len(str(abs(numero)))
print("Cantidad de dígitos:", contador)

# 3) Sumar todos los números enteros entre dos valores (excluyendo los extremos)
print("\nEjercicio 3:")
a = int(input("Ingrese el primer número: "))
b = int(input("Ingrese el segundo número: "))
if a > b:
    a, b = b, a
suma = 0
for i in range(a + 1, b):
    suma += i
print("La suma es:", suma)

# 4) Sumar números ingresados hasta que el usuario ingrese un 0
print("\nEjercicio 4:")
suma = 0
while True:
    numero = int(input("Ingrese un número (0 para terminar): "))
    if numero == 0:
        break
    suma += numero
print("Suma total:", suma)

# 5) Juego de adivinanza de número aleatorio entre 0 y 9
print("\nEjercicio 5:")
import random
numero_secreto = random.randint(0, 9)
intentos = 0
while True:
    intento = int(input("Adivina el número (entre 0 y 9): "))
    intentos += 1
    if intento == numero_secreto:
        break
print(f"¡Correcto! Lo adivinaste en {intentos} intento(s).")

# 6) Imprimir números pares entre 0 y 100 en orden decreciente
print("\nEjercicio 6:")
for i in range(100, -1, -1):
    if i % 2 == 0:
        print(i)

# 7) Sumar todos los números entre 0 y un número positivo ingresado
print("\nEjercicio 7:")
n = int(input("Ingrese un número entero positivo: "))
suma = sum(range(n + 1))
print("La suma es:", suma)

# 8) Ingresar 100 números e indicar cuántos son pares, impares, positivos y negativos
print("\nEjercicio 8:")
pares = impares = positivos = negativos = 0
for _ in range(100):
    num = int(input("Ingrese un número: "))
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1
    if num > 0:
        positivos += 1
    elif num < 0:
        negativos += 1
print("Pares:", pares)
print("Impares:", impares)
print("Positivos:", positivos)
print("Negativos:", negativos)

# 9) Calcular la media de 100 números ingresados
print("\nEjercicio 9:")
suma = 0
for _ in range(100):
    num = int(input("Ingrese un número: "))
    suma += num
media = suma / 100
print("La media es:", media)

# 10) Invertir los dígitos de un número ingresado
print("\nEjercicio 10:")
numero = int(input("Ingrese un número: "))
invertido = int(str(abs(numero))[::-1])
if numero < 0:
    invertido = -invertido
print("Número invertido:", invertido)
