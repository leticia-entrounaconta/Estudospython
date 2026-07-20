# 💱 Conversor de Moedas em Python

Projeto desenvolvido em Python para realizar conversões entre **Real, Dólar e Euro** utilizando cotações informadas pelo usuário.

O programa funciona pelo terminal e permite selecionar o tipo de conversão, informar a cotação atual da moeda e inserir o valor que será convertido.

---

## 📌 Funcionalidades

O programa permite realizar as seguintes conversões:

1. Real para dólar;
2. Dólar para real;
3. Real para euro;
4. Euro para real.

Além disso, o sistema:

* aceita valores com ponto ou vírgula;
* verifica se a opção escolhida é válida;
* verifica se a cotação informada é maior que zero;
* exibe o resultado com duas casas decimais;
* encerra o programa quando uma informação inválida é identificada.

---

## 🖥️ Exemplo do menu

Ao executar o programa, será apresentado o seguinte menu:

```text
========= Conversor de Moedas =========

Escolha a conversão:
1. Real para dólar
2. Dólar para real
3. Real para euro
4. Euro para real

Escolha uma opção:
```

---

## 🚀 Como executar o projeto

### Pré-requisitos

Para executar o programa, é necessário ter o Python instalado no computador.

Você pode verificar a instalação utilizando o comando:

```bash
python --version
```

Ou, dependendo da configuração do computador:

```bash
py --version
```

### Executando o programa

1. Faça o download ou clone este repositório.
2. Abra o terminal na pasta do projeto.
3. Execute o arquivo Python.

Exemplo:

```bash
python conversor_moedas.py
```

No Windows, também pode ser utilizado:

```bash
py conversor_moedas.py
```

---

## 💵 Exemplo: Real para dólar

Considere:

* opção escolhida: `1`;
* cotação do dólar: `5,50`;
* valor em reais: `100`.

Entrada:

```text
Escolha uma opção: 1
Digite a cotação do dólar. Exemplo 5.50: 5,50
Digite o valor que deseja converter: 100
```

Cálculo realizado:

```text
100 ÷ 5,50 = 18,18
```

Resultado:

```text
Resultado: US$ 18.18
```

---

## 💰 Exemplo: Dólar para real

Considere:

* opção escolhida: `2`;
* cotação do dólar: `5,50`;
* valor em dólares: `100`.

Entrada:

```text
Escolha uma opção: 2
Digite a cotação do dólar. Exemplo 5.50: 5,50
Digite o valor que deseja converter: 100
```

Cálculo realizado:

```text
100 × 5,50 = 550
```

Resultado:

```text
Resultado: R$ 550.00
```

---

## 💶 Exemplo: Real para euro

Considere:

* opção escolhida: `3`;
* cotação do euro: `6,50`;
* valor em reais: `100`.

Entrada:

```text
Escolha uma opção: 3
Digite a cotação do euro. Exemplo 6.50: 6,50
Digite o valor que deseja converter: 100
```

Cálculo realizado:

```text
100 ÷ 6,50 = 15,38
```

Resultado:

```text
Resultado: € 15.38
```

---

## 💶 Exemplo: Euro para real

Considere:

* opção escolhida: `4`;
* cotação do euro: `6,50`;
* valor em euros: `100`.

Entrada:

```text
Escolha uma opção: 4
Digite a cotação do euro. Exemplo 6.50: 6,50
Digite o valor que deseja converter: 100
```

Cálculo realizado:

```text
100 × 6,50 = 650
```

Resultado:

```text
Resultado: R$ 650.00
```

---

## 🧮 Regras de conversão

### Real para dólar

O valor em reais é dividido pela cotação do dólar:

```python
resultado = valor / cotacao_dolar
```

### Dólar para real

O valor em dólares é multiplicado pela cotação do dólar:

```python
resultado = valor * cotacao_dolar
```

### Real para euro

O valor em reais é dividido pela cotação do euro:

```python
resultado = valor / cotacao_euro
```

### Euro para real

O valor em euros é multiplicado pela cotação do euro:

```python
resultado = valor * cotacao_euro
```

---

## 🔄 Aceitando ponto ou vírgula

O programa utiliza o método `.replace()` para substituir vírgulas por pontos antes da conversão para `float`.

Exemplo:

```python
input("Digite a cotação: ").replace(",", ".")
```

Dessa forma, as duas entradas abaixo são aceitas:

```text
5.50
```

```text
5,50
```

Após a substituição, o valor é convertido para número decimal:

```python
cotacao_dolar = float(
    input("Digite a cotação do dólar: ").replace(",", ".")
)
```

---

## ✅ Validação da cotação

O programa verifica se a cotação informada é menor ou igual a zero:

```python
if cotacao_dolar <= 0:
    print("Erro: a cotação deve ser maior que zero.")
    exit()
```

A mesma verificação é realizada para o euro.

Exemplos de valores inválidos:

```text
0
```

```text
-5.50
```

Quando isso acontece, o programa apresenta uma mensagem de erro e encerra a execução.

---

## ❌ Validação da opção escolhida

As opções válidas são:

```text
1
2
3
4
```

Caso o usuário informe outro valor, o programa executa o bloco `else`:

```python
else:
    print("Erro: opção inválida!")
    exit()
```

Exemplo:

```text
Escolha uma opção: 8
Erro: opção inválida!
```

---

## 🎯 Formatação do resultado

O resultado é exibido utilizando uma `f-string`:

```python
print(f"Resultado: R$ {resultado:.2f}")
```

O trecho:

```python
{resultado:.2f}
```

faz com que o valor seja apresentado com duas casas decimais.

Exemplo:

```text
18.1818181818
```

É exibido como:

```text
18.18
```

---

## 🧠 Conceitos de Python utilizados

Neste projeto foram utilizados os seguintes conceitos:

* `print()` para exibir informações;
* `input()` para receber dados do usuário;
* variáveis;
* conversão de texto para número com `float()`;
* estruturas condicionais `if`, `elif` e `else`;
* operadores de comparação;
* operadores matemáticos;
* operador lógico `or`;
* método `.replace()`;
* formatação com `f-string`;
* encerramento do programa com `exit()`.

---

## 📂 Estrutura do projeto

```text
conversor-de-moedas/
│
├── conversor_moedas.py
└── README.md
```

---

## ⚠️ Limitações atuais

A cotação das moedas não é consultada automaticamente.

O usuário precisa informar manualmente a cotação atual do dólar ou do euro.

O programa também ainda não trata entradas como:

```text
cinco
```

Caso um texto não numérico seja informado no lugar da cotação ou do valor, o Python apresentará um erro do tipo:

```text
ValueError
```

---

## 🔧 Possíveis melhorias futuras

Algumas melhorias que podem ser adicionadas ao projeto:

* tratar entradas inválidas utilizando `try` e `except`;
* impedir valores negativos no campo de conversão;
* consultar cotações automaticamente por meio de uma API;
* adicionar outras moedas;
* permitir várias conversões sem encerrar o programa;
* criar funções para organizar melhor o código;
* apresentar os valores no formato monetário brasileiro;
* criar uma interface gráfica;
* registrar a data e a hora de cada conversão.

---

## 📚 Objetivo do projeto

Este projeto foi criado com o objetivo de praticar fundamentos da linguagem Python, especialmente:

* entrada e saída de dados;
* estruturas condicionais;
* operadores matemáticos;
* validação de informações;
* formatação de números;
* manipulação básica de strings.

---

## 👩‍💻 Autora

Desenvolvido por **Leticia Monteiro** como projeto de estudo em Python.
