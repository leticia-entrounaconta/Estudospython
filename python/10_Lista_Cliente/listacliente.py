clientes = [ #lista
    {
        "nome": "João Silva",
        "cpf": "12345678901",                #cada cliente é representado por um dicionário
        "idade": 28,
        "ativo": True
    },
    {
        "nome": "Maria Souza",
        "cpf": "98765432100",
        "idade": 34,
        "ativo": False
    },
    {
        "nome": "Carlos Lima",
        "cpf": "45678912300",
        "idade": 22,
        "ativo": True
    }
]

print("Clientes cadastrados")

for cliente in clientes:
    print("Nome:", cliente["nome"])
    print("Cpf:", cliente["cpf"])
    print("Idade:", cliente["idade"])

    if cliente["ativo"]:
        print("Status: Ativo")
    else:
        print("Status: Inativo")

    print()

print("Total de clientes:", len(clientes))

novo_cliente = {
        "nome": "Ana Pereira",
        "cpf": "11122233344",
        "idade": 25,
        "ativo": True
    }

clientes.append(novo_cliente)

print("Cliente adicionado com sucesso.")

for cliente in clientes:
    if cliente["cpf"] == "98765432100":
        cliente["ativo"] = True
        print("Cliente encontrado:", cliente["nome"])
        print("Status atualizado com sucesso.")
        break
cliente_para_remover = None

for cliente in clientes:
     if cliente["cpf"] == "45678912300":
         cliente_para_remover = cliente
         break

if cliente_para_remover is not None:
   clientes.remove(cliente_para_remover)

   print(
       f'Cliente {cliente_para_remover["nome"]} removido com sucesso.'
   )

print("\nLista atualizada:")

for cliente in clientes:
    if cliente["ativo"]:
        status="Ativo"
    else:
        status = "Inativo"

    print(f'{cliente["nome"]} - {status}')