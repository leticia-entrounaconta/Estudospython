# Remoção de Clientes Duplicados

Este projeto identifica e remove registros duplicados de uma lista de clientes utilizando o CPF como identificador único.

## Funcionalidades

O programa:

* Percorre todos os clientes cadastrados;
* Verifica se o CPF já foi processado;
* Mantém apenas o primeiro registro de cada CPF;
* Cria uma nova lista sem duplicidades;
* Conta quantos registros duplicados foram ignorados;
* Exibe os clientes únicos e os totais do processamento.

## Estrutura dos dados

Cada cliente é representado por um dicionário contendo:

* Nome;
* CPF.

Exemplo:

```python
{
    "nome": "João Silva",
    "cpf": "12345678901"
}
```

## Conceitos utilizados

* Listas;
* Dicionários;
* Conjuntos (`set`);
* Laço `for`;
* Operador `not in`;
* Método `add()`;
* Método `append()`;
* Função `len()`;
* Contador;
* F-strings.

## Funcionamento

O conjunto `cpfs_encontrados` armazena os CPFs que já foram processados:

```python
cpfs_encontrados = set()
```

Quando um CPF ainda não existe no conjunto, ele é adicionado:

```python
cpfs_encontrados.add(cpf)
clientes_sem_duplicidade.append(cliente)
```

Quando o CPF já existe, o registro é considerado duplicado e o contador aumenta:

```python
duplicados_removidos += 1
```

## Exemplo de saída

```text
Clientes sem duplicidade:
João Silva - 12345678901
Maria Souza - 98765432100
Carlos Lima - 45678912300

Total de registros recebidos: 5
Total de clientes únicos: 3
Total de duplicados removidos: 2
```

## Como executar

```bash
python nome_do_arquivo.py
```
