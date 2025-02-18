base = int(input("Informe a base: "))
exp = int(input("Informe o expoente: "))

base_alt = base
for i in range (1, exp):
  base = base * base_alt

print(f"O resultado é: {base}")