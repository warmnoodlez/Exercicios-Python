nomes = []
notas = [][]

for i in range (0,4):
  nomes[i] = input(f"Informe o nome do {i+1}º aluno: ")
  for j in range (0,5):
    notas[i][j] = float(input(f"Informe a nota do {j+1}º aluno: "))

for i in range (0,4):
  notas[i][]