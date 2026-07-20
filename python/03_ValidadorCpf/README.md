# 🪪 Validador de CPF em Python

Projeto desenvolvido em Python para verificar se um CPF informado pelo usuário é válido.

O programa remove caracteres de formatação, verifica a quantidade de dígitos, impede sequências inválidas e calcula os dois dígitos verificadores do CPF.

---

## 📌 Funcionalidades

O programa realiza as seguintes verificações:

* remove pontos e hífen do CPF;
* remove espaços no início e no final;
* verifica se o CPF possui exatamente 11 dígitos;
* verifica se o CPF contém apenas números;
* rejeita CPFs com todos os números iguais;
* calcula o primeiro dígito verificador;
* calcula o segundo dígito verificador;
* compara os dígitos calculados com os dígitos informados;
* retorna `True` para CPF válido;
* retorna `False` para CPF inválido.

---

## 🖥️ Exemplo de execução

Ao executar o programa, será exibido:

```text
========== Validador de CPF ==========
Digite o CPF:
```

Exemplo de resultado:

```text
========== Validador de CPF ==========
Digite o CPF: 000.000.000-00
CPF inválido.
```

O CPF pode ser digitado com ou sem pontuação.

Exemplos de formatos aceitos:

```text
123.456.789-00
```

```text
12345678900
```

---

## 🚀 Como executar o projeto

### Pré-requisitos

É necessário ter o Python instalado no computador.

Para verificar a instalação, utilize:

```bash
python --version
```

No Windows, também pode ser utilizado:

```bash
py --version
```

### Executando o programa

1. Faça o download ou clone este repositório.
2. Abra o terminal na pasta do projeto.
3. Execute o arquivo Python.

Exemplo:

```bash
python validador_cpf.py
```

Ou:

```bash
py validador_cpf.py
```

---

## 📂 Estrutura do projeto

```text
validador-de-cpf/
│
├── validador_cpf.py
└── README.md
```

---

## 🧠 Como o programa funciona

O programa possui uma função chamada:

```python
validar_cpf(cpf)
```

Essa função recebe um CPF e retorna:

```python
True
```

quando o CPF é válido.

Ou:

```python
False
```

quando o CPF é inválido.

Exemplo:

```python
resultado = validar_cpf("12345678900")

print(resultado)
```

---

## 1. Remoção da formatação

O CPF pode ser informado com pontos e hífen:

```text
123.456.789-00
```

Porém, para realizar os cálculos, o programa precisa trabalhar somente com os números.

A limpeza é feita com:

```python
cpf = cpf.replace(".", "").replace("-", "").strip()
```

O método `.replace()` troca os caracteres informados por uma string vazia.

Exemplo:

```text
123.456.789-00
```

Após a limpeza:

```text
12345678900
```

O método `.strip()` remove espaços do início e do final.

Exemplo:

```text
   12345678900
```

Após o `.strip()`:

```text
12345678900
```

---

## 2. Verificação da quantidade de caracteres

Um CPF deve possuir exatamente 11 dígitos.

A validação é feita com:

```python
if len(cpf) != 11:
    return False
```

A função `len()` retorna a quantidade de caracteres.

Exemplos inválidos:

```text
123456789
```

```text
123456789000
```

Nos dois casos, a função retorna:

```python
False
```

---

## 3. Verificação de caracteres numéricos

O programa verifica se todos os caracteres são números:

```python
if not cpf.isdigit():
    return False
```

O método `.isdigit()` retorna `True` quando todos os caracteres são dígitos.

Exemplo inválido:

```text
123456789AB
```

Como existem letras, o CPF é considerado inválido.

---

## 4. Bloqueio de números repetidos

Sequências com todos os números iguais não são CPFs válidos.

Exemplos:

```text
00000000000
11111111111
22222222222
99999999999
```

A verificação é feita com:

```python
if cpf == cpf[0] * 11:
    return False
```

### Como essa comparação funciona

O trecho:

```python
cpf[0]
```

pega o primeiro caractere do CPF.

Se o CPF informado for:

```text
11111111111
```

Então:

```python
cpf[0]
```

será:

```text
1
```

O trecho:

```python
cpf[0] * 11
```

repete esse caractere 11 vezes:

```text
11111111111
```

Se o resultado for igual ao CPF completo, significa que todos os números são iguais.

---

## 5. Cálculo do primeiro dígito verificador

O primeiro dígito verificador é calculado utilizando os nove primeiros números do CPF.

Os pesos utilizados são:

```text
10, 9, 8, 7, 6, 5, 4, 3, 2
```

O programa percorre os primeiros nove dígitos:

```python
for indice in range(9):
    soma += int(cpf[indice]) * (10 - indice)
```

O `range(9)` gera os índices:

```text
0, 1, 2, 3, 4, 5, 6, 7, 8
```

Cada dígito é convertido para número utilizando:

```python
int(cpf[indice])
```

Depois, o número é multiplicado pelo peso correspondente.

---

## 6. Regra do primeiro dígito

Após realizar a soma, o primeiro dígito é calculado com:

```python
primeiro_digito = (soma * 10) % 11
```

O operador `%` retorna o resto de uma divisão.

Exemplo:

```python
25 % 11
```

Resultado:

```text
3
```

Caso o resultado seja `10`, ele deve ser transformado em `0`:

```python
if primeiro_digito == 10:
    primeiro_digito = 0
```

