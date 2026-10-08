#Escribe un programa en Python que inicialice una lista llamadafrutas con los
#elementos"manzana" ,"platano" y"naranja" .

frutas = ["manzanas" , "platanos" , "naranjas"]

opcion = 0

while opcion != 0:
    print("==== MENÚ ====")
    print("1. Muestra la lista completa por pantalla.")
    print("2. Ver un elemento por índice")
    print("3. Añade un elemento")
    print("4. Modifica el elemento")
    print("5. Borra un elemento")
    print("6. Salir")

    menu = int(input("Elige una opción: "))
    match menu:
        case 1:
            print("Mostrando lista completa")
            print(frutas)
           
        case 2:
            indice = int(input("Introduce el índice: "))

            if indice >= 0 and indice < len(frutas):
                print("La fruta es:", frutas[indice])
            else:
                print("Índice no válido")
          
        case 3:
            print("Introduce una nueva fruta:")
            frutas.append(frutas)
            print ("Fruta añadida correctamente")
           
        case 4:
            indice = int(print("Introduzca la posición que quiere cambiar"))
            if indice >= 0 and indice < len(frutas):
                nueva_fruta = input("Introduce el nuevo nombre: ")
                frutas[indice] = nueva_fruta

                print("Fruta modificada correctamente")
            else:
                print("Índice no válido")
            
        case 5:
            indice = int(input("Introduce el índice que quieres borrar: "))

            if indice >= 0 and indice < len(frutas):
                frutas.pop(indice)

                print("Fruta borrada correctamente")
            else:
                print("Índice no válido")
        case 6:
            print("Saliendo del programa...")
            break;
        case _:
            print("Opción no valida")
    
