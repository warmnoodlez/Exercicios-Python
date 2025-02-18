num = int(input("Informe um número: "))
num_inf = num

fatorial = num
for i in range (1, num):
  fatorial = fatorial * (num - 1)
  num = num - 1

print (f"O fatorial de {num_inf} é: {fatorial}")