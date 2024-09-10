print("Olá, seja bem-vindo ao posto de gasolina virtual!")
print("Você irá colocar Gasolina ou Álcool?")
combustivel = input("Digite\n[G] para Gasolina\n[A] para Álcool:\n")
combustivel = combustivel.upper()
litros = float(input("Quantos litros deseja abastecer?\n"))

if (combustivel == "G"):
  if (litros <= 20):
    preco = litros * 5.50
    desconto = preco * 0.03
    total = preco - desconto
    print(f"O valor a ser pago é R${total:.2f}")
  else:
    preco = litros * 5.50
    desconto = preco * 0.05
    total = preco - desconto
    print(f"O valor a ser pago é R${total:.2f}")
elif (combustivel == "A")
  if (litros <= 20):
    preco = litros * 3.90
    desconto = preco * 0.04
    total = preco - desconto
    print(f"O valor a ser pago é R${total:.2f}")
  else:
    preco = litros * 3.90
    desconto = preco * 0.06
    total = preco - desconto
    print(f"O valor a ser pago é R${total:.2f}")
else:
  print("Opção inválida")