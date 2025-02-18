import math

co_a = float(input("Informe o coeficiente A: "))
co_b = float(input("Informe o coeficiente B: "))
co_c = float(input("Informe o coeficiente C: "))

if co_a == 0:
    print("Coeficiente A inválido.")
else:
    delta = co_b*co_b-4*co_a*co_c
    raiz_delta = math.sqrt(delta)
    x1 = (-co_b+raiz_delta)/2*co_a
    x2 = (-co_b-raiz_delta)/2*co_a

if delta <= -1:
    print("Equação inválida, delta negativo.")
elif delta == 0:
    print(f"A raíz da sua equação é {x1}.")
else:
    print(f"A raíz positiva (+) da sua equação é {x1}\nE a raíz negativa (-) da sua equação é {x2}")