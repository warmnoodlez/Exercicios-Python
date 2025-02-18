num = []

for i in range (0,3):
  num.append(float(input(f"Informe o {i+1}° número: ")))

resultado = num[0] * num[1] * num[2]

print(f"O produto dos números informados é: {resultado}")