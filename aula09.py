import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Dados de exemplo
preco = np.array([10,15,20,25,30,35,40])
vendas = np.array([100,90,80,60,50,30,20])

preco = preco.reshape(-1,1)

modelo = LinearRegression()
modelo.fit(preco, vendas)

previsao = modelo.predict(preco)

# Visualização grafica
plt.scatter(preco, vendas, color='Blue', label="Dados reais")
plt.plot(preco, previsao, color='red', linewidth=2, label='Modelo linear')
plt.title('Relação entre preço e vendas')
plt.xlabel('Preço do produto')
plt.ylabel('Vendas mensais')
plt.legend()
plt.grid(True)
plt.show()
