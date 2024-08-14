nums = []

for i in range (0,3):
  nums.append(int(input(f"Informe a {i+1}º medida do lado do triângulo: ")))

if nums[0] == nums[1] and nums[1] == nums[2]:
  print("O triângulo informado é equilátero")
elif nums[0] == nums[1] or nums[1] == nums[2] or nums[0] == nums[2]:
  print("O triângulo informado é isósceles")
else:
  print("O triângulo informado é escaleno")