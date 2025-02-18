num = int(input("Informe um número: "))

primo = True

if num < 2:
  primo = False
else:
  for i in range(1, num):
    if num % i == 0:
      primo = False
    else:
      primo = True

if primo == True:
  print("O número informado é primo!")
else:
  print("O número informado não é primo!")