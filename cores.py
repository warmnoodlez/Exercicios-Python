print("\33[1;31;47mCálculo aumento de salário\33[m\n")
salario = float(input("Informe o seu salário R$: "))
aumento = salario * 0.25
novo_salario = salario + aumento

print(f"O seu salário era \33[0;32;43mR${salario}\33[m. Você receberá um aumento de \33[1;35;46mR${aumento}\33[m. Seu novo salário é \33[7;35;46mR${novo_salario}\33[m")