
faixas = [(1, 15), (16, 30), (31, 45), (46, 60), (61, 200)]
contadores = [0, 0, 0, 0, 0]
total_pessoas = 0
while total_pessoas < 15:
  idade = int(input("Insira a idade da pessoa: "))

  for i, (inicio, fim) in enumerate(faixas):
    if inicio <= idade <= fim:
      contadores[i] += 1
      break
  total_pessoas += 1
for i, (inicio, fim) in enumerate(faixas):
  print(f"Faixa etária {i+1}: {contadores[i]} pessoas")

percentagem_primeira = contadores[0] / total_pessoas * 100
percentagem_ultima = contadores[-1] / total_pessoas * 100
print(f"Percentagem de pessoas na primeira faixa etária: {percentagem_primeira:.2f}%")
print(f"Percentagem de pessoas na última faixa etária: {percentagem_ultima:.2f}%")
print(faixas)





