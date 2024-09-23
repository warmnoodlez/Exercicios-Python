tabela = dict()

quantidade = 2
desempenho = []
for i in range(0,quantidade):
   time = input("\33[1;37;40mInforme o nome do time: \33[m")
   if time not in tabela:
    for c in range(0,5):
      if c == 0:
        info = int(input ("Informe a quantidade de vitórias: "))
      elif c == 1:
        info = int(input ("Informe a quantidade de empates: "))  
      elif c ==2:
        info = int(input("Informe a quantidade de derrotas: "))
      elif c ==3:
        info = int(input("Informe a quantidade de gols próprios: "))  
      elif c == 4:
        info = int(input("Informe a quantidade de gols contras: ")) 
      desempenho.append(info)
    desempenho.insert(0, desempenho[0]*3 + desempenho[1])
    desempenho.append(desempenho[-2] - desempenho[-1])  
    #tabela[time] = desempenho
    tabela[time] = {"Pontos": desempenho[0], "Vitórias": desempenho[1], "Empates":desempenho[2], "Gols Próprio" : desempenho[3], "Gols Contra" : desempenho[4], "Saldo": desempenho[5]}
    desempenho = []


print(tabela)

