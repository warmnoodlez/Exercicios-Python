num = int(input("Informe um número: "))

def e_primo(n):  
  primo_ = True

  if n < 2:
      return False
  elif n == 2:
      primo_ = True
  else:
    for i in range(3,n):
      if n % i == 0:
        primo_ = False
        break
      else:
        primo_ = True

  return primo_


for i in range (1, num+1):
  print(e_primo(i), i)
  # if (e_primo(i) == True):
  #   print(i)
  # else:
  #   continue