impar = []
par = []
num = dict() #Declaração de dicionário.

for i in range (0,10):
  n = float(input(f"Informe o {i+1}° número: ")) 
  if(n % 2 == 0):
    par.append(n)  
  else:
    impar.append(n)
    
num.update({"par": par}) # Adição dos itens do vetor par no item "par" do dicionário.
num.update({"impar":  impar}) # Adição dos itens do vetor impar no item "impar" do dicionário.

# Exibindo os itens do dicionário.
print(num)
print(num["par"])
print(num["impar"])
