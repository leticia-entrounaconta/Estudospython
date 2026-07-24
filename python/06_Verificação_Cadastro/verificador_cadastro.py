casos_teste = [                       #lista
    {
        "nome": "João",
        "idade": 22,
        "usuario_ativo": True,
        "possui_permissao": True
    },
    {
        "nome": "",
        "idade": 25,
        "usuario_ativo": True,
        "possui_permissao": True
    },
    {
        "nome": "Maria",
        "idade": 17,
        "usuario_ativo": True,
        "possui_permissao": True
    },
    {
        "nome": "Carlos",
        "idade": 30,
        "usuario_ativo": False,
        "possui_permissao": True
    },
    {
        "nome": "Ana",
        "idade": 28,
        "usuario_ativo": True,
        "possui_permissao": False
    }
]

#definindo variavel 
def verificar_cadastros(lista_de_cadastros):

    for cadastro in lista_de_cadastros:

        nome = cadastro["nome"]
        idade = cadastro["idade"]
        usuario_ativo = cadastro["usuario_ativo"]
        possui_permissao = cadastro["possui_permissao"]

        if not nome: #se não informar nome
            print("Acesso negado: nome não informado.")

        elif idade < 18: #se o nome não estiver vazio mas idade não +18 negar
            print("Acesso negado: idade mínima não atingida.")

        elif not usuario_ativo: #se o nome estiver ok e a idade também , verifcar se o usuário está ativo,caso não negar
            print("Acesso negado: usuário inativo.")

        elif not possui_permissao:
            print("Acesso negado: usuário sem permissão.")

        else:
            print(f"Acesso permitido para {nome}.") 
#f-string para inserir variáveis em um texto

verificar_cadastros(casos_teste)