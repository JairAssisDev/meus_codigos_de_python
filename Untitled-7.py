
idades = []
pesos = []
alturas = []

media_idade = 0
pessoas_peso_alto_altura_baixa = 0
pessoas_idade_10_30_altura_alta = 0
total_altura_alta = 0
for i in range(4):
  idade = int(input("Digite a idade da pessoa {}: ".format(i+1)))
  peso = float(input("Digite o peso da pessoa {}: ".format(i+1)))
  altura = float(input("Digite a altura da pessoa {}: ".format(i+1)))

  idades.append(idade)
  pesos.append(peso)
  alturas.append(altura)
media_idade = sum(idades) / len(idades)
for i in range(len(pesos)):
  if pesos[i] > 90 and alturas[i] < 1.50:
    pessoas_peso_alto_altura_baixa += 1
for i in range(len(alturas)):
  if alturas[i] > 1.90:
    total_altura_alta += 1
    if 10 <= idades[i] <= 30:
      pessoas_idade_10_30_altura_alta += 1

if total_altura_alta > 0:
  percentagem_idade_10_30_altura_alta = (pessoas_idade_10_30_altura_alta / total_altura_alta) * 100
print("Média de idade das dez pessoas:", media_idade)
print("Quantidade de pessoas com peso superior a 90 quilos e altura inferior a 1,50 metro:", pessoas_peso_alto_altura_baixa)
print("Percentagem de pessoas com idade entre 10 e 30 anos entre as pessoas que medem mais de 1,90 metro:",percentagem_idade_10_30_altura_alta)
