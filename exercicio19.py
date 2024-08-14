nums = []

for i in range (0,3):
  nums.append(int(input(f"Informe o {i+1}º número: ")))

nums.sort(reverse=True)

print(f"Os números em ordem decrescente são: {nums[0]}, {nums[1]} e {nums[2]}")