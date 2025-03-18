import numpy as np

A = np.array([[2,3], [4,1]])

B = np.array([8,7])

solucao = np.linalg.solve(A, B)

print(f"\nSolucões para x e y: {solucao}\n")