---

## 7. Cálculo do segundo dígito verificador

Para calcular o segundo dígito, são utilizados os dez primeiros dígitos do CPF.

Isso inclui:

* os nove números iniciais;
* o primeiro dígito verificador.

Os pesos utilizados são:

```text
11, 10, 9, 8, 7, 6, 5, 4, 3, 2
```

O cálculo é realizado com:

```python
for indice in range(10):
    soma += int(cpf[indice]) * (11 - indice)
```

Depois, o segundo dígito é calculado:

```python
segundo_digito = (soma * 10) % 11
```

Caso o resultado seja `10`, ele também é transformado em `0`:

```python
if segundo_digito == 10:
    segundo_digito = 0
```

---

## 8. Comparação dos dígitos verificadores

Após calcular os dois dígitos, o programa compara o resultado com os dois últimos números do CPF informado:

```python
return cpf[-2:] == f"{primeiro_digito}{segundo_digito}"
```

O trecho:

```python
cpf[-2:]
```

pega os dois últimos caracteres do CPF.

A f-string:

```python
f"{primeiro_digito}{segundo_digito}"
```

junta os dois dígitos calculados.

Se os valores forem iguais, a função retorna:

```python
True
```

Caso contrário:

```python
False
```

---

## ✅ Exemplo de uso da função

```python
cpf_informado = input("Digite o CPF: ")

if validar_cpf(cpf_informado):
    print("CPF válido.")
else:
    print("CPF inválido.")
```

A função pode ser utilizada em outros projetos, como:

* sistemas de cadastro;
* formulários;
* APIs;
* sistemas administrativos;
* aplicações web;
* automações;
* validações de planilhas.

---

## 🧩 Código completo

```python
def validar_cpf(cpf):
    cpf = cpf.replace(".", "").replace("-", "").strip()

    if len(cpf) != 11:
        return False

    if not cpf.isdigit():
        return False

    if cpf == cpf[0] * 11:
        return False

    soma = 0

    for indice in range(9):
        soma += int(cpf[indice]) * (10 - indice)

    primeiro_digito = (soma * 10) % 11

    if primeiro_digito == 10:
        primeiro_digito = 0

    soma = 0

    for indice in range(10):
        soma += int(cpf[indice]) * (11 - indice)

    segundo_digito = (soma * 10) % 11

    if segundo_digito == 10:
        segundo_digito = 0

    return cpf[-2:] == f"{primeiro_digito}{segundo_digito}"


print("========== Validador de CPF ==========")

cpf_digitado = input("Digite o CPF: ")

if validar_cpf(cpf_digitado):
    print("CPF válido.")
else:
    print("CPF inválido.")
```

---

## 🧪 Exemplos de entradas inválidas

### CPF com menos de 11 dígitos

```text
123456789
```

Resultado:

```text
CPF inválido.
```

### CPF com letras

```text
123456789AB
```

Resultado:

```text
CPF inválido.
```

### CPF com todos os números iguais

```text
11111111111
```

Resultado:

```text
CPF inválido.
```

### CPF vazio

```text
```

Resultado:

```text
CPF inválido.
```

---

## 🧠 Conceitos de Python utilizados

Neste projeto foram utilizados os seguintes conceitos:

* criação de funções;
* parâmetros;
* retorno com `return`;
* valores booleanos `True` e `False`;
* estruturas condicionais `if` e `else`;
* laço de repetição `for`;
* função `range()`;
* função `len()`;
* conversão de texto para inteiro com `int()`;
* operadores matemáticos;
* operador de módulo `%`;
* acesso a caracteres por índice;
* f-strings;
* métodos `.replace()`, `.strip()` e `.isdigit()`;
* entrada de dados com `input()`;
* saída de dados com `print()`.

---

## ⚠️ Observação importante

Este projeto verifica se a estrutura matemática do CPF é válida.

Isso não significa que o CPF:

* pertença a uma pessoa específica;
* esteja ativo;
* esteja regular na Receita Federal;
* tenha sido realmente emitido.

Para verificar a situação cadastral de um CPF, é necessário utilizar um serviço oficial autorizado.

---

## 🔧 Possíveis melhorias futuras

Algumas melhorias que podem ser adicionadas:

* permitir outros tipos de espaços no CPF;
* criar uma função para formatar o CPF;
* validar se o valor recebido é uma string;
* criar testes automatizados;
* permitir várias validações sem encerrar o programa;
* organizar o projeto em módulos;
* criar uma interface gráfica;
* criar uma API;
* integrar a validação a um formulário;
* adicionar mensagens de erro específicas.

---

## 🧪 Exemplo de testes automatizados

Uma melhoria futura seria criar testes utilizando `assert`:

```python
assert validar_cpf("11111111111") is False
assert validar_cpf("123") is False
assert validar_cpf("CPF inválido") is False
```

Também é possível utilizar bibliotecas de testes, como:

```text
unittest
pytest
```

---

## 📚 Objetivo do projeto

Este projeto foi criado para praticar fundamentos da linguagem Python, especialmente:

* funções;
* validação de dados;
* manipulação de strings;
* estruturas condicionais;
* laços de repetição;
* cálculos matemáticos;
* retorno de valores booleanos.

---

## 👩‍💻 Autora

Desenvolvido por **Leticia Monteiro** como projeto de estudo em Python.
s