
idades = []
alturas = []
pesos = []

pessoas_acima_50 = 0
altura_media_10_20 = 0
total_10_20 = 0
pessoas_abaixo_40 = 0

for i in range(3):
  idade = int(input("Digite a idade da pessoa {}: ".format(i+1)))
  altura = float(input("Digite a altura da pessoa {}: ".format(i+1)))
  peso = float(input("Digite o peso da pessoa {}: ".format(i+1)))

  idades.append(idade)
  alturas.append(altura)
  pesos.append(peso)

for idade in idades:
  if idade > 50:
    pessoas_acima_50 += 1
for i in range(len(idades)):
  if 10 <= idades[i] <= 20:
    altura_media_10_20 += alturas[i]
    total_10_20 += 1

if total_10_20 > 0:
  altura_media_10_20 /= total_10_20
for peso in pesos:
  if peso < 40:
    pessoas_abaixo_40 += 1

percentagem_abaixo_40 = (pessoas_abaixo_40 / len(pesos)) * 100

print("Quantidade de pessoas com idade superior a 50:", pessoas_acima_50)
print("Média das alturas das pessoas com idade entre 10 e 20:", altura_media_10_20)
print("Percentagem de pessoas com peso inferior a 40 quilos:", percentagem_abaixo_40)
