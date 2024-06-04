import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Ler os dados do arquivo Excel
df = pd.read_excel(r"C:\Users\Ana Carolina Padilha\OneDrive\Área de Trabalho\caso.csv\caso (4).xlsx")

# Configurar o estilo seaborn
sns.set(style="whitegrid")

# Criar o boxplot
plt.figure(figsize=(10, 6))
sns.boxplot(data=df, y='deaths')
plt.ylabel('Número de mortes')
plt.title('Boxplot Número de mortes')
plt.tight_layout()

# Mostrar o boxplot
plt.show()
