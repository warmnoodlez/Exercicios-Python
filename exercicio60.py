num = int(input("Informe o número para a tabuada: "))
num_2 = int(input("Informe o número inicial para a tabuada: "))
num_3 = int(input("Informe o número final para a tabuada: "))

for i in range (num_2, num_3+1):
  print(f"{num} x {i} = {num*i}")