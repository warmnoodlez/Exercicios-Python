import os
intervalos = [0,0,0,0,0]
num = 1

while num >= 0:
    num = int(input("Informe um número: "))
    os.system('cls')
    if num >= 0 and num <= 25:
        intervalos[0] = intervalos[0]+1
    elif num > 25 and num <= 50:
        intervalos[1] = intervalos[1]+1
    elif num > 50 and num <= 75:
        intervalos[2] = intervalos[2]+1
    elif num > 75 and num <= 100:
        intervalos[3] = intervalos[3]+1
    elif num > 100:
        intervalos[4] = intervalos[4]+1

print("Quantidade de números nos intervalos:")
print(f"Intervalo [0-25]: {intervalos[0]} números.")
print(f"Intervalo [26-50]: {intervalos[1]} números.")
print(f"Intervalo [51-75]: {intervalos[2]} números.")
print(f"Intervalo [76-10]: {intervalos[3]} números.")
print(f"Números maiores que 100: {intervalos[4]} números.")