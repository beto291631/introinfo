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

# los programas inteligentes usan booleanos para tomar deciciones sobre si ejecutar lineas de codigo u omitirlas.
if True :
    print("hola")

activo = True
if activo == True:
    print("el usuario esta activo")
    activo = False
    num = 20 

cargado = False
if cargado :
    print("el celular esta cargado")

print("conecte el cargador ")

