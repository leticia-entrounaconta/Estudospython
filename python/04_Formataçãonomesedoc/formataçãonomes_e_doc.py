def normalizar_nome(nome):

    if nome is None:
        raise ValueError("O nome não pode ser nulo.")

    if not isinstance(nome, str):
        raise TypeError("O nome deve ser informado como texto.")

    # Remove espaços no início, no final e espaços duplicados.
    nome = " ".join(nome.split())

    if not nome:
        raise ValueError("O nome não pode estar vazio.")

    caracteres_permitidos = {" ", "-", "'"}

    # Verifica se existem números ou símbolos inválidos.
    for caractere in nome:
        if not caractere.isalpha() and caractere not in caracteres_permitidos:
            raise ValueError(
                f"O nome contém um caractere inválido: '{caractere}'."
            )

    particulas = {"de", "da", "das", "do", "dos", "e"}

    palavras = nome.lower().split()
    palavras_formatadas = []

    # Formata cada palavra do nome.
    for indice, palavra in enumerate(palavras):
        if indice > 0 and palavra in particulas:
            palavras_formatadas.append(palavra)
        else:
            palavras_formatadas.append(palavra.capitalize())

    return " ".join(palavras_formatadas)



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

    # Percorre os primeiros dez dígitosos nove iniciais e o primeiro dígito verificador original.
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



print("\n========== 1- Normalizador de Nome ==========")

while True:
    nome_digitado = input("Digite o nome completo: ")

    try:
        nome_normalizado = normalizar_nome(nome_digitado)
        print(f"\nNome normalizado: {nome_normalizado}")
        break
    except (ValueError, TypeError) as e:
        print(f"\nErro: {e}") #esse print mostra o erro que ocorreu, seja ele de valor ou de tipo
        print("Verifique o nome e tente novamente.\n")

print("\n============ 2- Validador de CPF ============")

while True:
    cpf_digitado = input("Digite o CPF: ")

    if validar_cpf(cpf_digitado):
        print("\nCPF validado com sucesso!")
        break

    print("\nCPF inválido.")
    print("Verifique os números e tente novamente.\n")

# -------------------- Finalização para ficar bonitinho --------------------

print("\n")
print("          PROGRAMA FINALIZADO")
print("=" * 45) #repete o '=' 45 vezes 