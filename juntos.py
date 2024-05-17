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

# Adquiere los datos desde archivos csv usando biblioteca PANDAS
df_cientificos = pd.read_csv('salario-ciencias.csv')  # Reemplaza con la ruta correcta
df_pedagogos = pd.read_csv('salarios-pedagogo.csv')   # Reemplaza con la ruta correcta

# Datos
x_cientificos = df_cientificos['salario']
x_pedagogos = df_pedagogos['salario']

# Mostrar resultados en consola para Científicos de Datos
print("==============================\n")
print(" \nAnálisis de salarios de científico de Datos Amalia Soto")
print(" \n<< Datos de entrada >>")
print(sorted(x_cientificos))
print(" \n<< Resultados obtenidos >>\n")

# Medidas de centralidad para Científicos de Datos
print('Media:', st.mean(x_cientificos))
print('Mediana:', st.median(x_cientificos))

# Medidas de dispersión para Científicos de Datos
print('Varianza: ', st.variance(x_cientificos))
print('Desviación Estandar: ', st.stdev(x_cientificos))

# Asimetría y curtosis para Científicos de Datos
print("Asimetría", sp.skew(x_cientificos, bias=True))  
print("Curtosis", sp.kurtosis(x_cientificos, fisher=True))
print("==============================\n\n\n")

# Mostrar resultados en consola para Pedagogos
print("==============================\n")
print(" \nAnálisis de salarios de pedagogos")
print(" \n<< Datos de entrada >>")
print(sorted(x_pedagogos))
print(" \n<< Resultados obtenidos >>\n")

# Medidas de centralidad para Pedagogos
print('Media:', st.mean(x_pedagogos))
print('Mediana:', st.median(x_pedagogos))

# Medidas de dispersión para Pedagogos
print('Varianza: ', st.variance(x_pedagogos))
print('Desviación Estandar: ', st.stdev(x_pedagogos))

# Asimetría y curtosis para Pedagogos
print("Asimetría", sp.skew(x_pedagogos, bias=True))  
print("Curtosis", sp.kurtosis(x_pedagogos, fisher=True))
print("==============================\n\n\n")

# Crear subplots para las gráficas de caja y bigote
fig, axs = plt.subplots(2, 1, figsize=(10, 10))

# Establecer límites de los ejes para garantizar la misma escala
limites_x = [min(x_cientificos.min(), x_pedagogos.min()), max(x_cientificos.max(), x_pedagogos.max())]

# Gráfica de caja y bigote para Científicos de Datos
sns.boxplot(x=x_cientificos, color='coral', ax=axs[0])
sns.swarmplot(x=x_cientificos, color='crimson', ax=axs[0])
axs[0].set_xlim(limites_x)
axs[0].set_xlabel('Salarios de Científicos de Datos')
axs[0].set_title('Gráfica de Caja y Bigote de los Salarios de Científicos de Datos')

# Gráfica de caja y bigote para Pedagogos
sns.boxplot(x=x_pedagogos, color='lightgreen', ax=axs[1])
sns.swarmplot(x=x_pedagogos, color='darkgreen', ax=axs[1])
axs[1].set_xlim(limites_x)
axs[1].set_xlabel('Salarios de Pedagogos')
axs[1].set_title('Gráfica de Caja y Bigote de los Salarios de Pedagogos')

# Ajustar el layout
plt.tight_layout()
plt.show()

# Crear subplots para los histogramas
fig, axs = plt.subplots(2, 1, figsize=(10, 10))

# Establecer límites de los ejes para garantizar la misma escala
limites_y_hist = [0, max(x_cientificos.value_counts().max(), x_pedagogos.value_counts().max())]

# Histograma y curva de densidad para Científicos de Datos
sns.histplot(x_cientificos, kde=True, bins=11, edgecolor='blue', color='coral', ax=axs[0])
axs[0].axvline(st.mean(x_cientificos), color='red', linestyle='--', label=f'Media: {st.mean(x_cientificos):.2f}')
axs[0].set_xlim(limites_x)
axs[0].set_ylim(limites_y_hist)
axs[0].set_xlabel('Salarios')
axs[0].set_ylabel('Frecuencia')
axs[0].legend()
axs[0].set_title('Histograma y Curva de Densidad de los Salarios de Científicos de Datos')

# Histograma y curva de densidad para Pedagogos
sns.histplot(x_pedagogos, kde=True, bins=11, edgecolor='blue', color='lightgreen', ax=axs[1])
axs[1].axvline(st.mean(x_pedagogos), color='red', linestyle='--', label=f'Media: {st.mean(x_pedagogos):.2f}')
axs[1].set_xlim(limites_x)
axs[1].set_ylim(limites_y_hist)
axs[1].set_xlabel('Salarios')
axs[1].set_ylabel('Frecuencia')
axs[1].legend()
axs[1].set_title('Histograma y Curva de Densidad de los Salarios de Pedagogos')

# Ajustar el layout
plt.tight_layout()
plt.show()
