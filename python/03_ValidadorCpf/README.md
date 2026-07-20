# Validador de CPF em Python

Projeto desenvolvido em Python para verificar se um CPF informado pelo usuário possui uma estrutura matemática válida.

## Funcionalidades

O programa:

* remove pontos, hífen e espaços externos;
* verifica se o CPF possui 11 dígitos;
* impede letras e outros caracteres;
* rejeita sequências repetidas, como `11111111111`;
* calcula os dois dígitos verificadores;
* retorna `True` para CPF válido e `False` para inválido.

## Como executar

É necessário ter o Python instalado.

No terminal, execute:

```bash
python validador_cpf.py
```

No Windows, também pode utilizar:

```bash
py validador_cpf.py
```

##  🖥️ Exemplo de execução

```text
========== Validador de CPF ==========
Digite o CPF: 106.193.494-25
CPF válido.
```

Exemplo inválido:

```text
========== Validador de CPF ==========
Digite o CPF: 111.111.111-11
CPF inválido.
```

## Formatos aceitos

O CPF pode ser digitado com ou sem pontuação:

```text
106.193.494-25
10619349425
```

## Conceitos utilizados

* funções;
* parâmetros e `return`;
* estruturas condicionais;
* laço `for`;
* valores booleanos;
* manipulação de strings;
* índices e fatiamento;
* cálculos matemáticos;
* operador de módulo `%`.

## Observação

O programa verifica somente se os dígitos do CPF são matematicamente válidos.

Isso não confirma se o CPF existe, está ativo, pertence a uma pessoa ou está regular na Receita Federal.

## Possíveis melhorias

* repetir a solicitação quando o CPF for inválido;
* validar o tipo do valor recebido;
* remover espaços internos;
* formatar o CPF automaticamente;
* criar testes automatizados;
* organizar o código em uma função `main`.

## Autora

👩‍💻 Desenvolvido por **Leticia Monteiro** como projeto de estudo em Python.
