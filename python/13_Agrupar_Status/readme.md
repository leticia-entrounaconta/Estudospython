# Agrupamento de Resultados por Status

Este projeto organiza registros de processamento de acordo com o status de cada CPF.

## Funcionalidades

O programa:

* Percorre uma lista de resultados;
* Identifica o status de cada registro;
* Cria automaticamente um grupo para cada status;
* Adiciona os registros no grupo correspondente;
* Exibe a quantidade de registros por status;
* Mostra os CPFs pertencentes a cada grupo.

## Estrutura dos dados

Cada registro é representado por um dicionário contendo:

* CPF;
* Status do processamento.

Exemplo:

```python
{
    "cpf": "12345678901",
    "status": "sucesso"
}
```

## Conceitos utilizados

* Listas;
* Dicionários;
* Estruturas aninhadas;
* Laço `for`;
* Método `setdefault()`;
* Método `append()`;
* Método `items()`;
* Função `len()`.

## Funcionamento

O método `setdefault()` verifica se o status já existe no dicionário.

Caso não exista, ele cria uma nova chave com uma lista vazia:

```python
resultados_agrupados.setdefault(status, [])
```

Depois, o registro é adicionado ao grupo correto:

```python
resultados_agrupados[status].append(resultado)
```

## Exemplo de saída

```text
Status: sucesso
Quantidade: 2
CPFs:
- 12345678901
- 11122233344

Status: erro
Quantidade: 2
CPFs:
- 98765432100
- 55566677788

Status: pendente
Quantidade: 1
CPFs:
- 45678912300
```

## Como executar

```bash
python nome_do_arquivo.py
```
