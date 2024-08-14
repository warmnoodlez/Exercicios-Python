salario = float(input("Informe o salário: "))
gratficacao = salario * 0.05
imposto = salario * 0.07
salario_liquido = salario + gratficacao - imposto

print(f"O salário líquido é de R${salario_liquido}")