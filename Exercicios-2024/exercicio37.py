print("Olá, esse é um resolvedor de equações do segundo grau! (Utilizando a fórmula de Bhaskara)")

co_a = float(input("Por favor, informe o coeficiente A: "))
co_b = float(input("Agora, informe o coeficiente B: "))
co_c = float(input("E por último o coeficiente C: "))

delta = (co_b**2) - 4 * co_a * co_c
if delta < 0:
  print("A equação não possui raízes reais.")
elif delta == 0:
  x = (-co_b + (delta**0.5)) / (2 * co_a)
  print(f"A equação possui apenas uma raiz real: {x}")
else:
  x1 = (-co_b + (delta**0.5)) / (2 * co_a)
  x2 = (-co_b - (delta**0.5)) / (2 * co_a)
  print(f"A equação possui duas raízes reais: {x1} e {x2}")