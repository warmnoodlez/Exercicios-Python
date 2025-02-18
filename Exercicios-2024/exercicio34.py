altura = float(input("Informe a sua altura: "))
sexo = str(input("Informe o seu sexo:\n[M] - Masculino\n[F] - Feminino\n"))

if sexo == "M" or sexo == "m":
  peso_ideal = (72.7 * altura) - 58
  print(f"O seu peso ideal é: {peso_ideal}")
elif sexo == "F" or sexo == "f":
  peso_ideal = (62.1 * altura) - 44.7
  print(f"O seu peso ideal é: {peso_ideal}")
else:
  print("Sexo inválido")