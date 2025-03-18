# Dados do produto
produto = {
  "nome": "Smartphone X200",
  "preco": 1999.99,
  "quantidade_estoque": 50,
  "avaliacao_clientes": 4.7,
  "numero_avaliacoes": 345,
  "caracteristicas": ["64GB", "12MP", "4000mAh"],
  "disponivel": True
}

# Funcão para identificar o tipo de dado
def identificar_tipo_dado(valor):
  if isinstance(valor, str):
    return "Dado Qualitativo (String)"
  elif isinstance(valor, (int, float)):
    return "Dado Quantitativo (Número)"
  elif isinstance(valor, list):
    return "Dado Qualitativo (Lista de Strings)"
  elif isinstance(valor, bool):
    return "Dado Qualitativo (Booleano)"
  else:
    return "tipo de dado desconhecido"
  
print()
# Exibir os dados e seus tipo
for chave, valor in produto.items():
  tipo = identificar_tipo_dado(valor)
  print(f"{chave}: {valor} -> {tipo}")
    
