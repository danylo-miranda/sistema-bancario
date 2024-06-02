# Sistema Bancario

Atendendo a solicitação do cliente, que, solicitou o desenvolvimento de um sistema bancario, afim de modernizar suas operações.

## Índice

* [Iniciar](#iniciar)
* [Linguagem](#linguagem-utilizada)
* [Bibliotecas Utilizadas](#bibliotecas-utilizadas)
* [Versão](#versões)
* [Detalhamento](#detalhamento-das-operações)
* [Interface](#interface-gráfica)
* [Contato](#contato)

## Iniciar

* Execute o arquivo app.py

## Linguagem utilizada

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

* Python 3.10.12

## Bibliotecas utilizadas

* tkinter
* csv
* datetime

## Versões 

## Versões 

* Notas tecnicas do lançamento e divulgação da versão beta do projeto <font color="orange">(0.1.1)</font> 

A primeira versão do sistema contará com apenas 3 operações :
---

| Depósito | Saque | Extrato|
|----------|-------|--------|
| Deve ser possível depositar valores positivos para a conta bancária| 3 saques diários com limite máximo de R$500,00 por saque | Essa operação deve listar todos os depósitos e saques realizados na conta|

* <font color="orange">**Interface:**</font>Para uma melhor experiência do usuário, desenvolvi uma interface gráfica.

-

* Notas tecnicas da atualização <font color="orange">(0.1.2)</font>


 A segunda versão do sistema  traz a implementação de cadastro de clientes, conta corrente além de melhorias nas funções do sistema :
 ---

* <font color="pink">**Novidades:**</font>Apresentando o cadastro de clientes:

| Criar Usuario | Criar Conta Corrente |
|---------------|----------------------|
| Cadastro de cliente | Vincular conta corrente ao usuario|

* <font color="orange">**Criar usuário:**</font>O programa deve armazenar os usuários em uma lista, um usuário é composto porÇ nome, data de nascimento, cpf e enddereço. Oendereço é uma string com o formato (logradouro, numero, bairro, cidade/sigla estado). Deve ser armazenado somento os numeros do cpf. Não será cadastrado 2 usuarios com o mesmo cpf.

* <font color="orange">**Criar conta corrente:**</font>O programa deve armazenar contas em uma lista, uma conta é compostapor: agência, número da conta e usuario. O numero da conta é sequencial, iniciando em 1. O número da agência é fixo:"0001" .O usuário agora pode ter mais de uma conta.

-

* <font color="orange"> **Sacar:** </font>A função sacar receberá os argumentos apenas por nome (keyword only): 

|Ex. de argumentos | Ex. de retorno |
|-----------------------|---------------------|
| Saldo, valor, extrato, limite, numero_saques, limite_saques| Saldo e extrato |

-

* <font color="orange">**Depositar:**</font>A função depositar receberá uma atualização e passrá a receber os argumentos apenas por posição(positional only):

|Ex. de argumentos | Ex. de retorno |
|-----------------------|---------------------|
| Saldo, valor, extrato | Saldo e extrato |

-

* <font color="orange">**Extrato:**</font>A função extrato receberá atualizações onde deve receber os argumentos por posição e nome (positional only e keyword only):

|Ex. argumentos posicionais | Ex. argumentos nomeados |
|-----------------------|---------------------|
| Saldo |  Extrato |

-

## Detalhamento das operações

* Depósito: Deve ser possível depositar valores positivos para a conta bancária. Todos os depósitos devem ser armazenados em uma variável e exibidos na operação de extrato.

* Saque: O sistema deve permitir realizar 3 saques diários com limite máximo de R$500,00 por saque. Caso o usuário não tenha saldo em conta, o sistema deve exibir uma mensagem informando que não será possível sacar o dinheiro por falta de saldo. Todos os saques devem ser armazenados em uma variável e exibidos na operação de extrato.

* Essa operação deve listar todos os depósitos e saques realizados na conta. No fim da listagem deve ser exibido o saldo atual da conta. Os valores devem serexibidos utilizando o formato R$ xxx.xx

## Interface Gráfica

* Para garantir uma melhor experiência para o usuário, o sistema possui uma interface gráfica básica que executa as operações solicitadas pelo cliente.

* Permite imprimir na tela as movimentações realizadas no dia.

* Pensando na escalabilidade do sistema, a função de salvar em csv foi implementada. Ao encerrar o sistema, um arquivo .csv é gerado com os dados do extrato salvos. Isso garante uma espécie de backup dos dados e futuramente pode servir para a integração com um Banco de Dados.

![interface](https://danylo-bucket.s3.amazonaws.com/academico/imagens/app_financeiro/interface.png)

### Funcionamento dos botoes

|Depositar|Sacar|Extrato|Sair|
|---------|-----|-------|----|
|Deposita a quantia indicada no campo Valor|Saca a quantia indicada no campo Valor|Imprime na tela as movimentacoes executadas|Fecha o programa e salva os dados em um arquivo .csv|

## Contato
[![LinkedIn](https://img.shields.io/badge/linkedin-%230077B5.svg?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/adm-danylo-miranda/)