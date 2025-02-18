import os
candidatos = []
votos = [0,0,0]

for i in range (0,3):
    candidatos.append(input(f"Informe o nome do {i+1}º candidato: "))

num_eleitores = int(input("Informe a quantidade de eleitores: "))
os.system('cls')

for i in range (0,num_eleitores):
    voto = input(f"Informe o seu voto:\n[1] - {candidatos[0]}\n[2] - {candidatos[1]}\n[3] - {candidatos[2]}\n")
    os.system('cls')
    if voto == "1":
        votos[0] = votos[0]+1
    elif voto == "2":
        votos[1] = votos[1]+1
    elif voto == "3":
        votos[2] = votos[2]+1
    else:
        print("Voto não aceito pois é inválido. ")

print (f"Votos finais da eleição:\nCandidato {candidatos[0]} - {votos[0]} votos.\nCandidato {candidatos[1]} - {votos[1]} votos.\nCandidato {candidatos[2]} - {votos[2]} votos.")