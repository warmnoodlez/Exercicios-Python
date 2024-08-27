print("Olá, esse é um gerador da sequencia de Fibonacci! :)")
n_termo = int(input("Informe a quantidade de termos que deseja gerar: "))

n1 = 0
n2 = 1
n3 = n1+n2

print("Termo 1: 1")
for i in range (1,n_termo+1):
  print(f"Termo {i+1}: {n3}")
  n1 = n2
  n2 = n3
  n3 = n1+n2