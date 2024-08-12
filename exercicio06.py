num1 = int(input("Informe o primeiro número: "))
num2 = int(input("Informe o segundo número: "))
print ("\n[+] para Somar\n[-] para Subtrair")
operacao = input("Informe a operação: ")

if (operacao == "+"):
  print(f"A soma dos números é {num1+num2}")
elif (operacao == "-"):
  print(f"A subtração dos números é {num1-num2}")
else:
  print("Operação inválida")