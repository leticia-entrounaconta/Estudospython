def normalizar_nome(nome):
   
    nome = " ".join(nome.split())

    if not nome:
        return None

    if not all(caractere.isalpha() or caractere == " " for caractere in nome):
        return None

    return nome.title()


def validar_cpf(cpf):
    
    cpf = cpf.replace(".", "").replace("-", "").strip()

    
    if len(cpf) != 11:
        return False

    
    if not cpf.isdigit():
        return False

    
    if cpf == cpf[0] * 11:
        return False

    soma = 0

    
    for indice in range(9):
        soma += int(cpf[indice]) * (10 - indice)

    primeiro_digito = (soma * 10) % 11

    if primeiro_digito == 10:
        primeiro_digito = 0

    soma = 0

    
    for indice in range(10):
        soma += int(cpf[indice]) * (11 - indice)

    segundo_digito = (soma * 10) % 11

    if segundo_digito == 10:
        segundo_digito = 0

    return cpf[-2:] == f"{primeiro_digito}{segundo_digito}"


def formatar_cpf(cpf):
    # Remove a formatação existente.
    cpf = cpf.replace(".", "").replace("-", "").strip()

    return f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"


print("========== Cadastro ==========")

nome_digitado = input("Digite o nome completo: ")
nome_normalizado = normalizar_nome(nome_digitado)

if nome_normalizado is None:
    print("Erro: o nome não pode estar vazio ou conter números.")
else:
    print(f"Nome normalizado: {nome_normalizado}")


cpf_digitado = input("Digite o CPF: ")

if validar_cpf(cpf_digitado):
    print(f"CPF válido: {formatar_cpf(cpf_digitado)}")
else:
    print("Erro: CPF vazio ou inválido.")