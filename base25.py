# JOGO DA VELHA
# Com base no exercício anterior, crie um JOGO DA VELHA completo. Quando um dos jogadores fizer a velha, informe quem foi o vencedor, se X ou O, e encerre o programa.

def exibir(t): [print(" | ".join(l)) or print("-"*9) for l in t]

def venceu(t, j):
    return any(all(c == j for c in l) for l in t) or \
           any(all(t[i][j] == j for i in range(3)) for j in range(3)) or \
           all(t[i][i] == j for i in range(3)) or \
           all(t[i][2 - i] == j for i in range(3))

def jogar():
    t = [[" "]*3 for _ in range(3)]; j = "X"
    while True:
        exibir(t)
        l, c = map(int, input(f"Jogador {j}, linha e coluna: ").split())
        if t[l][c] != " ": print("Ocupado!"); continue
        t[l][c] = j
        if venceu(t, j): exibir(t); print(f"{j} venceu!"); break
        if all(c != " " for r in t for c in r): exibir(t); print("Deu velha!"); break
        j = "O" if j == "X" else "X"

jogar()