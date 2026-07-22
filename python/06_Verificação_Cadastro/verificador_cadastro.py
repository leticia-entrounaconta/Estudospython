                                                               #Input -> inserir
print("          CONTROLE DE ACESSO")                          #strip -> remover espaços no incio e final do texto
                                                               #upper -> converter letras minúsculas de uma string em maiúsculas
nome = input("Digite o nome: ").strip()                        #if -> condição 
                                                               #isdigit() -> verifica se todos caracteres são números
idade_texto = input("Digite a idade: ").strip()                #tiltle deixa a primeira letra de cada palavra em maiúscula
                                                               #if -> se, elif -> se não, else -> senão,
resposta_ativo = input(
    "O usuário está ativo? (S/N): "
).strip().upper() #upper está sendo usado para se o usuário digitar minúsculo o programa transformar em maiúsculo o s / n

resposta_permissao = input(
    "O usuário possui permissão? (S/N): "
).strip().upper()

usuario_ativo = resposta_ativo == "S"
possui_permissao = resposta_permissao == "S"


if not nome:  #if signfica se, e not nome verifica se o nome está vazio
    print("Acesso negado: nome não informado.")

elif not idade_texto.isdigit():
    print("Acesso negado: idade inválida.")

else:
    idade = int(idade_texto)

    if idade < 18:
        print("Acesso negado: idade mínima não atingida.")

    elif not usuario_ativo:
        print("Acesso negado: usuário inativo.")

    elif not possui_permissao:
        print("Acesso negado: usuário sem permissão.")

    else:
        nome = nome.title()                                   
        print(f"Acesso permitido para {nome}.") #F-string-> coloca-se um f antes da string e o nome da variável dentro das chaves