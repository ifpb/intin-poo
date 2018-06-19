class ContaBancaria:
    numero = "00000-0"
    agencia = "0000-0"
    saldo = 0.0
    codigo_tipo = "01" #01 = Conta Corrente, 02 = Poupança
    nome_tipo = ""

    def __init__(self, numero, agencia, saldo, codigo_tipo):
        if (self.validaTipo(codigo_tipo) == True):
            self.numero = numero
            self.agencia = agencia
            self.saldo = saldo
            self.codigo_tipo = codigo_tipo
            if (self.codigo_tipo == "01"):
                self.nome_tipo = "Conta Corrente"
            else:
                self.nome_tipo = "Poupança"
        else:
            print("Tipo de conta inválida: escolha Conta Corrente ou Poupança")

    def validaTipo(self, codigo_tipo):
        if (codigo_tipo == "01" or codigo_tipo == "02"):
            return True
        else:
            return False

    def mostrarSaldo(self):
        print(self.saldo)

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if (self.saldo >= valor):
            self.saldo -= valor
        else:
            print("Saldo insuficiente!")

print("Bem-vindo ao gerenciamento de contas")

print("Informe os dados da sua conta")

numero = input("Digite o numero da conta: ")
agencia = input("Digite o numero da agencia: ")
tipo = input("Digite o tipo da conta (01=Conta Corrente, 02=Poupança):")
conta = ContaBancaria(numero, agencia, 0.0, tipo)
print("Parabens, voce criou uma nova conta!")
print("Tipo de conta criada: ")
print(conta.nome_tipo)
print("Saldo inicial: ")
print(conta.mostrarSaldo())