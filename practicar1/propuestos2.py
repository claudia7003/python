#Añade al ejercicio anterior un control de errores o control de excepciones con
#try/except, incluye reglas de negocio con raise, por ejemplo una distancia en metros no
#puede ser negativa y las excepciones de ValueError y ZeroDivisionError.

opcion = 0

while opcion != 0:

    print("\n--- MENÚ ---")
    print("9. Ejercicio 9")
    print("10. Ejercicio 10")
    print("11. Ejercicio 11")
    print("12. Ejercicio 12")
    print("13. Ejercicio 13")
    print("0. Salir")

    try:
        opcion = int(input("Elige una opción: "))

        match opcion:

            case 9:
                print("Aquí va el ejercicio 9")

            case 10:
                print("Aquí va el ejercicio 10")

            case 11:
                print("Aquí va el ejercicio 11")

            case 12:
                distancia = float(input("Introduce una distancia en metros: "))

                if distancia < 0:
                    raise ValueError("La distancia no puede ser negativa")

                print("La distancia es:", distancia, "metros")

            case 13:
                nombre = input("Introduce tu nombre: ")
                apellido = input("Introduce tu apellido: ")

                print("Bienvenido", nombre, apellido)

            case 0:
                print("Hasta luego")

            case _:
                print("Opción no válida")

    except ValueError:
        print("Error: debes introducir un número válido")

    except ZeroDivisionError:
        print("Error: no se puede dividir entre cero")