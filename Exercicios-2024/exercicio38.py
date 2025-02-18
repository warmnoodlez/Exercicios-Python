print("Olá, esse é um verificador de anos bissextos! :)")
ano = int(input("Informe um ano: "))

if ano % 4 == 0:
  print("Esse ano é bissexto!")
else:
  print(f"O ano {ano} não é bissexto!")