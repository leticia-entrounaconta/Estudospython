clientes = [
    {
        "nome": "João Silva",
        "cpf": "12345678901"
    },
    {
        "nome": "Maria Souza",
        "cpf": "98765432100"
    },
    {
        "nome": "João Silva",
        "cpf": "12345678901"
    },
    {
        "nome": "Carlos Lima",
        "cpf": "45678912300"
    },
    {
        "nome": "Maria Souza",
        "cpf": "98765432100"
    }
]

cpfs_encontrados = set()

clientes_sem_duplicidade = []

duplicados_removidos = 0

for cliente in clientes:
    cpf = cliente["cpf"]

    if cpf not in cpfs_encontrados:
        cpfs_encontrados.add(cpf)
        clientes_sem_duplicidade.append(cliente)
    else:
        duplicados_removidos +=1
print("Clientes sem duplicidade:")

for cliente in clientes_sem_duplicidade:
    print(f'{(cliente ["nome"])} - {cliente["cpf"]}')

print(
    "\nTotal de registros recebidos:",
    len(clientes)
)

print(
    "Total de Clientes únicos:",
    len(clientes_sem_duplicidade)

)

print(
    "Total de duplicaods recebidos:",
    duplicados_removidos
)