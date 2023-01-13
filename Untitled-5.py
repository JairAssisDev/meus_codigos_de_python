
avista_total = []
cretido_total = []
total = []

for i in range(1,15):
 
  code = int(input("Escolha a transação  (0 para Avista, 1 no cartão) : "))
  valor = float(input("Digite o valor da compra : "))


  if code == 0:

    avista_total.append(valor)
    total.append(valor)
  elif code == 1:

    cretido_total.append(valor)
    total.append(valor)

valor_parecela = cretido_total[0] / 3


print("Total de transações em dinheiro:", sum(avista_total))
print("Total de transações de crédito:", sum(cretido_total))
print("Total:", sum(total))
print("Primeira prestação para operações de crédito:", valor_parecela)
