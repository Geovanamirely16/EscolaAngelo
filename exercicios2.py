import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Criando os dados: Notas dos alunos em diferentes matérias
materias = ["Matemática", "Física", "Química", "História", "Português"]
alunos = ["Aluno 1", "Aluno 2", "Aluno 3", "Aluno 4", "Aluno 5"]
notas = np.array([
[7, 6, 8, 5, 9],
[5, 7, 6, 8, 7],
[9, 8, 7, 6, 8],
[6, 5, 8, 7, 6],
[8, 9, 7, 6, 5]
])

# Criando o heatmap
plt.figure(figsize=(8, 5))
sns.heatmap(notas, annot=True, cmap="coolwarm", xticklabels=materias,
yticklabels=alunos)

# Configuração do gráfico
plt.title("Notas de Alunos em Diferentes Matérias")
plt.xlabel("Matérias")
plt.ylabel("Alunos")

# Salvando o gráfico em .tiff
plt.savefig("heatmap_notas.tiff", format="tiff", dpi=300)

# Exibindo o gráfico
plt.show()