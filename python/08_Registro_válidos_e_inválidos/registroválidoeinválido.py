registros = [                                         #lista 

    {"nome": "Ana", "cpf": "12345678901", "idade": 25},
    {"nome": "", "cpf": "98765432100", "idade": 30},
    {"nome": "Carlos", "cpf": "12345", "idade": 17},   #dicionário 
    {"nome": "Maria", "cpf": None, "idade": 40},
]

registros_validos = [] #essa lista recebe o registros que passarem por todas verificações 
registros_invalidos = [] #essa lista receberá registros que tiverem algum problema 

for numero, registro in enumerate(registros, start=1):#A parte For cria duas variáveis temporárias, numero guarda a posição de registro, registro guarda o registro que está sendo usado aquele momento
 #permite que eu percorrar a lista e também obtenha a númeração de cada item
    nome = registro["nome"] #aqui o programa vai pegar o nome do registro
    cpf = registro["cpf"] #aqui o cpf
    idade = registro["idade"] #aqui a idade

    motivos = []
    #aqui criamos a lista vazia para armazenar problemas encontrados
    #ela foi criada dentro do for,assim, cada registro terá sua própria lista de motivos.
    
    if nome is None or nome.strip() == "": #O if significa se essa condição for verdade,o nome possuir o valor none execute o abaixo:
        motivos.append("Nome não informado") #verificando se o nome tá vazio
                                            #strip remove o espaço do incio e do final     
                                            #.append adiciona o valor ao final de uma lista existente
    if cpf is None or cpf == "":
        motivos.append("CPF não informado") #se o cpf estiver vazio ou none o programa adiciona esse motivo à lista
    elif len(cpf) != 11: #caso a condição anterior não seja verdadeira, verifique esta outra condição. A condição verifica os caracteres
        motivos.append("CPF inválido")

    
    if idade is None:
        motivos.append("Idade não informada")
    elif idade < 18: #Caso a condição anterior não seja verdadeira, verifique esta outra condição
        motivos.append("Pessoa menor de idade")

     
    if motivos:
        registros_invalidos.append({
            "numero": numero,
            "registro": registro,
            "motivos": motivos
        })

    
    else:
        registros_validos.append(registro)


print(f"Total de registros: {len(registros)}")
print(f"Registros válidos: {len(registros_validos)}")
print(f"Registros inválidos: {len(registros_invalidos)}")


print("\nRegistros válidos:")

for registro in registros_validos:       #essa parte percorre a lista de registros válidos e mostra o nome e cpf de cada pessoa
    print(f'{registro["nome"]} - {registro["cpf"]}')


print("\nRegistros inválidos:")

for item in registros_invalidos:
    numero = item["numero"]
    motivos = item["motivos"]

    texto_motivos = " e ".join(motivos) #o join aqui serve para juntar vários rextos de uma lista e transformá-los em um único texto.

    print(f"Registro {numero}: {texto_motivos}.")
    