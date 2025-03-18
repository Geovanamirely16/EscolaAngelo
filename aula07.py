import numpy as np

v1 = np.array([20,0])
v2 = np.array([0,5])

velocidade = v1 + v2
print(velocidade)

escalar = 2
v2_dobro = escalar * 2
velocidade_dobro = v1 + v2_dobro
print(velocidade_dobro)

produto_escalar = np.dot(v1 , v2)
print(produto_escalar)

v1_3D = np.array([20, 0, 0])
v2_3D = np.array([0, 5, 0])
produto_vetorial = np.cross(v1_3D, v2_3D)
print(produto_vetorial)