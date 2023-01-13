
soma_pares = 0
soma_primos = 0

for i in range(10):
  numero = int(input("Digite o número {}: ".format(i+1)))

  if numero % 2 == 0:
    soma_pares += numero
  else:
    eh_primo = True
    for i in range(2, numero):
      if numero % i == 0:
        eh_primo = False
        break
    if eh_primo:
      soma_primos += numero

print("Soma dos números pares:", soma_pares)
print("Soma dos números primos:", soma_primos)

