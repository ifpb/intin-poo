from Pessoa import Pessoa

class Cliente(Pessoa):
    def __init__(self, nome, idade):
        Pessoa.__init__(self, nome, idade)

    def calcular_valor_final_passagem(self, valor):
        if self.idade > 65:
            return 0 #Cliente idoso
        else:
            return valor