deposito = float(input("Informe o valor do depósito: "))
taxa = float(input("Informe a taxa de juros: "))
juros = deposito * taxa / 100
saldo = deposito + juros

print(f"O valor do rendimento é de R${juros} e o saldo final é de R${saldo}")