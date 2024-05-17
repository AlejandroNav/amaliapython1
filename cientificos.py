# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# Importando módulos
import pandas as pd
import matplotlib.pyplot as plt
import statistics as st
import scipy.stats as sp
import seaborn as sns
import warnings

# Desactivar advertencias de Seaborn
warnings.filterwarnings("ignore")

# Adquiere los datos desde un archivo csv usando biblioteca PANDAS
dataframe = pd.read_csv('salario-ciencias.csv')  # Reemplaza con la ruta correcta
x = dataframe['salario']

# Muestra resultados en consola
print("==============================\n")
print(" \nAnálisis de salarios de cientifico de Datos Amalia soto")
print(" \n<< Datos de entrada >>")
print(sorted(x))
print(" \n<< Resultados obtenidos >>\n")

# Medidas de centralidad
print('Media:', st.mean(x))
print('Mediana:', st.median(x))

# Medidas de dispersión
print('Varianza: ', st.variance(x))
print('Desviación Estandar: ', st.stdev(x))

# Asimetría y curtosis
print("Asimetría", sp.skew(x,bias=True))  
print("Curtosis",sp.kurtosis(x,fisher=True))
print("==============================\n\n\n")

# Gráfica de caja y bigote
plt.figure(figsize=(16, 5))  # Crea una nueva figura con un tamaño especificado de 16 pulgadas de ancho y 5 pulgadas de alto.
sns.boxplot(x=x, color='coral')  # Crea la gráfica de caja y bigote usando los datos en x y colorea de azul claro.
plt.xlabel('Salarios de Científicos de Datos')  # Etiqueta del eje x
plt.title('Gráfica de Caja y Bigote de los Salarios de Científicos de Datos')  # Añade un título a la gráfica
sns.swarmplot(x=x, color='crimson')  # Superpone una gráfica de dispersión sobre la gráfica de caja y bigote con puntos rojos oscuros


# Histograma y curva de densidad
plt.figure(figsize=(10, 5))
sns.histplot(x, kde=True, bins=11, edgecolor='blue', color='coral')
plt.xlabel('Salarios')
plt.ylabel('Frecuencia')
plt.axvline(st.mean(x), color='red', linestyle='--', label=f'Media: {st.mean(x):.2f}')
plt.legend()
plt.title('Histograma y Curva de Densidad de los Salarios de Cientificos de Datos')

# Mostrar las gráficas
plt.show()