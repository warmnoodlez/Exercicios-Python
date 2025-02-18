vendas = dict()
media = []
qtd_vendas = []
cond_b = False
nome_produtos = ""
conclusao = []

qtd_produtos = int(input("Informe a quantidade de produtos a ser analisados: "))

for a in range(0, qtd_produtos):
  nome_produtos = input("Informe o nome do produto: ")
  print("Informe a quantidade de meses de vendas do produto a ser analisado: ")
  meses = int(input())
  
  for b in range (0, meses):
    print(f"Informe a quantidade de vendas no mês {b+1}: ")
    qtd_vendas.append(int(input()))
    
  vendas[nome_produtos]=qtd_vendas
  media.append(sum(vendas[nome_produtos])/len(vendas[nome_produtos]))
  qtd_vendas=[]

  for c in range (0, len(vendas[nome_produtos])):
    cond_a = 0
    if(vendas[nome_produtos][c] >= media[a]):
      cond_a = cond_a+1
    cond_b = cond_a >= (len(vendas[nome_produtos])/2)

  if cond_b is True:
    conclusao.append(f"O produto {nome_produtos} possui aumento nas vendas.\n")
  else:
    conclusao.append(f"O produto {nome_produtos} possui baixa nas vendas.\n")

print(conclusao)