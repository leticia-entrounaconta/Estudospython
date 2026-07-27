def remover_clientes_duplicados(lista_clientes):
    cpfs_vistos = set()
    clientes_unicos = []
    
    for cliente in lista_clientes:
        cpf = cliente.get('cpf')
        if cpf not in cpfs_vistos:
            cpfs_vistos.add(cpf)
            clientes_unicos.append(cliente)
            
    return clientes_unicos

# Exemplo de uso:
dados_clientes = [
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
resultado = remover_clientes_duplicados(dados_clientes)
print(resultado)