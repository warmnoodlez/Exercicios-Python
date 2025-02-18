print("\33[1;35;40mTabela de times.\33[m\n")
tabela = dict()

quantidade = 1
desempenho = []
for i in range(0,quantidade):
   time = input("\33[1;37;40mInforme o nome do time: \33[m")
   if time not in tabela:
    for c in range(0,5):
      if c == 0:
        info = int(input ("\33[1;37;40mInforme a quantidade de vitórias:\33[m "))
      elif c == 1:
        info = int(input ("\33[1;37;40mInforme a quantidade de empates:\33[m "))  
      elif c ==2:
        info = int(input("\33[1;37;40mInforme a quantidade de derrotas: \33[m"))
      elif c ==3:
        info = int(input("\33[1;37;40mInforme a quantidade de gols próprios: \33[m"))  
      elif c == 4:
        info = int(input("\33[1;37;40mInforme a quantidade de gols contras:\33[m ")) 
      desempenho.append(info)
    print()
    desempenho.insert(0, desempenho[0]*3 + desempenho[1])
    desempenho.append(desempenho[-2] - desempenho[-1])  
    tabela[time] = desempenho
    #tabela[time] = {"Pontos": desempenho[0], "Vitórias": desempenho[1], "Empates":desempenho[2], "Gols Próprio" : desempenho[3], "Gols Contra" : desempenho[4], "Saldo": desempenho[5]}
    desempenho = []


#0print(tabela)

print("{:<10}   {:<10}   {:<10}   {:<10}   {:<10}   {:<10}   {:<10}   {:<10}".format("\33[1;34;40mTIME\33[m", "\33[1;35;40mPONTOS\33[m" , "\33[1;34;40mVITÓRIAS\33[m", "\33[1;35;40mEMPATES\33[m", "\33[1;34;40mDERROTAS\33[m","\33[1;35;40mGOLS PRÓPRIOS\33[m","\33[1;34;40mGOLS CONTRA\33[m", "\33[1;35;40mSALDO\33[m"))
for nomeDoTime, desempenho in tabela.items():
  time = nomeDoTime 
  pontos, vitorias, empates, derrotas, golspro,golscontra,saldo = desempenho
  print(("{:<10}  {:<10}  {:<10}  {:<10}  {:<10} {:<10}  {:<10}  {:<10}".format(time, pontos , vitorias, empates, derrotas, golspro, golscontra,saldo)))

