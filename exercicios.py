import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Criando os dados: Temperatura ao longo do dia em 3 cidades
horarios = ["06h", "09h", "12h", "15h", "18h", "21h"]
cidades = ["Cidade A", "Cidade B", "Cidade C"]
temperaturas = np.array([
[15, 18, 25, 30, 27, 20], # Cidade A
[12, 17, 24, 29, 25, 18], # Cidade B
[10, 14, 22, 26, 23, 16] # Cidade C
])

# Criando o heatmap
plt.figure(figsize=(8, 5))
sns.heatmap(temperaturas, annot=True, cmap="coolwarm&quot",
xticklabels=horarios, yticklabels=cidades)

# Configuração do gráfico
plt.title("Temperatura ao Longo do Dia&quot")
plt.xlabel("Horários")
plt.ylabel("Cidades")

# Salvando o gráfico em .tiff

plt.savefig("heatmap_temperatura.tiff", format="tiff", dpi=300)

# Exibindo o gráfico
plt.show()