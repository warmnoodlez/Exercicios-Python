nums = []

for i in range (0,10):
  nums.append(float(input(f"Informe o {i+1}º número: ")))

menor_num = min(nums)
maior_num = max(nums)

print(f"O maior número é {maior_num} e o menor é {menor_num}.")