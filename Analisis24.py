# Importando módulos
import pandas as pd
import matplotlib.pyplot as plt
import statistics as st
import scipy.stats as sp
import seaborn as sns

# Adquiere los datos desde archivos csv usando PANDAS
df_amalia = pd.read_csv('pasos-amalia.csv')  
df_alvaro = pd.read_csv('pasos-alvaro.csv') 

# Sacar los datos para Amalia y Alvaro del cvs en un df
datos_amalia = df_amalia['pasos']
datos_alvaro = df_alvaro['Pasos']

print(" \nAnálisis de pasos de Amalia y Alvaro \n")
print("==========\n")
# Medidas de centralidad para Amalia
print('Media Amalia:', st.mean(datos_amalia))
print('Mediana Amalia:', st.median(datos_amalia))
print("-----------\n")
# Medidas de dispersión para Amalia
print('Varianza Amalia: ', st.variance(datos_amalia))
print('Desviación Estandar Amalia: ', st.stdev(datos_amalia))
print("-----------\n")
# Asimetría y curtosis para Amalia  
print("Asimetría Amalia:", sp.skew(datos_amalia, bias=True))
print("Curtosis Amalia:", sp.kurtosis(datos_amalia, fisher=True))
print("-----------\n")
# Medidas de centralidad para Alvaro
print('Media Alvaro:', st.mean(datos_alvaro))
print('Mediana Alvaro:', st.median(datos_alvaro))
print("-----------\n")
# Medidas de dispersión para Alvaro
print('Varianza Alvaro: ', st.variance(datos_alvaro))
print('Desviación Estandar Alvaro: ', st.stdev(datos_alvaro))
print("-----------\n")
# Asimetría y curtosis para Alvaro
print("Asimetría Alvaro:", sp.skew(datos_alvaro, bias=True))
print("Curtosis Alvaro:", sp.kurtosis(datos_alvaro, fisher=True))
print("==============================\n")

# Crear histogramas de los pasos caminados
plt.figure(figsize=(16, 5))

# Histograma de Amalia
plt.subplot(1, 2, 1)
sns.histplot(datos_amalia, kde=True, color='blue')
plt.title('Histograma de Pasos de Amalia')
plt.xlabel('Pasos')
plt.ylabel('Frecuencia')

# Histograma de Alvaro
plt.subplot(1, 2, 2)
sns.histplot(datos_alvaro, kde=True, color='green')
plt.title('Histograma de Pasos de Alvaro')
plt.xlabel('Pasos')
plt.ylabel('Frecuencia')

plt.tight_layout()
plt.show()

# Diagrama de caja y bigotes de Amalia con puntos en rojo
plt.figure(figsize=(8, 5))
sns.boxplot(x=datos_amalia, color='blue')
sns.swarmplot(x=datos_amalia, color='red', ax=plt.gca())
plt.title('Diagrama de Caja y Bigotes de Pasos de Amalia')
plt.xlabel('Pasos')
plt.tight_layout()
plt.show()

# Diagrama de caja y bigotes de Álvaro con puntos en rojo
plt.figure(figsize=(8, 5))
sns.boxplot(x=datos_alvaro, color='green')
sns.swarmplot(x=datos_alvaro, color='red', ax=plt.gca())
plt.title('Diagrama de Caja y Bigotes de Pasos de Álvaro')
plt.xlabel('Pasos')
plt.tight_layout()
plt.show()

# Crear una figura para los diagramas de caja y bigotes en la misma escala, en formato horizontal
# Crear un DataFrame con los datos de ambos grupos
datos_combinados = pd.DataFrame({
    'Pasos': pd.concat([datos_amalia, datos_alvaro]),
    'Persona': ['Amalia'] * len(datos_amalia) + ['Álvaro'] * len(datos_alvaro)
})

plt.figure(figsize=(10, 5))

# Diagrama de caja y bigotes de ambos datasets en horizontal
sns.boxplot(x='Pasos', y='Persona', data=datos_combinados, palette=['blue', 'green'])
sns.swarmplot(x='Pasos', y='Persona', data=datos_combinados, color='red')

# Añadir etiquetas y título
plt.title('Diagrama de Caja y Bigotes de Pasos de Amalia y Álvaro en la Misma Escala')
plt.xlabel('Pasos')
plt.ylabel('Personas')

# Crear un gráfico de líneas para mostrar el registro diario de pasos
plt.figure(figsize=(14, 7))

# Gráfico de líneas de Amalia
plt.subplot(2, 1, 1)
df_amalia['pasos'].plot(kind='bar', color='blue')
plt.title('Registro Diario de Pasos de Amalia')
plt.xlabel('Fecha')
plt.ylabel('Pasos')

# Gráfico de líneas de Álvaro
plt.subplot(2, 1, 2)
df_alvaro['Pasos'].plot(kind='bar', color='green')
plt.title('Registro Diario de Pasos de Álvaro')
plt.xlabel('Fecha')
plt.ylabel('Pasos')





plt.tight_layout()
plt.show()
