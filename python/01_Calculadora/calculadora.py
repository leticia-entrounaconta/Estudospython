
print("==========Calculadora==========")            #mostrar na tela.
num1 = float(input("Digite o primeiro número: "))  #convertendo o texto em número decimal.
num2 = float(input("Digite o segundo número: "))          

print("Operações")                              #mostrar na tela.
print("1. Adição")
print("2. Subtração")
print("3. Multiplicação")   
print("4. Divisão")

operação = input("Escolha a operação: ")

if (operação == "1"):  #Uma condição permite que o programa tome uma decisão.
    resultado = num1 + num2
    print("Resultado:", resultado)
elif (operação == "2"):
    resultado = num1 - num2
    print("Resultado:", resultado)
elif (operação == "3"):
    resultado = num1 * num2
    print("Resultado:", resultado)
elif (operação == "4"):
    if (num2 != 0):
        resultado = num1 / num2
        print("Resultado:", resultado)
    else: 
        print("erro: número é zero")
else:
    print("números inválidos")