
#Ela recebe um CPF e devolve True (válido) ou False (inválido).
def validar_cpf(cpf):
    # Remove pontos, hífens e espaços extras do CPF digitado.
    cpf = cpf.replace(".", "").replace("-", "").strip()

    # Verifica se o CPF possui exatamente 11 caracteres.
    if len(cpf) != 11:
        return False

    # Verifica se todos os caracteres são números.
    if not cpf.isdigit():
        return False

    # Impede CPFs com todos os dígitos iguais, como 11111111111.
    if cpf == cpf[0] * 11:
        return False

    # Variável que armazenará a soma do cálculo do primeiro dígito.
    soma = 0

    # Percorre os primeiros nove dígitos do CPF.
    # range(9) gera os números de 0 até 8.
    for indice in range(9):
        # Converte o caractere para número e multiplica pelo peso.
        soma += int(cpf[indice]) * (10 - indice)

    # Calcula o primeiro dígito verificador.
    primeiro_digito = (soma * 10) % 11

    # Se o resultado for 10, o dígito verificador deve ser 0.
    if primeiro_digito == 10:
        primeiro_digito = 0

    # Zera a soma para iniciar o cálculo do segundo dígito.
    soma = 0

    # Percorre os primeiros dez dígitos os nove iniciais e o primeiro dígito verificador original.
    for indice in range(10):
        # Agora os pesos vão de 11 até 2.
        soma += int(cpf[indice]) * (11 - indice)

    # Calcula o segundo dígito verificador.
    segundo_digito = (soma * 10) % 11

    # Se o resultado for 10, o dígito verificador deve ser 0.
    if segundo_digito == 10:
        segundo_digito = 0

    # Compara os dois dígitos calculados com os dois últimos dígitos do CPF.
    return cpf[-2:] == f"{primeiro_digito}{segundo_digito}"


# Mostra o título do programa.
print("========== Validador de CPF ==========")

# Solicita o CPF ao usuário.
cpf_digitado = input("Digite o CPF: ")

# Chama a função e verifica o resultado.
if validar_cpf(cpf_digitado):
    print("CPF válido.")
else:
    print("CPF inválido.")