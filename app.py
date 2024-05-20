from funcoes import ContaBancaria
from interface import InterfaceGrafica
from modulos import tk

def main():
    root = tk.Tk()
    conta = ContaBancaria()
    app = InterfaceGrafica(root, conta)
    root.mainloop()

if __name__ == "__main__":
    main()