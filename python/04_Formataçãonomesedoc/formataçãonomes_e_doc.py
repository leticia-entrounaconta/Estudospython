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

    # Verifica números e símbolos inválidos.
    for caractere in nome:
        if not caractere.isalpha() and caractere not in caracteres_permitidos:
            raise ValueError(
                f"O nome contém um caractere inválido: '{caractere}'."
            )

    particulas = {"de", "da", "das", "do", "dos", "e"}

    palavras = nome.lower().split()
    palavras_formatadas = []

    for indice, palavra in enumerate(palavras):
        if indice > 0 and palavra in particulas:
            palavras_formatadas.append(palavra)
        else:
            palavras_formatadas.append(palavra.capitalize())

    return " ".join(palavras_formatadas)


def validar_cpf(cpf):
    # Remove pontos, hífens e espaços extras.
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


def limpar_cpf(cpf):
    """Remove pontos, traços e espaços do CPF."""
    return cpf.replace(".", "").replace("-", "").strip()


def formatar_cpf(cpf):
    """Formata o CPF como 000.000.000-00."""
    cpf = limpar_cpf(cpf)

    return f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"


def validar_email(email):
    email = email.strip()

    if not email:
        return False

    # O e-mail deve possuir apenas um @.
    if email.count("@") != 1:
        return False

    usuario, dominio = email.split("@")

    # Verifica se existe conteúdo antes e depois do @.
    if not usuario or not dominio:
        return False

    # O domínio deve possuir pelo menos um ponto.
    if "." not in dominio:
        return False

    # Não permite espaços.
    if " " in email:
        return False

    # Não permite domínio começando ou terminando com ponto.
    if dominio.startswith(".") or dominio.endswith("."):
        return False

    return True

def validar_telefone(telefone):
    # Remove caracteres usados na formatação.
    telefone = (
        telefone.replace("(", "")
        .replace(")", "")
        .replace("-", "")
        .replace(" ", "")
    )

    # Verifica se possui apenas números.
    if not telefone.isdigit():
        return False

    # Telefone fixo: 10 dígitos.
    # Celular: 11 dígitos.
    if len(telefone) not in (10, 11):
        return False

    # Impede números com todos os dígitos iguais.
    if telefone == telefone[0] * len(telefone):
        return False

    # O DDD não pode começar com zero.
    if telefone[0] == "0":
        return False

    # Celulares brasileiros possuem 9 após o DDD.
    if len(telefone) == 11 and telefone[2] != "9":
        return False

    return True


def cpf_ja_cadastrado(cpf, clientes):
    cpf = limpar_cpf(cpf)

    for cliente in clientes:
        if limpar_cpf(cliente["cpf"]) == cpf:
            return True

    return False


def solicitar_nome():
    while True:
        nome = input("Nome completo: ")

        try:
            return normalizar_nome(nome)

        except (ValueError, TypeError) as erro:
            print(f"Erro: {erro}")


def solicitar_cpf(clientes):
    while True:
        cpf = input("CPF: ").strip()

        if not cpf:
            print("Erro: o CPF não pode ficar vazio.")
            continue

        if not validar_cpf(cpf):
            print("Erro: CPF inválido. Digite um CPF válido.")
            continue

        if cpf_ja_cadastrado(cpf, clientes):
            print("Erro: este CPF já está cadastrado.")
            continue

        return formatar_cpf(cpf)


def solicitar_idade():
    while True:
        idade = input("Idade: ").strip()

        if not idade:
            print("Erro: a idade não pode ficar vazia.")
            continue

        try:
            idade = int(idade)

            if idade <= 0:
                print("Erro: a idade deve ser maior que zero.")
                continue

            return idade

        except ValueError:
            print("Erro: a idade deve ser informada com números inteiros.")


def solicitar_email():
    while True:
        email = input("E-mail: ").strip()

        if not email:
            print("Erro: o e-mail não pode ficar vazio.")
            continue

        if not validar_email(email):
            print("Erro: informe um e-mail válido. Exemplo: nome@email.com")
            continue

        return email.lower()


