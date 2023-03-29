# while y el for
# un bucle WHILE repite su bucle de codigo mientras su condicion es True.
# para detener el bucle creamos una variable antes de crear el bucle
control = True

while control == True:
    print("hola mundo")

    control = False

print("se mostro una sola vez")

# para controlar las veces que se repite un bucle while comensamos con una variable establecida en un numero. llamamos a esta variable :contador:

contador = 1
while contador < 10 :
    print(contador)
    contador += 1

# calculo de interes compuesto
cuenta = 1000
interes = 0.11
annos = 3

print("monto inicial", cuenta)

contador = 1 

while contador <= annos:
    interes_compuesto = cuenta + interes
    cuenta += interes_compuesto
    cuenta +=100
    print("años: ",contador,": ", cuenta)
    contador += 1


# Hacer un programa que calcule la suma, resta, multiplicación y división de dos números ingresados por el usuario.

numero1 = int(input("ingrese un numero" ))
numero2 = int (input("ingrese otro numero"))
numero3 = int(input("ingrese otro numero"))
operacion = input("suma, resta, multiplicacion, divicion")
if operacion == "suma" :
    print(numero1 + numero2)

elif operacion == "resta":
    print(numero1 - numero2)

elif operacion == "multiplicacion":
    print(numero2 * numero1)

elif operacion == "divicion":
    print(numero3 / numero1)

# Hacer un programa que calcule el área y la circunferencia de un círculo.
pi = 3.14


diametro = float(input("Ingresa el diámetro: "))
circunferencia = diametro * pi
radio = diametro / 2
print(f"La circunferencia es {circunferencia} y el radio es {radio}")

# Hacer un programa que calcule el promedio de una lista de números ingresados por el usuario.


# Hacer un programa que determine si un número ingresado por el usuario es par o impar.
numero= int(input("ingrese un numero"))
if numero % 2 == 0:
    print("El número es par")
else:
    print("El número es impar")



# Hacer un programa que calcule la tabla de multiplicar de un número ingresado por el usuario.
numero = int(input("4"))
for f in range(1,11):
    print(f'4 x {f} = {4 * f}')



# Hacer un programa que cuente la cantidad de letras y números en un texto ingresado por el usuario.


# Hacer un programa que ordene una lista de números ingresados por el usuario en orden ascendente o descendente.