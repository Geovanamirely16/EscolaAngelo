# Faça uma função que retorne um jogo da mega sena com valores aleatórios não repitidos.
# O usuário deverá dizer quantos números quer jogar, de 6 até 10
# Imprima o resultado solicitado.

import random

def gerar_jogo_mega_sena(qtd_numeros):
    if qtd_numeros < 6 or qtd_numeros > 10:
        return "Você deve escolher entre 6 e 10 números."
    
    jogo = random.sample(range(1, 61), qtd_numeros)
    jogo.sort()
    return jogo

# Exemplo de uso:
try:
    qtd = int(input("Quantos números você quer jogar? (de 6 até 10): "))
    resultado = gerar_jogo_mega_sena(qtd)
    print("Seu jogo da Mega-Sena:", resultado)
except ValueError:
    print("Por favor, insira um número válido.")