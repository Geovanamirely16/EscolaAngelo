# Dados quantitativos: vendas semanais
vendas_semanais = [150, 200, 250, 300, 400, 300, 420]

# Dados qualitativos: feedback de clientes
feedbacks = [
  "Produto fácil de usar, mas caro.",
  "Excelente desempenho, mas design fraco.",
  "Muito satisfeito com a qualidade.",
  "É muito caro, porém bom desempenho, boa Qualidade"]

# Analisando os dados quantitativos: crescimento de vendas
crescimento = [(vendas_semanais[i] - vendas_semanais[i-1]) / vendas_semanais[i-1] * 100 for i in range(1, len(vendas_semanais))]
media_crescimento = sum(crescimento) / len(crescimento)

print()
print(f"\nCrescimento semanal das vendas: \n{crescimento}\n")
print(f"Crescimento médio das vendas: {media_crescimento}")
print()

# Analisando os dados qualitativos: Identificando recorrencias
from collections import Counter

#Palavras-chave que pode indicar temas recorrentes
keywords = ["caro", "desempenho", "qualidade", "fraco"]

#Contando a frequência das palavras-chave nos feedbacks
temas_relevantes = Counter()

for feedback in feedbacks:
  for palavra in feedback.split():
    if palavra.lower().strip(".,") in keywords:
      temas_relevantes[palavra.lower().strip(".,")] += 1

print()      
print(f"Temas recorrentes: {temas_relevantes}")
print()
