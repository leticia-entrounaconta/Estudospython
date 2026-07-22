
usuario_correto = "admin"
senha_correta = "123456"


tentativas = 0
limite_tentativas = 3

while tentativas < limite_tentativas:
    print(f"\n--- Tentativa {tentativas + 1} de {limite_tentativas} ---")
    usuario_digitado = input("Usuário: ")
    senha_digitado = input("Senha: ")

    if usuario_digitado == usuario_correto and senha_digitado == senha_correta:
        print("\nLogin realizado com sucesso! Bem vindo.")
        break #encerra o looping
    else:
        print("Usuário ou senha incorretos.")
        tentativas += 1 #inserir tentativa no contador


else: 
    print("\nNúmero máximo de tentativas atingido. Acesso bloqueado")

