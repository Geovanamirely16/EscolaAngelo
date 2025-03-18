import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Criando matriz de correlação fictícia para as notas
notas_corr = np.array[
[1.00, 0.60, 0.45, 0.30, 0.50],
[0.60, 1.00, 0.55, 0.25, 0.65],
[0.45, 0.55, 1.00, 0.40, 0.60],
[0.30, 0.25, 0.40, 1.00, 0.35],
[0.50, 0.65, 0.60, 0.35, 1.00]
]

materias = ["Matemática", "Física", "Química", "História", "Português"]

plt.figure(figsize=(7,6))
sns.heatmap(notas_corr, annot=True, cmap="coolwarm", vmin=-1, vmax=1,
linewidths=0.5, fmt=".2f",
xticklabels=materias, yticklabels=materias)

plt.title("Correlação entre Notas de Alunos")
plt.savefig("heatmap_correlação_notas.tiff", format="tiff", dpi=300)
plt.show()