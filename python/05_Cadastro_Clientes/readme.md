# Sistema de Cadastro de Clientes

Projeto desenvolvido em Python para realizar o cadastro e o gerenciamento básico de clientes por meio do terminal.

O sistema permite cadastrar, listar, pesquisar e excluir clientes, aplicando validações para evitar dados incorretos.

## Funcionalidades

### Cadastrar cliente

Permite cadastrar um novo cliente informando:

* nome completo;
* CPF;
* idade;
* e-mail;
* telefone.

Antes de salvar, o sistema verifica se os dados são válidos.

### Listar clientes

Exibe todos os clientes cadastrados, mostrando suas principais informações.

Caso não exista nenhum cadastro, o sistema informa que a lista está vazia.

### Pesquisar cliente

A pesquisa é realizada pelo CPF.

Quando o cliente é encontrado, o sistema apresenta todos os seus dados. Caso contrário, exibe uma mensagem informando que o cliente não foi localizado.

### Excluir cliente

Permite excluir um cliente utilizando o CPF.

Antes da exclusão, o sistema solicita uma confirmação para evitar que o cadastro seja removido por engano.

### Sair

Encerra a execução do programa.

## Validações

### Nome

O nome não pode estar vazio, conter números ou símbolos inválidos.

Também é normalizado, removendo espaços duplicados e ajustando letras maiúsculas e minúsculas.

Exemplo:

```text
Entrada:  MARIA   DA   SILVA
Saída: Maria da Silva
```

### CPF

O CPF deve:

* possuir 11 dígitos;
* conter apenas números;
* ter dígitos verificadores válidos;
* não possuir todos os números iguais;
* não estar cadastrado anteriormente.

O CPF pode ser informado com ou sem pontuação.

### Idade

A idade deve ser um número inteiro maior que zero.

Valores vazios, negativos, iguais a zero ou com letras não são aceitos.

### E-mail

O e-mail deve:

* conter apenas um `@`;
* possuir texto antes e depois do `@`;
* conter um domínio válido;
* não possuir espaços.

Exemplo válido:

```text
cliente@email.com
```

### Telefone

O telefone deve possuir DDD e conter:

* 10 dígitos para telefone fixo;
* 11 dígitos para celular.

O sistema também impede letras, números repetidos e formatos inválidos.

## Estrutura dos dados

Cada cliente é armazenado em um dicionário:

```python
cliente = {
    "nome": "Maria da Silva",
    "cpf": "000.000.000-00",
    "idade": 25,
    "email": "maria@email.com",
    "telefone": "(81) 99999-9999"
}
```

Os clientes são adicionados a uma lista:

```python
clientes = []
```

## Menu do sistema

```text
=============================================
          SISTEMA DE CADASTRO
=============================================

1 - Cadastrar cliente
2 - Listar clientes
3 - Pesquisar cliente
4 - Excluir cliente
5 - Sair
```

## Conceitos utilizados

O projeto utiliza conceitos importantes de Python, como:

* funções;
* listas;
* dicionários;
* estruturas condicionais;
* laços de repetição;
* tratamento de exceções;
* validação de dados;
* entrada e saída pelo terminal.

## Como executar

Salve o código em um arquivo chamado `main.py`.

Depois, execute no terminal:

```bash
python main.py
```

## Observação

Os clientes ficam armazenados apenas durante a execução do programa.

Ao fechar o sistema, os dados são apagados. Uma melhoria futura seria salvar os cadastros em um arquivo JSON, CSV ou banco de dados.

## 👩‍💻Autora

Desenvolvido por **Leticia Monteiro** como projeto de estudo em Python.
