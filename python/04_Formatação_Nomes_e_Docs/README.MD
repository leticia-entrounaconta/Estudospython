# Cadastro e Validação de Dados

Projeto em Python para normalizar nomes e validar CPFs informados pelo usuário.

##  📌Funcionalidades

### Normalização de nome

O programa:

* remove espaços extras;
* impede nomes vazios;
* bloqueia números e símbolos inválidos;
* permite hífen e apóstrofo;
* deixa as iniciais em maiúsculo;
* mantém partículas como `de`, `da`, `do` e `dos` em minúsculo.

Exemplo:

```text
Entrada:     JOÃO       DA SILVA
Saída: João da Silva
```

### Validação de CPF

O programa:

* remove pontos e hífen;
* verifica se existem 11 dígitos;
* impede caracteres não numéricos;
* rejeita sequências repetidas;
* calcula os dois dígitos verificadores;
* solicita novamente o CPF quando ele for inválido.

## Como executar

É necessário ter o Python instalado.

No terminal, execute:

```bash
python cadastro.py
```

No Windows, também pode usar:

```bash
py cadastro.py
```

##  🖥️ Exemplo de execução

```text
========== 1- Normalizador de Nome ==========
Digite o nome completo:     LETICIA MONTEIRO

Nome normalizado: Leticia Monteiro

============ 2- Validador de CPF ============
Digite o CPF: 106.193.494-25

CPF validado com sucesso!

          PROGRAMA FINALIZADO
=============================================
```

## Conceitos utilizados

* funções;
* `if` e `else`;
* `for` e `while`;
* `try` e `except`;
* `raise`;
* manipulação de strings;
* valores booleanos;
* cálculos matemáticos;
* entrada e saída de dados.

## Observação

A função valida apenas a estrutura matemática do CPF. Ela não confirma se o documento existe, está ativo ou pertence a uma pessoa.


## 👩‍💻Autora

Desenvolvido por **Leticia Monteiro** como projeto de estudo em Python.
