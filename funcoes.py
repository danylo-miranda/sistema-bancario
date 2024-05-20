from modulos import tk, datetime, csv

class ContaBancaria:
    def __init__(self, saldo_inicial=0, limite=500):
        self.saldo = saldo_inicial
        self.limite = limite
        self.extrato = ""
        self.num_saques = 0
        self.LIMITE_SAQUES = 3

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            data_hora = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            self.extrato += f"Depósito: R$ {valor:.2f} em {data_hora}\n"
        else:
            print("Operação falhou! O valor informado é inválido.")

    def sacar(self, valor):
        excedeu_saldo = valor > self.saldo
        excedeu_limite = valor > self.limite
        excedeu_saques = self.num_saques >= self.LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Saldo insuficiente.")
        elif excedeu_limite:
            print("Operação falhou! Valor do saque excede o limite permitido.")
        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")
        elif valor > 0:
            self.saldo -= valor
            data_hora = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            self.extrato += f"Saque: R$ {valor:.2f} em {data_hora}\n"
            self.num_saques += 1
        else:
            print("Operação falhou! O valor informado é inválido.")

    def exibir_extrato(self):
        print("\n====================EXTRATO====================")
        print("Não foram realizados movimentações." if not self.extrato else self.extrato)
        print(f"\nSaldo: R$ {self.saldo:.2f}")
        print("=================================================")


    def salvar_extrato_csv(self, nome_arquivo="extrato.csv"):
        try:
            with open(nome_arquivo, "w", newline="") as arquivo_csv:  # Corrigido aqui
                escritor_csv = csv.writer(arquivo_csv)

                # Escrever o cabeçalho com os nomes das colunas
                escritor_csv.writerow(["OPERACAO", "VALOR", "DATA", "HORA"])

                for linha in self.extrato.splitlines():
                    partes = linha.split(" em ")
                    if len(partes) == 2:
                        # Extrair o valor da operação
                        valor_str = partes[0].split(": R$ ")[1]

                        # Separa Data e Hora
                        data, hora = partes[1].split()

                        # Escrever os dados nas colunas corretas
                        escritor_csv.writerow([partes[0].split(":")[0], valor_str, data, hora])

                print(f"Extrato salvo com sucesso em {nome_arquivo}")
        except Exception as e:
            print(f"Erro ao salvar o extrato: {e}")



