# Exercício 1 - Validador de CPF

# Criando função para resetar o programa.
import sys
import os

def resetar_programa():
    python = sys.executable
    os.execl(python, python, * sys.argv)

# Definindo Listas
resultado = []
digitos_cpf = []
verificadores = []

# Informando o CPF:
cpf = input("\nInforme o seu CPF: ")

# Se o CPF for escrito somente utilizando números, ele executará o programa. Caso contrário ele insistirá para o usuário informar da maneira correta.
condicao = cpf.isdigit()

# Testando condição:
if condicao == True:
    organizando_digitos()
    primeiro_digito()
    segundo_digito()
    teste_final()
else:
    resetar_programa()

# Definindo funções:

# Organizando os digitos em listas.
def organizando_digitos():
    # Separando digitos individualmente em uma lista e os convertendo de Caracter para Inteiros
    digitos_cpf_strg = list(cpf)
    for val in digitos_cpf_strg:
        digitos_cpf.append(int(val))

    # Separando os digitos do CPF em duas listas: inscrição e os digitos verificadores.
    num_inscricao = digitos_cpf[:9]
    verificadores_cpf = digitos_cpf[-2:]


# Fazendo o cálculo para obter o primeiro digito.
def primeiro_digito():
    b = -1
    for a in range(10,1,-1):
        b = b + 1
        resultado.append(a*digitos_cpf[b])

    soma = sum(resultado)
    resto = soma % 11

    if resto < 2:
        verificadores.append(0)
    else:
        verificadores.append(11-resto)




# Fazendo o cálculo para obter o segundo digito.
def segundo_digito():
    # Resetando elementos para o novo cálculo.
    resultado.clear()
    b = -1 

    for a in range(11,1,-1):
        b = b + 1
        resultado.append(a*digitos_cpf[b])

    soma = sum(resultado)
    resto = soma % 11

    if resto < 2:
        verificadores.append(0)
    else:
        verificadores.append(11-resto)

# Testando se o CPF é válido ou não.
def teste_final():
    if verificadores == verificadores_cpf:
        print("O CPF informado é valido! :)")
    else:
        print("O CPF informado não é válido. :(")