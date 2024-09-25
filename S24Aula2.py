vendas = dict()
qtd_vendas = []
qtd_produtos = int(input("Informe a quantidade de produtos a ser analisados: "))

for a in range(0, qtd_produtos):
  nome_produtos = input("Informe o nome do produto: ")
  print("Informe a quantidade de meses de vendas do produto a ser analisado: ")
  meses = int(input())
  for b in range (0, meses):
    print(f"Informe a quantidade de vendas no mês {b+1}: ")
    qtd_vendas.append(int(input()))
    
  vendas[nome_produtos]=qtd_vendas
  qtd_vendas=[]

  

