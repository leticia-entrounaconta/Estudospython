# Busca de Cliente por CPF

Este projeto realiza a busca de um cliente dentro de uma lista utilizando o CPF como identificador.

## Funcionalidades

O programa:

* Solicita o CPF ao usuário;
* Remove espaços, pontos e hífens;
* Percorre a lista de clientes;
* Compara o CPF informado com os CPFs cadastrados;
* Interrompe a busca ao encontrar o cliente;
* Exibe os dados do cliente encontrado;
* Informa quando o CPF não existe na lista.

## Estrutura dos dados

Cada cliente é representado por um dicionário contendo:

* Nome;
* CPF;
* Idade.

## Conceitos utilizados

* Listas;
* Dicionários;
* `input()`;
* Laço `for`;
* Condicionais;
* `strip()`;
* `replace()`;
* `None`;
* `break`.

## Exemplo de execução

```text
Digite o CPF do cliente: 987.654.321-00

Cliente encontrado.
Nome: Maria Souza
CPF: 98765432100
Idade: 34
```

Caso o CPF não seja encontrado:

```text
Cliente não encontrado com o CPF informado.
```

## Como executar

```bash
python nome_do_arquivo.py
```
