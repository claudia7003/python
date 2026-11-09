#Recorrer un alista de frutas y mostrar cada fruta en mayúsculas

frutas = ["manzana", "banana", "cereza"]

for fruta in frutas:
    print(fruta.upper())

#Recorrrer una tupla de coordenadas y mostrar cada numero acompañado de un mensaje

cordenadas = (10, 20, 30)

for punto in cordenadas:
    print(f"El punto es: {punto}")

#Mostrar el nombre de cada producto y junto con su precio

precios = {
    "pan" : 1.2,
    "leche" : 0.9,
    "café" : 2.5
} 
for producto, precio in precios.items():
    print(f"{producto}: {precio} €")

#Recorrer las claves del diccionario y obtener sus precios

precios = {
    "pan" : 1.2,
    "leche" : 0.9,
    "café" : 2.5
} 
for producto, precio in precios.items():
    print(f"{producto}-> {precios[producto]} €")

#Recorrer unicamente los precios del diccionario.

precios = {
    "pan": 1.2,
    "leche": 0.9,
    "café": 2.5
}
for precio in precios.values():
    print(f"Precio: {precio} €")

#Recorrer una palabra y duplicar cada letra.

texto = "Python"
for letra in texto:
    print(letra * 2)