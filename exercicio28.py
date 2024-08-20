num=[]
for i in range (0,3):
    num.append(float(input(f"Informe o {i+1}° número: ")))

num=sorted(num)

print(f"O maior número dentre os informados é {num[2]}")