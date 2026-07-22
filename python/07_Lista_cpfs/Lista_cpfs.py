cpfs = [
    "12345678901", #11 caracteres 
    "98765432100",      #--
    "", #string vazia 
    "12345", #incompleto 
    None #ausencia de uma informação
]

for cpf in cpfs: 
    if cpf is None or cpf == "":  #verifica se o cpf não foi informado,is none -> verificar se o valor é none e  cpf == "", verifica se o valor é uma string vazia
        print("Cpf vazio. Registro ignorado.")   # O or significa Ou, portanto, a condição sera verdadeira quando o cpf for none ou estiver vazio 
        continue
    if len(cpf) != 11: #verifica a quantidade de caracteres #len -> é usada para retornar o tamanho ou o número de itens de um objeto, nesse caso ele conta os caracteres
        print(f"CPF {cpf} possui quantidade inválida de caracteres.") # E o f antes das aspas serve para inserir o valor da variável dentro do texto 
        continue

    print(f"processando cpf: {cpf}")
print(f"Total de registros recebidos;{len(cpfs)}") #nesse caso o len está sendo aplicado para lista inteira (resposta 5)