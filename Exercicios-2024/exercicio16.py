salario = float(input("Informe o salário: "))
aumento = float(input("Informe o percentual de aumento: "))

aumento = aumento/100

novo_salario = salario + (salario * aumento)

print(f"O novo salário é de R${novo_salario}")