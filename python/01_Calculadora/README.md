# Calculadora em Python

Projeto simples de uma calculadora feita em Python para praticar entrada de dados, conversão de tipos, operações matemáticas e estruturas condicionais.

## 📌Funcionalidades

- Adição
- Subtração
- Multiplicação
- Divisão
- Validação para impedir divisão por zero
- Mensagem para opção inválida

## Pré-requisito

Ter o Python 3 instalado no computador.

Para confirmar a instalação, abra o terminal e execute:

```powershell
python --version
```

## Como executar

1. Salve o código em um arquivo chamado `calculadora.py`.
2. Abra o terminal na pasta onde o arquivo foi salvo.
3. Execute:

```powershell
python .\calculadora.py
```

Se necessário, tente:

```powershell
py .\calculadora.py
```

## Como usar

Ao iniciar o programa, informe dois números e escolha uma operação no menu:

```text
========== Calculadora ==========
Digite o primeiro número: 10
Digite o segundo número: 5

Operações
1. Adição
2. Subtração
3. Multiplicação
4. Divisão

Escolha a operação: 2
Resultado: 5.0
```

## Operações disponíveis

| Opção | Operação | Exemplo |
| --- | --- | --- |
| `1` | Adição | `10 + 5 = 15` |
| `2` | Subtração | `10 - 5 = 5` |
| `3` | Multiplicação | `10 * 5 = 50` |
| `4` | Divisão | `10 / 5 = 2` |

## Tratamento de divisão por zero

Antes de realizar uma divisão, o programa verifica se o segundo número é diferente de zero. Caso seja zero, apresenta a mensagem:

```text
Erro: não é possível dividir por zero.
```

## Conceitos praticados

- `print()` para mostrar mensagens na tela;
- `input()` para receber dados do usuário;
- `float()` para converter texto em número decimal;
- variáveis;
- operadores matemáticos: `+`, `-`, `*` e `/`;
- condições com `if`, `elif` e `else`;
- comparação com `==` e `!=`.

## Melhorias futuras

- Permitir executar vários cálculos sem reiniciar o programa;
- Tratar erros quando a pessoa digitar letras no lugar de números;
- Mostrar o cálculo completo, por exemplo: `10.0 + 5.0 = 15.0`;
- Adicionar potência e porcentagem.


## 👩‍💻Autora

Desenvolvido por **Leticia Monteiro** como projeto de estudo em Python.
