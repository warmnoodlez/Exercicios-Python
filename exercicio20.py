periodo = input("Informe o periodo:\n[M] - Matutino\n[V] - Vespertino\n[N] - Noturno\n")
periodo = periodo.lower()

if periodo == "m":
    print("Bom dia!")
elif periodo == "v":
    print("Boa tarde!")
elif periodo == "n":
    print("Boa noite!")
else:
    print("Periodo inválido, tente novamente!")