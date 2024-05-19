import pandas as pd

# Crear un DataFrame a partir de un diccionario
data = {
    'Nombre': ['Ana', 'Juan', 'María', 'Pedro'],
    'Edad': [23, 34, 29, 40],
    'Ciudad': ['Madrid', 'Barcelona', 'Valencia', 'Sevilla']
}

df = pd.DataFrame(data)

# Mostrar el DataFrame
print(df)
print("==============================\n")
# Seleccionar una columna
print(df['Edad'])
print("==============================\n")
# Filtrar filas donde la edad es mayor de 30
print(df[df['Edad'] > 30])
print("==============================\n")
# Agregar una nueva columna
df['Puntaje'] = [85, 90, 95, 80]
print(df)
print("==============================\n")
# Guardar el DataFrame en un archivo CSV
df.to_csv('datos.csv', index=False)