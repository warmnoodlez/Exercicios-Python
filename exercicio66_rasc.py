nomes = []
notas = []

# for i in range (0,4):
#   nomes[i] = nomes.append(f"Informe o nome do {i+1}º aluno: ")
#   for j in range (0,4):
#     notas[i][j] = nomes.append(f"Informe a nota do {j+1}º aluno: ")

# for i in range (0,4):
#   notas[i][5] = notas[i][0] + notas[i][1] + notas[i][2] + notas[i][3]
#   print(notas[i][5])

#boletim = [["Thomas", 8, 9, 7, 6, 0], ["Grazy", 7,8,9,10,0], ["José", 9,8,7,6,0], ["Maria", 10,9,8,7,0]]
boletim = []

for i in range(0, 4):
  nome = input(f"Informe o nome do {i+1}º aluno: ")
  nomes.append(nome)
  notas = []
  for n in range(0, 4):
    notas.append(float(input(f"Informe a nota do {n+1}º bimestre do aluno(a) {nome}: ")))
  notas.insert(0, nome)
  boletim.append(notas)

for a in range (0,4):
  boletim[nomes[a]][]

print(boletim)

# boletim = dict()
# for i in range(0, 4):
#   nome = input(f"Informe o nome do {i+1}º aluno: ")
#   if boletim.get(nome):
#     print("Aluno já cadastrado!")
#   else:
#     notas = []
#     for j in range(0, 4):
#       notas.append(float(input(f"Nota do {j+1}º {nome}: ")))

#     boletim[nome] = notas
#     print()

# print(boletim)
