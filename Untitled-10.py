
print("1. Média aritmética")
print("2. Média ponderada")
print("3. Sair")

opcao = int(input("Escolha uma opção: "))

if opcao == 1:
  
  valores = []
  valor = float(input("Digite um valor (ou qualquer número negativo para encerrar): "))
  while valor >= 0:
    valores.append(valor)
    valor = float(input("Digite um valor (ou qualquer número negativo para encerrar): "))

  
  if len(valores) > 0:
    media = sum(valores) / len(valores)
    print("Média aritmética:", media)
  else:
    print("Nenhum valor foi digitado.")
elif opcao == 2:
  
  valores = []
  pesos = []
  valor = float(input("Digite um valor (ou qualquer número negativo para encerrar): "))
  while valor >= 0:
    peso = float(input("Digite o peso do valor {}: ".format(valor)))
    valores.append(valor)
    pesos.append(peso)
    valor = float(input("Digite um valor (ou qualquer número negativo para encerrar): "))