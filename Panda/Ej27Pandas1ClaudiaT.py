import os as pd

nombre_archivo = "Ej 27 Pandas Datos.xlsx"
nombre_hoja = "Alumnos"
datos = {}

excel = pd.ExcelFile(Ej 27 Pandas 1)

#Leer una hoja "Alumnos"
df = pd.read_excel(excel, sheet_name = nombre_hoja, index_col = None)

#Rellena los datos vacios fillna()
df = df.fillna("")
print(f"Tabla de leidos: {df}")

#Convertir el DataFrame a diccionario usando orient = "records"
datos[nombre_hoja] = df.to_dict(orient = "records")
print(datos)

#Recorre e imprime dato a dato con bucle for

for nombre_hoja in datos:
    print(f"Hoja: {nombre_hoja}")

    for alumno in datos[nombre_hoja]:

        for columna, dato in alumno.items():
            print(f"{columna} : {dato}")

