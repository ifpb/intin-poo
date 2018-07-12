from ContaBancaria import ContaBancaria

class ContaImposto(ContaBancaria):
    def __init__(self, numero, agencia, saldo, codigo_tipo, percentualImposto):
        ContaBancaria.__init__(self, numero, agencia, saldo, codigo_tipo)
        self.__percentualImposto = percentualImposto

    def calcularImposto(self):
        return self.saldo - (self.saldo * self.__percentualImposto)