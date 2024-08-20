num = int(input("Digite um número: "))
if num <= 0:
    print("Número inválido")
else:
    quad = num*num
    cubo = num**3
    print(f"{num} ao quadrado é: {quad}\n{num} ao cubo é: {cubo}")