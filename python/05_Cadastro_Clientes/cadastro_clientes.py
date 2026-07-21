import re


def normalizar_nome(nome):
    """Remove espaços duplicados e padroniza o nome."""
    nome = " ".join(nome.strip().split())

    if not nome:
        raise ValueError("O nome não pode ficar vazio.")

    caracteres_permitidos = {" ", "-", "'",}

    for caractere in nome:
        if not caractere.isalpha() and caractere not in caracteres_permitidos:
            raise ValueError("O nome contém caracteres inválidos.")

    return nome.title()


def limpar_cpf(cpf):
    """Remove pontos, traços e outros caracteres do CPF."""
    return re.sub(r"\D", "", cpf)


def validar_cpf(cpf):
    """Verifica se o CPF é válido."""
    cpf = limpar_cpf(cpf)

    if len(cpf) != 11:
        return False

    if cpf == cpf[0] * 11:
        return False

    soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
    primeiro_digito = (soma * 10) % 11

    if primeiro_digito == 10:
        primeiro_digito = 0

    if primeiro_digito != int(cpf[9]):
        return False

    soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
    segundo_digito = (soma * 10) % 11

    if segundo_digito == 10:
        segundo_digito = 0

    return segundo_digito == int(cpf[10])


def formatar_cpf(cpf):
    """Formata o CPF no padrão 000.000.000-00."""
    cpf = limpar_cpf(cpf)

    return f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"


def cpf_ja_cadastrado(cpf, clientes):
    """Verifica se o CPF já foi cadastrado."""
    cpf = limpar_cpf(cpf)

    for cliente in clientes:
        if limpar_cpf(cliente["cpf"]) == cpf:
            return True

    return False


def solicitar_nome():
    while True:
        try:
            nome = input("Nome completo: ")
            return normalizar_nome(nome)

        except ValueError as erro:
            print(f"Erro: {erro}")


def solicitar_cpf(clientes):
    while True:
        cpf = input("CPF: ").strip()

        if not cpf:
            print("Erro: o CPF não pode ficar vazio.")

        elif not validar_cpf(cpf):
            print("Erro: CPF inválido.")

        elif cpf_ja_cadastrado(cpf, clientes):
            print("Erro: este CPF já está cadastrado.")

        else:
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
            else:
                return idade

        except ValueError:
            print("Erro: informe a idade usando números inteiros.")


def solicitar_email():
    while True:
        email = input("E-mail: ").strip()

        if not email:
            print("Erro: o e-mail não pode ficar vazio.")

        elif "@" not in email:
            print("Erro: o e-mail deve conter @.")

        else:
            return email.lower()


def solicitar_telefone():
    while True:
        telefone = input("Telefone: ").strip()

        if not telefone:
            print("Erro: o telefone não pode ficar vazio.")
        else:
            return telefone


def cadastrar_cliente(clientes):
    print("\n========== CADASTRO DE CLIENTE ==========")

    cliente = {
        "nome": solicitar_nome(),
        "cpf": solicitar_cpf(clientes),
        "idade": solicitar_idade(),
        "email": solicitar_email(),
        "telefone": solicitar_telefone()
    }

    clientes.append(cliente)

    print("\nCliente cadastrado com sucesso!")


def listar_clientes(clientes):
    print("\n========== LISTA DE CLIENTES ==========")

    if not clientes:
        print("Nenhum cliente cadastrado.")
        return

    for indice, cliente in enumerate(clientes, start=1):
        print(f"\nCliente {indice}")
        print(f"Nome: {cliente['nome']}")
        print(f"CPF: {cliente['cpf']}")
        print(f"Idade: {cliente['idade']}")
        print(f"E-mail: {cliente['email']}")
        print(f"Telefone: {cliente['telefone']}")
        print("-" * 40)


def pesquisar_cliente(clientes):
    print("\n========== PESQUISAR CLIENTE ==========")

    if not clientes:
        print("Nenhum cliente cadastrado.")
        return

    cpf_pesquisa = input("Digite o CPF do cliente: ").strip()

    if not cpf_pesquisa:
        print("Erro: o CPF não pode ficar vazio.")
        return

    cpf_pesquisa = limpar_cpf(cpf_pesquisa)

    for cliente in clientes:
        if limpar_cpf(cliente["cpf"]) == cpf_pesquisa:
            print("\nCliente encontrado:")
            print(f"Nome: {cliente['nome']}")
            print(f"CPF: {cliente['cpf']}")
            print(f"Idade: {cliente['idade']}")
            print(f"E-mail: {cliente['email']}")
            print(f"Telefone: {cliente['telefone']}")
            return

    print("Cliente não encontrado.")


def excluir_cliente(clientes):
    print("\n========== EXCLUIR CLIENTE ==========")

    if not clientes:
        print("Nenhum cliente cadastrado.")
        return

    cpf_exclusao = input("Digite o CPF do cliente: ").strip()

    if not cpf_exclusao:
        print("Erro: o CPF não pode ficar vazio.")
        return

    cpf_exclusao = limpar_cpf(cpf_exclusao)

    for cliente in clientes:
        if limpar_cpf(cliente["cpf"]) == cpf_exclusao:
            confirmacao = input(
                f"Deseja excluir o cliente {cliente['nome']}? (S/N): "
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
            print("\nOpção inválida. Escolha uma opção de 1 a 5.")


executar_sistema()