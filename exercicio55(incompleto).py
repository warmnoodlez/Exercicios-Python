frase = input("Informe a frase/palavra: ")

def substituir_acentos(string):
    acentos = ["á","à","â","ã","ê","é","í","ó","õ","ô","ú","ç","-",",","."]
    for acento in acentos:
        string = string.replace(acento, ' ')
    return string

frase_alt = frase.lower()
frase_alt = substituir_acentos(frase_alt)
frase_alt = frase_alt.strip(' ')
tmn_frase = len(frase_alt)
print(frase_alt)
frase_inv = frase_alt[::-1]
print(frase_inv)

for i in range (0,tmn_frase):
    if frase_alt[i] == frase_inv[i]:
        condicao = True
    else:
        condicao = False
        break

if condicao == True:
    print(f"A frase/palavra \"{frase}\" é um palíndromo.")
else:
    print(f"A frase/palavra \"{frase}\" não é um palíndromo.")