# Validação de CPFs

Este projeto percorre uma lista de CPFs e verifica se cada registro pode ser processado.

## Regras de validação

O programa verifica se:

* O CPF está vazio ou possui valor `None`;
* O CPF possui exatamente 11 caracteres;
* O CPF pode seguir para o processamento.

Quando o CPF está vazio, o registro é ignorado. Quando possui uma quantidade incorreta de caracteres, o programa informa o erro.

## Conceitos utilizados

* Listas;
* Laço `for`;
* Condicionais;
* Operador `or`;
* `None`;
* Função `len()`;
* `continue`;
* F-strings.

## Funcionamento do `continue`

O comando `continue` interrompe a repetição atual e passa para o próximo CPF da lista.

## Exemplo de saída

```text
processando cpf: 12345678901
processando cpf: 98765432100
Cpf vazio. Registro ignorado.
CPF 12345 possui quantidade inválida de caracteres.
Cpf vazio. Registro ignorado.
Total de registros recebidos: 5
```

## Como executar

```bash
python nome_do_arquivo.py
```
