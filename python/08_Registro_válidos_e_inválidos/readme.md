# Validação de Registros

Este projeto analisa uma lista de pessoas e separa os registros válidos dos inválidos.

## Regras de validação

Cada registro deve possuir:

* Nome preenchido;
* CPF preenchido;
* CPF com 11 caracteres;
* Idade informada;
* Idade igual ou superior a 18 anos.

## Funcionamento

O programa percorre todos os registros usando `for` e `enumerate()`.

Para cada pessoa, é criada uma lista chamada `motivos`, que armazena os problemas encontrados. Caso essa lista permaneça vazia, o registro é considerado válido. Caso possua algum motivo, o registro é adicionado à lista de inválidos.

## Conceitos utilizados

* Listas;
* Dicionários;
* Laço `for`;
* `enumerate()`;
* Condicionais;
* `append()`;
* `len()`;
* `strip()`;
* `join()`;
* F-strings.

## Saída esperada

```text
Total de registros: 4
Registros válidos: 1
Registros inválidos: 3

Registros válidos:
Ana - 12345678901

Registros inválidos:
Registro 2: Nome não informado.
Registro 3: CPF inválido e Pessoa menor de idade.
Registro 4: CPF não informado.
```

## Como executar

No terminal, utilize:

```bash
python nome_do_arquivo.py
```
