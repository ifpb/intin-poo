from Veiculo import Veiculo

class VeiculoNacional(Veiculo):
    def __init__(self, tipo, cor, placa, portas, preco):
        Veiculo.__init__(self, tipo, cor, placa, portas)
        self.__preco = preco

    def __str__(self):
        return Veiculo.__str__(self) + ", Preço = {}".format(self.__preco)

    @property
    def preco(self):
        return self.__preco

    @preco.setter
    def preco(self, preco):
        self.__preco = preco