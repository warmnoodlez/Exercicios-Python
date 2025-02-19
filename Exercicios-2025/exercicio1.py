# Exercício 1 - Validador de CPF

# Criando função para resetar o programa.
import funcoes

# Definindo Listas
listas = []
calc_verificadores = []

# Informando o CPF:
cpf = input("\nInforme o seu CPF: ")

# Se o CPF for escrito somente utilizando números, ele executará o programa. Caso contrário ele insistirá para o usuário informar da maneira correta.
condicao = cpf.isdigit()

# Testando condição:
while condicao != True:
    print("Caracteres inválidos detectados, tente novamente!")
    cpf = input("\nInforme o seu CPF: ")
    condicao = cpf.isdigit()
else:
    # Organizando digitos do CPF em listas: 
    listas = funcoes.organizando_digitos(cpf)
    num_inscricao = listas[0]
    verificadores_cpf = listas[1]
    digitos_cpf = listas[2]

    calc_verificadores.append(funcoes.primeiro_digito(digitos_cpf))
    calc_verificadores.append(funcoes.segundo_digito(calc_verificadores, digitos_cpf))
    
    funcoes.teste_final(calc_verificadores, verificadores_cpf)