import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Criando uma matriz de correlação fictícia entre temperaturas ao longo do dia
temperatura_corr = np.array
([[1.00, 0.85, 0.65],
[0.85, 1.00, 0.75],
[0.65, 0.75, 1.00]
])

cidades = ["Cidade A", "Cidade B", "Cidade C"]

plt.figure(figsize=(6,5))
sns.heatmap(temperatura_corr, annot=True, cmap="coolwarm", vmin=-1,
vmax=1, linewidths=0.5, fmt=".2f",
xticklabels=cidades, yticklabels=cidades)

plt.title("Correlação das Temperaturas entre Cidades")
plt.savefig("heatmap_correlação_temperatura.tiff", format="tiff", dpi=300)
plt.show()