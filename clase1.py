# son 4 tipos de variables
# String
name=""
last_name= "Arauz"
# Integer
id=1234567890
# Float
cash=10,5
# Bool
active=True 

# comparaciones de las variables 
# como verificar si el pin ingresado por un usuario con su pin guardado 
entered_pin = 5448
expected_pin=5440
result = entered_pin== expected_pin
print(result)
# comparaciones con desigualdad. tenemos que usar el operador !=
result_1= 1!=2
print(result_1)
one = 1
two=2 
print("------------")
print(one==two)
print(one!= two)


# vamos a hacer un interrutor de luz inteligente que apague las luces si es de dia y las encienda si es de noche 
print("-----------")
is_day = False 
lights_on = not is_day

print("daytime?")
print(is_day)


print("linghts on")
print(lights_on)


# con las comparaciones vamos a hacer un codigo que trastree los datos de ventas de una tienda de pantalones
print("-----------------")
stock=600
jeans_sold=500
target=500

target_hit=jeans_sold==target
print("hit jeans sale target:")
print(target_hit)

current_stock= stock - jeans_sold
in_stock =current_stock !=0
print("jeans in stock:")
print(in_stock)
print(current_stock)


# podemos usar comparaciones para verificar si un numeros es mayor o menor que otro numero

print("------------")

print(2 < 200)
print(2 > 200)   

print(201 <= 200)
print(2 >= 200)

print("------------")

# comparaciones de cadenas de texto

my_answer = "lowr"
solution = "low"

print(my_answer == solution)
print(my_answer != solution)


# ejercicio de medidor de frecuencia cardiaca, usando comparaciones para verificar si la frecuencia cardiaca es demaciado alta o baja y le diremos al paciente si debe preocuparse.

print("-------------")

heart_rate = 77
too_low = heart_rate < 60
too_high = heart_rate > 100

print("heart rate high?")
print(too_high)

# practica de suma variable 1
lote1=100
lote2=200
lote3= lote1+lote2
print(lote3)

#   ejercicio 2
edad=18
result= edad >=18
print("es mayor de 18?")
print(result)

print("-------")
# usemos comparaciones de string para etiquetar los datos adquiridos atravez de la encuestas de usuarios de una aplicacion de fitnes.
# verificamos la respuesta de la encuesta de los usuarios con respecto ala frecuencia e intensidad de la actividad, las etiquetaremos y mostraremos los resultados.

frecuencia = "una vez ala semana"
intensidad = "Baja"

activo = frecuencia=="diaria"
print("el usuario es activo?")
print(activo)

intenso = intensidad == "alta"
print("el usuario es intenso")
print(intenso)

# ejercicio casa 1
# crear un algoritmo con el que agregue una variable un numero de celular con el formato xxxxxxxx, e imprimir mediante cadenas de texto el link para enviar a whatsapp.

numero_celular = input("Ingrese su número de celular sin espacios ni guiones: ")
numero_celular = 86200454 
texto_enlace_whatsapp = "https://wa.me/" + numero_celular
print("Este es el enlace para enviar un mensaje por WhatsApp:")
print(texto_enlace_whatsapp)

print("--------------")
# pruebas practica 1


# ejercicio numero 1 Escribir un programa que muestre por pantalla la cadena ¡Hola Mundo!.
print("¡hola mundo!")

# ejercicio 2 Escribir un programa que almacene la cadena ¡Hola Mundo! en una variable y luego muestre por pantalla el contenido de la variable.
mensaje="¡hola mundo!"
print(mensaje)

# Ejercicio 3

# Escribir un programa que almacene el nombre del usuario en la consola y después de que muestre por pantalla la cadena ¡Hola <nombre>!, donde <nombre> es el nombre que es el nombre del usuario.

nombre = input("Por favor ingresa tu nombre: ")
print(f"¡Hola {nombre}!")

# Ejercicio 4

# Escribir un programa que muestre por pantalla el resultado de la siguiente operación aritmética



# Ejercicio 5

# Escribir un programa que pregunte almacene el número de horas trabajadas y el coste por hora. Después debe mostrar por pantalla la paga que le corresponde.

horas_trabajadas= float(input("horas trabajadas:"))
coste_por_hora= float (input("coste por hora"))
paga = horas_trabajadas * coste_por_hora
print("La paga correspondiente es: $" + str(paga))


# Ejercicio 6

# Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), calcule el índice de masa corporal y lo almacene en una variable, y muestre por pantalla la frase Tu índice de masa corporal es <imc> donde <imc> es el índice de masa corporal calculado redondeado con dos decimales.

peso = float(input("ingrese su peso en kg"))
estatura = float(input("ingrese estatura en metros"))
imc = peso / (estatura**2)
print("Tu índice de masa corporal es: " + "{:.2f}".format(imc))