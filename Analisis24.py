import pandas as pd
import statistics as st
import matplotlib.pyplot as plt

# Importando módulos

# Crear un DataFrame a partir de un diccionario
dataInventada = {
    'Nombre': ['Ana', 'Juan', 'María', 'Pedro', 'Luis', 'Jorge', 'Carlos','Magali'],
    'Edad': [23, 34, 29, 40, 33, 28, 25, 30],
    'Ciudad': ['Sidney', 'Londres', 'Tokyo', 'Paris','Londres', 'Londres', 'Londres', 'Londres']
}

miDataFrame = pd.DataFrame(dataInventada)

print(miDataFrame)
print("\n")
print(miDataFrame['Edad'])
print("\n")
print(miDataFrame[miDataFrame['Edad'] > 30])

listaEdades = miDataFrame['Edad'].tolist()
print("\n")
print(listaEdades)

media_edades = st.mean(listaEdades)
print("\n")
print(f'La media de la edad es: {media_edades}')