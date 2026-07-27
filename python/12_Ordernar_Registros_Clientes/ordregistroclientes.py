clientes = [
    {
        "nome": "Carlos Lima",
        "idade": 22,
        "data_cadastro": "2026-07-20"
    },
    {
        "nome": "Ana Pereira",
        "idade": 31,
        "data_cadastro": "2026-07-18"
    },
    {
        "nome": "Bruno Souza",
        "idade": 25,
        "data_cadastro": "2026-07-22"
    }
]

clientes_por_nome = sorted(                 #preserva a lista original, criando uma nova e sort modifica diretamente a original
    clientes,
    key=lambda cliente: cliente["nome"]
)
clientes_por_idade = sorted(
    clientes,
    key=lambda cliente: cliente["idade"]
)
clientes_por_cadastro = sorted(
    clientes,
    key=lambda cliente: cliente["data_cadastro"],
    reverse=True
)

print("ordem alfabética")

for cliente in clientes_por_nome:
    print(cliente["nome"])

print("\nOrdem por idade")

for cliente in clientes_por_idade:
    print(f'{cliente["nome"]} - {cliente["idade"]} anos')

print("\nCadastro mais recente")

for cliente in clientes_por_cadastro:
    print(f'{cliente["nome"]} -{cliente["data_cadastro"]}')