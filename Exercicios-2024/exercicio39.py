num = int(input("Informe um número: "))

centena = num // 100
dezena = (num % 100) // 10
unidade = num % 10

if centena == 0 and dezena == 0 and unidade == 0:
  print("Zero")
elif centena == 0 and dezena == 0:
  print(f"O número {num} possui {unidade} unidades.")
elif dezena == 0 and unidade == 0:
  print(f"O número {num} possui {centena} centenas.")
elif centena == 0 and unidade == 0:
  print(f"O número {num} possui {dezena} dezenas.")
elif centena == 0:
  print(f"O número {num} possui {dezena} dezenas e {unidade} unidades.")
elif dezena == 0:
  print(f"O número {num} possui {centena} centenas e {unidade} unidades.")
elif unidade == 0:
  print(f"O número {num} possui {centena} centenas e {dezena} dezenas.")
else:
  print(f"O número {num} possui {centena} centenas, {dezena} dezenas e {unidade} unidades.")
  
