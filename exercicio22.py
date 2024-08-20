import math
raio = float(input("Informe o raio de um círculo: "))
area = math.pi*(raio*raio)
area = math.ceil(area)
print (f"A área do seu círculo é de: {area}")