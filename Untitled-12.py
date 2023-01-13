
valores = []
maior_valor = None
menor_valor = None

valor = int(input("Digite um valor (ou zero para encerrar): "))
while valor != 0:
  if valor < 0:
    print("Valor inválido. Por favor, digite um valor positivo.")
  else:
    valores.append(valor)
  valor = int(input("Digite um valor (ou zero para encerrar): "))

if len(valores) > 0:
  maior_valor = max(valores)
  menor_valor = min(valores)

if maior_valor is not None:
  print("Maior valor:", maior_valor)
  print("Menor valor:", menor_valor)
else:
  print("Nenhum valor válido foi digitado.")
