import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from pandas import *


# Carregar dados do arquivo Excel
df = pd.read_excel(r"C:\Users\Ana Carolina Padilha\OneDrive\Área de Trabalho\caso.csv\caso (4).xlsx")

# Análise Descritiva
descricao = df[['confirmed', 'deaths']].describe()
print(descricao)

# Gráfico de Dispersão
plt.figure(figsize=(10, 8))
plt.scatter(df['confirmed'], df['deaths'], color='blue', alpha=0.5)
plt.xlabel('Número de Casos')
plt.ylabel('Número de Mortes')

# Aplicação da Regressão Linear Simples com NumPy
X = df['confirmed']
y = df['deaths']

# Calcular os coeficientes da regressão linear com NumPy
X_mean = np.mean(X)
y_mean = np.mean(y)
numerator = np.sum((X - X_mean) * (y - y_mean))
denominator = np.sum((X - X_mean) ** 2)
coef_angular = numerator / denominator
intercepto = y_mean - coef_angular * X_mean

# Prever os valores de y (mortes) usando a equação da linha de regressão
y_pred = intercepto + coef_angular * X

# Plotar a linha de regressão
plt.plot(X, y_pred, color='red', linewidth=2, label='Linha de Regressão')
plt.scatter([], [], color='blue', label='Dias do mês')
plt.legend()
plt.title('Regressão Linear Simples - Cidade de Fortaleza 2020 e 2021 - Número de casos x Número de mortes')
plt.grid(False)
plt.tight_layout()
plt.show()

print(f'Coeficiente Angular: {coef_angular}')
print(f'Intercepto: {intercepto}')
# Calcular os coeficientes da regressão linear com NumPy
X_mean = np.mean(X)
y_mean = np.mean(y)
numerator = np.sum((X - X_mean) * (y - y_mean))
denominator = np.sum((X - X_mean) ** 2)
coef_angular = numerator / denominator
intercepto = y_mean - coef_angular * X_mean

# Prever os valores de y (mortes) usando a equação da linha de regressão
y_pred = intercepto + coef_angular * X

# Plotar a linha de regressão
plt.plot(X, y_pred, color='red', linewidth=2, label='Linha de Regressão')
plt.scatter([], [], color='blue', label='Dias do mês')
plt.legend()
plt.title('Regressão Linear Simples - Cidade de Fortaleza  - Número de casos x Número de mortes')
plt.grid(False)
plt.tight_layou
plt.show()

print(f'Coeficiente Angular: {coef_angular}')
print(f'Intercepto: {intercepto}')

contagem_deaths = df['deths'].value_counts()

