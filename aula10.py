import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from mpl_toolkits.mplot3d import Axes3D

# Dados de exemplo
area = np.array([50,60,80,100,120,150,180])
quartos = np.array([1,2,2,3,3,4,4])
preco = np.array([200000, 240000, 310000, 360000, 400000, 500000])

# Criar matriz de variedades independentes
x = np.column_stack((area, quartos))

# Criar e treinar o modelo de regressão linear
modelo = LinearRegression()
modelo.fit(x, preco)

# Previsão usando o modelo treinado
previsao = modelo.predict(x)

# visualização grafica
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(area, quartos, preco, color='green', label='Dados reais')
ax.plot_trisurf(area, quartos, previsao, color='red', alpha=0.1, label='Plano ajustado')
ax.set_title('Relacão entre Area. Numero de Quartos e Preco de Venda')
ax.set_xlabel('Area (m²)')
ax.set_ylabel('Numero de Quartos')
ax.set_zlabel('Preço de Venda(R$)')
plt.legend()
plt.show()