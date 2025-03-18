import numpy as np 

F = np.array ([[2,4], [3,9]])

determinante = np.linalg.det(F)

if determinante != 0:
  inverta = np.linalg.inv(F)
  print(f"\nMatriz inversa de F = \n(inversa)\n ")
else:
  print("A matriz F não é inversível")
  