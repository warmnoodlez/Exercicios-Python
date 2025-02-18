from math import ceil

ano_nasc = int(input("Informe o seu ano de nascimento: "))
ano_at = int(input("Informe o ano atual: "))
idade = ano_at-ano_nasc

id_meses= idade*12
id_semanas= idade*52.143
id_semanas = ceil(id_semanas)
id_dias=idade*365

print(f"Sua idade em anos é: \33[1;30;45m{idade}\33[m")
print(f"Sua idade em meses é: \33[1;30;42m{id_meses}\33[m")
print(f"Sua idade em semanas é aproximadamente: \33[1;30;43m{id_semanas}\33[m")
print(f"Sua idade em dias é: \33[1;30;46m{id_dias}\33[m")