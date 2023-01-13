
idades = []
alturas = []
soma_alturas = 0

idade = int(input("Digite a idade da pessoa (ou qualquer número menor ou igual a zero para encerrar): "))
while idade > 0:
  altura = float(input("Digite a altura da pessoa: "))
  idades.append(idade)
  alturas.append(altura)
  idade = int(input("Digite a idade da pessoa (ou qualquer número menor ou igual a zero para encerrar): "))

for i in range(len(idades)):
  if idades[i] > 50:
    soma_alturas += alturas[i]

if len(idades) > 0:
  media_alturas = soma_alturas / len(idades)
  print("Média das alturas das pessoas com mais de 50 anos:", media_alturas)
else:
  print("Nenhuma idade foi digitada.")
