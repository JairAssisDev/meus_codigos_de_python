
# Exibe as tabuadas de 1 a 10
for numero in range(1, 11):
  print(f"Tabuada do número {numero}:")
  for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")
  print()  # Adiciona uma linha em branco entre as tabuadas
