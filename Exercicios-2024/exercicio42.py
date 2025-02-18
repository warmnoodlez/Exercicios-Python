num = []

for i in range (0,5):
  num.append(float(input(f"Informe o {i+1}° número: ")))

soma = sum(num)
media = soma / 5

print(f"A soma dos números informados é: {soma} e a média é: {media}")