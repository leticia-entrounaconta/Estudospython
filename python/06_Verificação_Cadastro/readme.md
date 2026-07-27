# Verificação de Acesso

Este projeto verifica se usuários podem acessar um sistema com base nas seguintes regras:

* O nome deve estar preenchido;
* O usuário deve ter 18 anos ou mais;
* O usuário deve estar ativo;
* O usuário deve possuir permissão de acesso.

## Funcionamento

Os dados dos usuários são armazenados em uma lista de dicionários. A função `verificar_cadastros()` percorre cada cadastro e valida as informações utilizando `if`, `elif` e `else`.

Quando alguma regra não é atendida, o programa informa o motivo da negativa. Caso todas as condições sejam válidas, o acesso é permitido.

## Conceitos utilizados

* Listas;
* Dicionários;
* Funções;
* Laço `for`;
* Condicionais;
* Operadores lógicos;
* F-strings.

## Como executar

No terminal, utilize:

```bash
python nome_do_arquivo.py
```

## Exemplo de saída

```text
Acesso permitido para João.
Acesso negado: nome não informado.
Acesso negado: idade mínima não atingida.
Acesso negado: usuário inativo.
Acesso negado: usuário sem permissão.
```
