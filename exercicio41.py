num = []

for i in range (0,5):
  num.append(float(input(f"Informe o {i+1}° número: ")))

num.sort()
print(f"O maior número informado foi: {num[4]}")