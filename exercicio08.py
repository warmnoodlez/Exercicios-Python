letra = str(input("Informe uma letra: "))
letra = letra.lower()

if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
    print("A letra informada é uma vogal")
else:
    print("A letra informada é uma consoante")