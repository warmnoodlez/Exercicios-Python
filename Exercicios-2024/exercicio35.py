from math import ceil

print("Olá, seja bem-vindo(a) a nossa loja de tintas virtual! :)\n")
print("Cada lata de tinta possui 18 litros e cada litro de tinta cobre 3 metros quadrados.\n")

area = float(input("Informe em metros quadrados a área a ser pintada: "))
latas = area/18
latas = ceil(latas)
preco_final = latas * 80

print(f"Você precisará de {latas} latas, que no total custam R${preco_final}! :)")
