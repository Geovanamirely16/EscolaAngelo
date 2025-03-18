gastos = [50, 30, 40, 60, 70, 1500]
media = sum(gastos) / len(gastos)

print(f"A média do valor gasto é R$ (media:.2f)")

notas = [75, 82, 90, 68, 88, 92, 70, 99]
notas.sort()
n = len(notas)
if n % 2 == 1:
  mediana = notas[n // 2]

print(f"A mediana das notas é(mediana)")
