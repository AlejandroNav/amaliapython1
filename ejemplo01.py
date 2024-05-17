# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# Importando módulos
import pandas as pd
import matplotlib.pyplot as plot
import statistics as st
import scipy.stats as sp
import seaborn as sns

#Adquiere los datos desde un archivo csv usando biblioteca PANDAS
dataframe = pd.read_csv('salarios-pedagogo.csv')
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
print("Curtosis",sp.kurtosis(x,fisher=True,))
print("==============================\n\n\n")

# Gráfica de caja y bigote
sns.boxplot(x);
plot.xlabel('Salarios')
sns.swarmplot(x, color='r')

# Histograma y curva de densidad
sns.displot(x, kde=True, bins=11)
plot.xlabel('Salarios')
plot.ylabel('Frecuencia')
plot.axvline(st.mean(x), color='red', linestyle='--')
plot.show


