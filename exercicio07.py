notas=[]

for i in range (0,4):
    notas.append(int(input(f"Informe a nota do {i+1}º Bimestre: ")))

disciplina=str(input("Informe a disciplina: "))

media=(notas[0]+notas[1]+notas[2]+notas[3])/4

print(f"A média das notas na disciplina de {disciplina} é de {media}")