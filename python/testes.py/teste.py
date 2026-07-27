cpfs_cadastrados = set()

while True:
    cpf = input("Digite o CPF ou 'sair' para encerrar: ")

    if cpf.lower() == "sair":
        break

    cpf = cpf.strip().replace(".", "").replace("-", "")

    if cpf in cpfs_cadastrados:
        print("Esse CPF já foi cadastrado.")
    else:
        cpfs_cadastrados.add(cpf)
        print("CPF cadastrado com sucesso.")

print("CPFs cadastrados:", cpfs_cadastrados)