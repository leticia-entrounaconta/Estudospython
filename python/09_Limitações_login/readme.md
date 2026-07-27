# Sistema de Login

Este projeto simula um sistema de autenticação com limite de tentativas.

## Funcionamento

O programa solicita usuário e senha e compara os dados informados com as credenciais corretas.

O usuário possui até 3 tentativas para realizar o login. Quando os dados estão corretos, o acesso é liberado e o laço é encerrado com `break`.

Caso o limite seja atingido, o acesso é bloqueado.

## Credenciais de teste

```text
Usuário: admin
Senha: 123456
```

## Conceitos utilizados

* Variáveis;
* `input()`;
* Laço `while`;
* Condicionais;
* Operador `and`;
* Contador;
* `break`;
* `else` associado ao `while`;
* F-strings.

## Exemplo de saída

```text
--- Tentativa 1 de 3 ---
Usuário: admin
Senha: 123456

Login realizado com sucesso! Bem-vindo.
```

Caso as três tentativas estejam incorretas:

```text
Número máximo de tentativas atingido. Acesso bloqueado.
```

## Como executar

```bash
python nome_do_arquivo.py
```
