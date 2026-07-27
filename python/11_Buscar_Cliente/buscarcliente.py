clientes = [
    {
        "nome": "João Silva",
        "cpf": "12345678901",
        "idade": 28
    },
    {
        "nome": "Maria Souza",
        "cpf": "98765432100",
        "idade": 34
    },
    {
        "nome": "Carlos Lima",
        "cpf": "45678912300",
        "idade": 22
    }
]


cpf_procurado = input("Digite o cpf do cliente: ") 

cpf_procurado = cpf_procurado.strip()            #remove espaços no início e no final
cpf_procurado = cpf_procurado.replace(".", "")
cpf_procurado = cpf_procurado.replace("-", "") #replace remove pontos e hífens

cliente_encontrado = None

for cliente in clientes:
    if cliente["cpf"] == cpf_procurado: #consulta cpf do dicionário 

        cliente_encontrado = cliente
        break

if cliente_encontrado is not None:
    print("\nCliente encontrado.")
    print("Nome:",cliente_encontrado["nome"])
    print("Cpf:", cliente_encontrado["nome"])
    print("Idade:", cliente_encontrado["idade"])

else:
    print("\n Cliente não encontrado com CPF informado.")