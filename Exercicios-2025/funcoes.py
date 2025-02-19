# FUNÇÕES PARA O EXERCÍCIO 1

# Organizando os digitos em listas.
def organizando_digitos(cpf):
    digitos_cpf = []
    # Separando digitos individualmente em uma lista e os convertendo de Caracter para Inteiros
    digitos_cpf_strg = list(cpf)
    for val in digitos_cpf_strg:
        digitos_cpf.append(int(val))

    # Separando os digitos do CPF em duas listas: inscrição e os digitos verificadores.
    num_inscricao = digitos_cpf[:9]
    verificadores_cpf = digitos_cpf[-2:]
    return (num_inscricao, verificadores_cpf, digitos_cpf)

# Fazendo o cálculo para obter o primeiro digito.
def primeiro_digito(digitos_cpf):
    calc = []
    verificadores = []
    b = -1
    for a in range(10,1,-1):
        b = b + 1
        calc.append(a*digitos_cpf[b])

    soma = sum(calc)
    resto = soma % 11

    if resto < 2:
        calc_verificadores = 0
    else:
        calc_verificadores = 11-resto
    return calc_verificadores

# Fazendo o cálculo para obter o segundo digito.
def segundo_digito(calc_verificadores, digitos_cpf):
    # Resetando elementos para o novo cálculo.
    calc = []
    b = -1 

    for a in range(11,1,-1):
        b = b + 1
        calc.append(a*digitos_cpf[b])

    soma = sum(calc)
    resto = soma % 11

    if resto < 2:
        calc_verificadores = 0
    else:
        calc_verificadores = 11-resto
    return calc_verificadores

# Testando se o CPF é válido ou não.
def teste_final(calc_verificadores, verificadores_cpf):
    if calc_verificadores == verificadores_cpf:
        print("O CPF informado é valido! :)")
    else:
        print("O CPF informado não é válido. :(")