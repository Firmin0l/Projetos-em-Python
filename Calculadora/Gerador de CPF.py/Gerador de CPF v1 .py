import random

for _ in range(100):
    # Gera os 9 primeiros dígitos
    nove_digitos = ''.join(str(random.randint(0, 9)) for _ in range(9))

    # Calcula o primeiro dígito verificador
    soma_1 = sum(int(d) * c for d, c in zip(nove_digitos, range(10, 1, -1)))
    digito_1 = (soma_1 * 10) % 11
    digito_1 = digito_1 if digito_1 <= 9 else 0

    # Calcula o segundo dígito verificador
    dez_digitos = nove_digitos + str(digito_1)
    soma_2 = sum(int(d) * c for d, c in zip(dez_digitos, range(11, 1, -1)))
    digito_2 = (soma_2 * 10) % 11
    digito_2 = digito_2 if digito_2 <= 9 else 0

    # Junta tudo
    cpf = f'{nove_digitos}{digito_1}{digito_2}'

    # Formata com pontos e traço
    cpf_formatado = f'{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}'
    print(cpf_formatado)
