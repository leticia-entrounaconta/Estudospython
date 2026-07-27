resultados = [
    {
        "cpf": "12345678901",
        "status": "sucesso"
    },
    {
        "cpf": "98765432100",
        "status": "erro"
    },
    {
        "cpf": "45678912300",
        "status": "pendente"
    },
    {
        "cpf": "11122233344",
        "status": "sucesso"
    },
    {
        "cpf": "55566677788",
        "status": "erro"
    }
]

resultados_agrupados = {}

for resultado in resultados:

    status = resultado["status"]

    resultados_agrupados.setdefault(status, []) #Se a chave status ainda não existir no dicionário, crie essa chave com uma lista vazia

    resultados_agrupados[status].append(resultado)

for status, lista_resultados in resultados_agrupados.items():

    print("Status:", status)

    print("Quantidade:", len(lista_resultados))

    print("CPFs:")

    for resultado in lista_resultados:
        print("-", resultado["cpf"])

print()
