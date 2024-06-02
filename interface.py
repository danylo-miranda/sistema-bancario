from funcoes import ContaBancaria
from modulos import tk, datetime, csv
from tkinter import messagebox

class Usuario:
    def __init__(self, nome, data_nascimento, cpf, endereco):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf
        self.endereco = endereco

class ContaCorrente:
    def __init__(self, agencia, numero, usuario, conta_bancaria):
        self.agencia = agencia
        self.numero = numero
        self.usuario = usuario
        self.conta_bancaria = conta_bancaria

class InterfaceContaBancaria:
    def __init__(self, master, conta_corrente, gerenciador_banco):
        self.master = master
        self.conta_corrente = conta_corrente
        self.conta = conta_corrente.conta_bancaria
        self.gerenciador_banco = gerenciador_banco

        master.title(f"Conta Corrente - {conta_corrente.usuario.nome}")
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
        tk.Button(self.frame_operacoes, text="Voltar", command=self.voltar).pack(side=tk.LEFT, padx=5)

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
            mensagem = self.conta.sacar(valor)
            if "sucesso" in mensagem.lower():
                self.exibir_mensagem(mensagem, "green")
            else:
                self.exibir_mensagem(mensagem, "red")
            self.atualizar_saldo()
        except ValueError:
            self.exibir_mensagem("Valor inválido. Digite um número válido.", "red")

    def exibir_mensagem(self, mensagem, cor="red"):
        self.label_mensagem.config(text=mensagem, fg=cor)
        self.master.after(6000, lambda: self.label_mensagem.config(text=""))

    def exibir_extrato(self):
        self.text_extrato.delete(1.0, tk.END)
        self.text_extrato.insert(tk.END, self.conta.extrato)

    def voltar(self):
        self.master.destroy()  # Fecha a janela da InterfaceContaBancaria
        self.gerenciador_banco.master.deiconify()  # Reabre a janela do GerenciadorBanco


