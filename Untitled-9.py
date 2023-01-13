
idades = []
soma_idades = 0

idade = int(input("Digite uma idade: "))
while idade != 0:
  idades.append(idade)
  soma_idades += idade
  idade = int(input("Digite uma idade: "))

if len(idades) > 0:
  media_idades = soma_idades / len(idades)
  print("Média das idades digitadas:", media_idades)
else:
  print("Nenhuma idade foi digitada.")
