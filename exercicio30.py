num1 = float(input("Informe o primeiro número: "))
num2 = float(input("Informe o segundo número: "))
op = input("Informe a operação desejada:\n[+] - Soma\n[-] - Subtração\n[/] - Divisão\n[*] - Multiplicação\n")

if op == "+":
  resultado = num1 + num2
elif op == "-":
  resultado = num1 - num2
elif op == "/":
  resultado = num1 / num2
elif op == "*":
  resultado = num1 * num2
else:
  print("Operação inválida")

print(f"O resultado da operação é: {resultado}")