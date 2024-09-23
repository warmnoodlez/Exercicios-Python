import os
nomes = []
boletim = []
media = 0

# Cadastro de alunos 
for i in range(0, 4):
  os.system('clear')
  nome = input(f"Informe o nome do {i+1}º aluno: ")
  nomes.append(nome)
  notas = []
  # Cadastro de notas
  for n in range(0, 4):
    notas.append(float(input(f"Informe a nota do {n+1}º bimestre do aluno(a) {nome}: ")))
  notas.insert(0, nome)
  boletim.append(notas)

# Cálculo da média
for a in range (0,4):
  media = (boletim[a][1] + boletim[a][2] + boletim[a][3] + boletim[a][4])/4
  boletim[a].append(media)

os.system('clear')

# Exibição do boletim
print("Boletim Escolar!")
for b in range(0,4):
  print(f"Aluno(a): {boletim[b][0]}")
  print(f"Nota do 1º bimestre: {boletim[b][1]}")
  print(f"Nota do 2º bimestre: {boletim[b][2]}")
  print(f"Nota do 3º bimestre: {boletim[b][3]}")
  print(f"Nota do 4º bimestre: {boletim[b][4]}")
  print(f"Média: {boletim[b][5]}")