print("========= Conversor de Moedas =========")

print("\nEscolha a conversão:")
print("1. Real para dólar")
print("2. Dólar para real")
print("3. Real para euro")
print("4. Euro para real")

opcao_moeda = input("\nEscolha uma opção: ")

# Opções que utilizam dólar, verifica se a opção escolhida é 1 ou 2.As duas opções utilizam a cotação do dólar.
if opcao_moeda == "1" or opcao_moeda == "2":
    cotacao_dolar = float(
        input(
            "Digite a cotação do dólar. Exemplo 5.50: "
        ).replace(",", ".") #O .replace(",", ".") troca a vírgula por ponto.
    )

    if cotacao_dolar <= 0: #verifica se a cotação do dólar é menor ou igual a zero
        print("Erro: a cotação deve ser maior que zero.") #mostra mensagem de erro caso a cotação seja menor ou igual a zero
        exit() #encerra o programa

# Opções que utilizam euro (3 ou 4)
elif opcao_moeda == "3" or opcao_moeda == "4":
    cotacao_euro = float(
        input(
            "Digite a cotação do euro. Exemplo 6.50: "
        ).replace(",", ".")  #O .replace(",", ".") troca a vírgula por ponto.
    )

    if cotacao_euro <= 0: # Verifica se a cotação é zero ou negativa.
        print("Erro: a cotação deve ser maior que zero.")
        exit()

# Executado se a opção não estiver entre 1 e 4
else:
    print("Erro: opção inválida!")
    exit() #encerra o programa

valor = float(
    input("Digite o valor que deseja converter: ").replace(",", ".") #O .replace(",", ".") troca a vírgula por ponto.
)

if opcao_moeda == "1":
    resultado = valor / cotacao_dolar
    print(f"Resultado: US$ {resultado:.2f}")

elif opcao_moeda == "2":
    resultado = valor * cotacao_dolar
    print(f"Resultado: R$ {resultado:.2f}")

elif opcao_moeda == "3":
    resultado = valor / cotacao_euro
    print(f"Resultado: € {resultado:.2f}")

elif opcao_moeda == "4":
    resultado = valor * cotacao_euro
    print(f"Resultado: R$ {resultado:.2f}")