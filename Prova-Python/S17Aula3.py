print("qual o numero de pessoas que participarão da reunião: ")
pessoas = int(input())
print("qual o tipo de reunião sera realizada: normal ou executiva ")
reuniao=input()

def recomendar_sala(pessoas, reuniao):
  if(pessoas>0):
    if reuniao == "normal":
      if(pessoas <= 5):
        print("A reunião sera relizada na sala pequena")
      elif(pessoas>=6 and pessoas<=15):
        print("A reunião sera realizada na sala média")
      else:
        print(" A reunião sera realizada na sala grande")
    elif reuniao == "executiva":
      print(" A reunião sera realizada na sala grande")
  else:
    print("Não é possivel realizar a reunião")

recomendar_sala(pessoas, reuniao)