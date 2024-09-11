frase = input("Informe a frase/palavra: ")

def substituir_acentos(string):
    acentos = ["á","à","â","ã","ê","é","í","ó","õ","ô","ú","ç","-",",","."]
    for acento in acentos:
        string = string.replace(acento, ' ')
    return string

frase_inv = frase.lower()
frase_inv = substituir_acentos(frase_inv)
frase_inv = frase_inv.replace(" ", "")
frase_alt = frase_inv
tmn_frase = len(frase_inv)
print(frase_alt)
frase_inv = frase_inv[::-1]
print(frase_inv)

for i in range (0,tmn_frase):
    if frase_inv[i] == frase_alt[i]:
        condicao = True
    else:
        condicao = False
        break

if condicao == True:
    print(f"A frase/palavra \"{frase}\" é um palíndromo.")
else:
    print(f"A frase/palavra \"{frase}\" não é um palíndromo.")