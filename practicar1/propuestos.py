#Escribe un programa que solicite al usuario dos números enteros y muestre la
#suma de ambos.
num1 = int(input ("Introduce el primer numero: "))
num2 = int(input ("Introduce el segundo numero: "))
print (f"La suma es {num1 + num2}")

#Escribe un programa que pida al usuario dos números reales (decimales) y
#calcule su suma.
num1 = float(input("Introduce el primer numero (decimal)"))
num2 = float(input ("Introduce el segundo numero (decimal)"))
print(f"La suma es {num1 + num2}")

#Crea un programa que pida dos números enteros y muestre el resultado de
#restar el segundo número al primero.
num1 = int(input("Introduce el primer numero"))
num2 = int(input("Introduce el segundo numero"))
print(f"La resta de el segundo numero menos el primero es {num2 - num1}")

#Realiza un programa que pida dos números enteros al usuario y devuelva el
#producto de ambos.
num1 = int(input("Introduce el primer numero"))
num2 = int(input("Introduce el segundo numero"))
print(f"El producto es {num1 % num2}" )

#Diseña un programa que solicite dos números reales y muestre el resultado
#de multiplicarlos entre sí
num1 = float(input("Introduce el primer numero (decimal)"))
num2 = float(input ("Introduce el segundo numero (decimal)"))
print(f"La multiplicación es {num1 * num2}")

#Pedir dos números enteros y hacer la división real
num1 = int(input ("Introduce el primer numero: "))
num2 = int(input ("Introduce el segundo numero: "))
print (f"La division es {num1 / num2}")

#Pedir dos números enteros y hacer la división entera
num1 = int(input ("Introduce el primer numero: "))
num2 = int(input ("Introduce el segundo numero: "))
print (f"La division es {num1 // num2}")

#Pedir dos números enteros y hacer el primer número módulo el segundo
#número.
num1 = int(input("Introduce el primer numero: "))
num2 = int(input("Introduce el segundo numero:"))
print(f"El modulo del segundo es {num2 % 2}" )

#Crea un programa que convierta metros a centímetros. El programa deberá
#pedir al usuario que introduzca una cantidad en metros y devolver la cantidad en
#centímetros.
metros = float(input("Introduce la cantidad en metros: "))
centimetros = metros * 100
print(f"{metros} metros equivalen a {centimetros} cm")

#Escribe un programa que calcule el área de un círculo. El programa deberá
#pedir al usuario que introduzca el radio del círculo y, utilizando la fórmula 
#Área = Pi * radio^2
import math
radio = float(input("Introduce el radio del circulo"))
area = Pi * (radio * radio)
print(f"El área del circulo es:{area} ")

#Escribe un programa que calcule el importe total a pagar en un restaurante. El
#programa deberá pedir al usuario el coste de la comida y el porcentaje de propina 
#que quiere dejar, y luego devolver el importe total
coste = float(input("Introduce el coste de la comida"))
propina = float(input("Introduce la cantidad de propina que quieres dejar"))
print(f"El importe total es: {coste + propina}")

#Crea un programa que calcule el IMC (Índice de Masa Corporal) del usuario.
#El programa deberá pedir al usuario su peso (en kilogramos) 
#y su altura (en metros), y luego calcular su IMC usando la fórmula: IMC = Peso / Altura^2
peso = float(input("Introduce tu peso en kg"))
altura = float(input("Introduce tu altura en metros"))
IMC = peso / altura * altura
print(f"Tu Indice de Masa Corporal es {IMC}")

#Escribe un programa que pida al usuario su nombre y su apellido, y luego
#imprima un mensaje de bienvenida que combine ambos.
nombre = input("Introduce tu nombre")
apellido = input ("Introduce tu apellido")
print(f"Hola! Bienvenido/a {nombre} {apellido} ")

#Meter en un match / case los ejercicios del 9 al 13, de forma que aparezca un
#menú con las 5 opciones para que el usuario decida que ejercicio o 
#enunciado quiere ejecutar.
def mostrarMenu():
    print("====MENU DE EJERCICIOS ====")
    print("9. Ejercicio 9")
    print("10. Ejercicio 10")
    print("11. Ejercicio 11")
    print("12. Ejercicio 12")
    print("13. Ejercicio 13")
    print("0. Salir")

    opcion = input("Introduce el numero del ejercicio")
    return opcion

opcion = mostrarMenu()

match opcion:
    case "9":
        print("El ejercicio 9 es:")
        metros = float(input("Introduce la cantidad en metros: "))
        centimetros = metros * 100
        print(f"{metros} metros equivalen a {centimetros} cm")
    case "10":
        print("El ejercicio 10 es:")
        #import math
        radio = float(input("Introduce el radio del circulo"))
        area = Pi * (radio * radio)
        print(f"El área del circulo es:{area} ")
    case "11":
        print("El ejercicio 11 es:")
        coste = float(input("Introduce el coste de la comida"))
        propina = float(input("Introduce la cantidad de propina que quieres dejar"))
        print(f"El importe total es: {coste + propina}")
    case "12":
        print("El ejercicio 12 es")
        peso = float(input("Introduce tu peso en kg"))
        altura = float(input("Introduce tu altura en metros"))
        IMC = peso / altura * altura
        print(f"Tu Indice de Masa Corporal es {IMC}")
    case "13":
        print("El ejercicio 13 es:")
        nombre = input("Introduce tu nombre")
        apellido = input ("Introduce tu apellido")
        print(f"Hola! Bienvenido/a {nombre} {apellido} ")
    case "0":
        print("Saliendo del programa....")
    case _:
        print("Opcion no valida")

#Añadir al ejercicio anterior una opción para salir del programa y un bucle del
#que sólo saldrá el programa cuando el usuario seleccione dicha opción de salida.ç
while True:
    print("====MENU DE EJERCICIOS ====")
    print("9. Ejercicio 9")
    print("10. Ejercicio 10")
    print("11. Ejercicio 11")
    print("12. Ejercicio 12")
    print("13. Ejercicio 13")
    print("0. Salir")

    opcion = input("Introduce el numero del ejercicio")
    

    

    match opcion:
        case "9":
            print("El ejercicio 9 es:")
            metros = float(input("Introduce la cantidad en metros: "))
            centimetros = metros * 100
            print(f"{metros} metros equivalen a {centimetros} cm")
        case "10":
            print("El ejercicio 10 es:")
            #import math
            radio = float(input("Introduce el radio del circulo"))
            area = Pi * (radio * radio)
            print(f"El área del circulo es:{area} ")
        case "11":
            print("El ejercicio 11 es:")
            coste = float(input("Introduce el coste de la comida"))
            propina = float(input("Introduce la cantidad de propina que quieres dejar"))
            print(f"El importe total es: {coste + propina}")
        case "12":
            print("El ejercicio 12 es")
            peso = float(input("Introduce tu peso en kg"))
            altura = float(input("Introduce tu altura en metros"))
            IMC = peso / altura * altura
            print(f"Tu Indice de Masa Corporal es {IMC}")
        case "13":
            print("El ejercicio 13 es:")
            nombre = input("Introduce tu nombre")
            apellido = input ("Introduce tu apellido")
            print(f"Hola! Bienvenido/a {nombre} {apellido} ")
        case "0":
            print("Saliendo del programa....")
        case _:
            print("Opcion no valida")