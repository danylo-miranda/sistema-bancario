from funcoes import ContaBancaria
from modulos import tk, datetime, csv

class InterfaceGrafica:
    def __init__(self, master, conta):
        self.master = master
        self.conta = conta
        master.title("Financeiro DSM")
        master.geometry('500x400')
        master.resizable(True, True)
        master.maxsize(width=900, height=700)
        master.minsize(width=500, height=400) 

        self.label_saldo = tk.Label(master, text=f"Saldo: R$ {self.conta.saldo:.2f}")
        self.label_saldo.pack(pady=10)
        self.label_mensagem = tk.Label(master, text='', fg='red')
        self.label_mensagem.pack(pady=5)

        self.frame_operacoes = tk.Frame(master)
        self.frame_operacoes.pack()
        self.frame_entrada = tk.Frame(master)
        self.frame_entrada.pack(pady=10)

        tk.Label(self.frame_entrada, text="Valor: R$").pack(side=tk.LEFT)
        self.entry_valor = tk.Entry(self.frame_entrada)
        self.entry_valor.pack(side=tk.LEFT)

        tk.Button(self.frame_operacoes, text="Depositar", command=self.depositar).pack(side=tk.LEFT, padx=5)
        tk.Button(self.frame_operacoes, text="Sacar", command=self.sacar).pack(side=tk.LEFT, padx=5)
        tk.Button(self.frame_operacoes, text="Extrato", command=self.exibir_extrato).pack(side=tk.LEFT, padx=5)
        tk.Button(self.frame_operacoes, text="Sair", command=self.sair).pack(side=tk.LEFT, padx=5)

        self.text_extrato = tk.Text(master, height=15, width=60)
        self.text_extrato.pack(pady=10)


    def depositar(self):
        try:
            valor = float(self.entry_valor.get())
            self.conta.depositar(valor)
            self.atualizar_saldo()
            self.exibir_mensagem("Depósito realizado com sucesso!", "green")
        except ValueError:
            self.exibir_mensagem("Valor inválido. Digite um número.")

    def atualizar_saldo(self):
        self.label_saldo.config(text=f"Saldo: R$ {self.conta.saldo:.2f}")

    def sacar(self):
        try:
            valor = float(self.entry_valor.get())
            mensagem = self.conta.sacar(valor)  # Obtém a mensagem da função sacar
            if "sucesso" in mensagem.lower():
                self.exibir_mensagem(mensagem, "green")
            else:
                self.exibir_mensagem(mensagem, "red")
            self.atualizar_saldo()
        except ValueError:
            self.exibir_mensagem("Valor inválido. Digite um número válido.", "red")


    def exibir_mensagem(self, mensagem, cor="red"):
        self.label_mensagem.config(text=mensagem, fg=cor)
        self.master.after(6000, lambda: self.label_mensagem.config(text=""))  # Limpa a mensagem após 3 segundos

    def exibir_extrato(self):
        self.text_extrato.delete(1.0, tk.END)  # Limpa o extrato anterior
        self.text_extrato.insert(tk.END, self.conta.extrato)

    def sair(self):
        self.conta.salvar_extrato_csv()
        self.master.destroy()