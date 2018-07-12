from ContaBancaria import ContaBancaria

class ContaSalario(ContaBancaria):
    def __init__(self, numero, agencia, saldo, codigo_tipo, salario=0):
        ContaBancaria.__init__(self, numero, agencia, saldo, codigo_tipo)
        self.salario = salario

    def __str__(self):
        return "Numero da Conta: %s, Agencia: %s, Saldo: %d, Tipo: %s, Salário: %d" % (self.numero, self.agencia, self.saldo, self.nome_tipo, self.salario)


contaSalario = ContaSalario("1231", "213-X", 100, "01")
print(contaSalario)
