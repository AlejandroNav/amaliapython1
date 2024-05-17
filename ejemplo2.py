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
dataframe = pd.read_csv('salarios-pedagogo.csv')  # Reemplaza con la ruta correcta
x = dataframe['salario']

# Muestra resultados en consola
print("==============================\n")
print(" \nAnálisis de salarios de pedagogo")
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
plt.figure(figsize=(10, 5))
sns.boxplot(x=x)
plt.xlabel('Salarios')
plt.title('Gráfica de Caja y Bigote de los Salarios de Pedagogo')
sns.swarmplot(x=x, color='r')

# Histograma y curva de densidad
plt.figure(figsize=(10, 5))
sns.histplot(x, kde=True, bins=11)
plt.xlabel('Salarios')
plt.ylabel('Frecuencia')
plt.axvline(st.mean(x), color='red', linestyle='--', label=f'Media: {st.mean(x):.2f}')
plt.legend()
plt.title('Histograma y Curva de Densidad de los Salarios de Pedagogo')

# Mostrar las gráficas
plt.show()