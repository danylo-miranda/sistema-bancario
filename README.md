# Sistema Bancario

Atendendo a solicitação do cliente, que, solicitou o desenvolvimento de um sistema bancario, afim de modernizar suas operações.

## Índice

* [Iniciar](#iniciar)
* [Linguagem](#linguagem-utilizada)
* [Bibliotecas Utilizadas](#bibliotecas-utilizadas)
* [Versão](#versão)
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

## Versão

* A primeira versão do sistema contará com apenas 3 operações :

| Depósito | Saque | Extrato|
|----------|-------|--------|
| Deve ser possível depositar valores positivos para a conta bancária.| 3 saques diários com limite máximo de R$500,00 por saque. | Essa operação deve listar todos os depósitos e saques realizados na conta.|

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