def solicitar_telefone():
    while True:
        telefone = input("Telefone com DDD: ").strip()

        if not telefone:
            print("Erro: o telefone não pode ficar vazio.")
            continue

        if not validar_telefone(telefone):
            print(
                "Erro: telefone inválido. "
                "Informe o DDD e o número, por exemplo: (81) 99999-9999."
            )
            continue

        return telefone


def cadastrar_cliente(clientes):
    print("\n=============================================")
    print("             CADASTRAR CLIENTE")
    print("=============================================")

    cliente = {
        "nome": solicitar_nome(),
        "cpf": solicitar_cpf(clientes),
        "idade": solicitar_idade(),
        "email": solicitar_email(),
        "telefone": solicitar_telefone()
    }

    clientes.append(cliente)

    print("\nCliente cadastrado com sucesso!")


def mostrar_cliente(cliente):
    print(f"Nome: {cliente['nome']}")
    print(f"CPF: {cliente['cpf']}")
    print(f"Idade: {cliente['idade']}")
    print(f"E-mail: {cliente['email']}")
    print(f"Telefone: {cliente['telefone']}")


def listar_clientes(clientes):
    print("\n=============================================")
    print("              LISTA DE CLIENTES")
    print("=============================================")

    if not clientes:
        print("Nenhum cliente cadastrado.")
        return

    for indice, cliente in enumerate(clientes, start=1):
        print(f"\nCliente {indice}")
        mostrar_cliente(cliente)
        print("-" * 45)


def pesquisar_cliente(clientes):
    print("\n=============================================")
    print("             PESQUISAR CLIENTE")
    print("=============================================")

    if not clientes:
        print("Nenhum cliente cadastrado.")
        return

    cpf = input("Digite o CPF do cliente: ").strip()

    if not cpf:
        print("Erro: o CPF não pode ficar vazio.")
        return

    if not validar_cpf(cpf):
        print("Erro: CPF inválido.")
        return

    cpf = limpar_cpf(cpf)

    for cliente in clientes:
        if limpar_cpf(cliente["cpf"]) == cpf:
            print("\nCliente encontrado:")
            mostrar_cliente(cliente)
            return

    print("Cliente não encontrado.")


def excluir_cliente(clientes):
    print("\n=============================================")
    print("              EXCLUIR CLIENTE")
    print("=============================================")

    if not clientes:
        print("Nenhum cliente cadastrado.")
        return

    cpf = input("Digite o CPF do cliente: ").strip()

    if not cpf:
        print("Erro: o CPF não pode ficar vazio.")
        return

    if not validar_cpf(cpf):
        print("Erro: CPF inválido.")
        return

    cpf = limpar_cpf(cpf)

    for cliente in clientes:
        if limpar_cpf(cliente["cpf"]) == cpf:
            print("\nCliente encontrado:")
            mostrar_cliente(cliente)

            confirmacao = input(
                "\nDeseja realmente excluir este cliente? (S/N): "
            ).strip().upper()

            if confirmacao == "S":
                clientes.remove(cliente)
                print("Cliente excluído com sucesso.")
            else:
                print("Exclusão cancelada.")

            return

    print("Cliente não encontrado.")


def mostrar_menu():
    print("\n=============================================")
    print("          SISTEMA DE CADASTRO")
    print("=============================================")
    print()
    print("1 - Cadastrar cliente")
    print("2 - Listar clientes")
    print("3 - Pesquisar cliente")
    print("4 - Excluir cliente")
    print("5 - Sair")


def executar_sistema():
    clientes = []

    while True:
        mostrar_menu()

        opcao = input("\nEscolha uma opção: ").strip()

        if opcao == "1":
            cadastrar_cliente(clientes)

        elif opcao == "2":
            listar_clientes(clientes)

        elif opcao == "3":
            pesquisar_cliente(clientes)

        elif opcao == "4":
            excluir_cliente(clientes)

        elif opcao == "5":
            print("\nSistema encerrado.")
            break

        else:
            print("\nErro: opção inválida. Escolha uma opção de 1 a 5.")


executar_sistema()