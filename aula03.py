import numpy as np

A = np.array([[2, 4, 6], [1, 3, 5], [7, 8, 9]])
B = np.array([[1, 0, 2], [4, 3, 1], [5, 6, 7]])

soma = A + B
print(f"\nEstoque total (A + B)\n{soma}\n")

sub = A - B
print(f"\nDiferença de estoque (A - B)\n{sub}\n")

C = np.array([[1, 2], [3, 4], [5, 6]])
D = np.array([[7, 8], [9, 10]])

mult = np.dot(C, D)
print(f"\nReceita total das vendas (C * D)\n{mult}\n")