class GerenciadorBanco:
    def __init__(self, master):
        self.master = master
        self.usuarios = []  # Lista de usuários
        self.contas = []  # Lista de contas
        self.numero_conta = 1  # Sequencial de número de contas

        self.criar_interface_inicial()

    def criar_interface_inicial(self):
        for widget in self.master.winfo_children():
            widget.destroy()

        tk.Label(self.master, text="Bem-vindo ao Gerenciador do Banco").pack(pady=20)
        tk.Button(self.master, text="Cadastrar Cliente", command=self.cadastrar_cliente).pack(pady=10)
        tk.Button(self.master, text="Acessar Conta", command=self.acessar_conta).pack(pady=10)
        tk.Button(self.master, text="Voltar", command=self.master.destroy).pack(pady=10)

    def cadastrar_cliente(self):
        for widget in self.master.winfo_children():
            widget.destroy()

        tk.Label(self.master, text="Cadastro de Cliente").pack(pady=20)
        tk.Label(self.master, text="Nome:").pack()
        nome_entry = tk.Entry(self.master)
        nome_entry.pack()
        tk.Label(self.master, text="Data de Nascimento (dd/mm/yyyy):").pack()
        data_nascimento_entry = tk.Entry(self.master)
        data_nascimento_entry.pack()
        tk.Label(self.master, text="CPF (somente números):").pack()
        cpf_entry = tk.Entry(self.master)
        cpf_entry.pack()
        tk.Label(self.master, text="Endereço:").pack()
        endereco_entry = tk.Entry(self.master)
        endereco_entry.pack()

        def criar_usuario():
            nome = nome_entry.get()
            data_nascimento = data_nascimento_entry.get()
            cpf = cpf_entry.get()
            endereco = endereco_entry.get()

            if not nome or not data_nascimento or not cpf or not endereco:
                messagebox.showerror("Erro", "Preencha todos os campos.")
                return

            if any(usuario.cpf == cpf for usuario in self.usuarios):
                messagebox.showerror("Erro", "CPF já cadastrado.")
                return

            usuario = Usuario(nome, data_nascimento, cpf, endereco)
            self.usuarios.append(usuario)
            self.criar_conta_corrente(usuario)

        tk.Button(self.master, text="Cadastrar", command=criar_usuario).pack(pady=10)
        tk.Button(self.master, text="Voltar", command=self.criar_interface_inicial).pack()

    def criar_conta_corrente(self, usuario):
        agencia = "0001"
        conta_bancaria = ContaBancaria(0, 5000)  # Cria uma nova conta bancária com saldo e limite de saque em 5000
        conta_corrente = ContaCorrente(agencia, self.numero_conta, usuario, conta_bancaria)
        self.contas.append(conta_corrente)
        self.numero_conta += 1
        messagebox.showinfo("Sucesso", f"Conta criada com sucesso! Número da conta: {conta_corrente.numero}")
        self.criar_interface_inicial()

    def acessar_conta(self):
        for widget in self.master.winfo_children():
            widget.destroy()

        tk.Label(self.master, text="Acessar Conta").pack(pady=20)
        tk.Label(self.master, text="CPF:").pack()
        cpf_entry = tk.Entry(self.master)
        cpf_entry.pack()

        def entrar():
            cpf = cpf_entry.get()
            usuario = next((u for u in self.usuarios if u.cpf == cpf), None)

            if not usuario:
                messagebox.showerror("Erro", "Usuário não encontrado.")
                return

            contas_usuario = [conta for conta in self.contas if conta.usuario.cpf == cpf]
            if not contas_usuario:
                messagebox.showerror("Erro", "Nenhuma conta encontrada para este usuário.")
                return

            self.selecionar_conta(contas_usuario)

        tk.Button(self.master, text="Entrar", command=entrar).pack(pady=10)
        tk.Button(self.master, text="Voltar", command=self.criar_interface_inicial).pack()

    def selecionar_conta(self, contas_usuario):
        for widget in self.master.winfo_children():
            widget.destroy()

        tk.Label(self.master, text="Selecione a Conta").pack(pady=20)
        contas_var = tk.StringVar(value=[f"Agência: {conta.agencia}, Conta: {conta.numero}" for conta in contas_usuario])
        listbox = tk.Listbox(self.master, listvariable=contas_var)
        listbox.pack()

        def selecionar():
            selecao = listbox.curselection()
            if not selecao:
                messagebox.showerror("Erro", "Selecione uma conta.")
                return

            conta_selecionada = contas_usuario[selecao[0]]
            self.criar_interface_conta(conta_selecionada)

        tk.Button(self.master, text="Selecionar", command=selecionar).pack(pady=10)
        tk.Button(self.master, text="Voltar", command=self.acessar_conta).pack()

    def criar_interface_conta(self, conta_corrente):
        interface_conta = tk.Toplevel(self.master)
        InterfaceContaBancaria(interface_conta, conta_corrente, self) 

class Apllication:  # Renomeie a classe para Apllication (com dois "p")
    def __init__(self, master):
        self.master = master
        master.title("Financeiro DSM")
        master.geometry('500x400')
        master.resizable(True, True)
        master.maxsize(width=900, height=700)
        master.minsize(width=500, height=400)

        self.label_bem_vindo = tk.Label(master, text="Bem-vindo ao Financeiro DSM")
        self.label_bem_vindo.pack(pady=20)

        self.botao_gerenciar_banco = tk.Button(master, text="Gerenciar Banco", command=self.abrir_gerenciador_banco)
        self.botao_gerenciar_banco.pack(pady=10)
        
        self.gerenciador_banco = GerenciadorBanco  # Instância do GerenciadorBanco


    def abrir_gerenciador_banco(self):
        if not hasattr(self, 'janela_gerenciador') or not self.janela_gerenciador.winfo_exists():
            self.janela_gerenciador = tk.Toplevel(self.master)
            self.gerenciador_banco = GerenciadorBanco(self.janela_gerenciador)
    
    