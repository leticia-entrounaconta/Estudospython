# Ordenação de Clientes

Este projeto cria diferentes ordenações para uma lista de clientes sem modificar a lista original.

## Funcionalidades

O programa organiza os clientes:

* Em ordem alfabética pelo nome;
* Do mais novo para o mais velho;
* Do cadastro mais recente para o mais antigo.

## Estrutura dos dados

Cada cliente é representado por um dicionário contendo:

* Nome;
* Idade;
* Data de cadastro.

## Conceitos utilizados

* Listas;
* Dicionários;
* `sorted()`;
* `lambda`;
* `reverse=True`;
* Laço `for`;
* F-strings.

## Funcionamento

A função `sorted()` cria uma nova lista ordenada, preservando a lista original.

O parâmetro `key` define qual campo será usado na ordenação:

```python
key=lambda cliente: cliente["nome"]
```

O atributo `reverse=True` inverte a ordem, sendo utilizado para mostrar os cadastros mais recentes primeiro.

## Exemplo de saída

```text
Ordem alfabética
Ana Pereira
Bruno Souza
Carlos Lima

Ordem por idade
Carlos Lima - 22 anos
Bruno Souza - 25 anos
Ana Pereira - 31 anos

Cadastro mais recente
Bruno Souza - 2026-07-22
Carlos Lima - 2026-07-20
Ana Pereira - 2026-07-18
```

## Como executar

```bash
python nome_do_arquivo.py
```
