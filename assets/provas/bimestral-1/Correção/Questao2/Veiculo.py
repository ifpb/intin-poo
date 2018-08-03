class Veiculo:
    def __init__(self, tipo, cor, placa, portas):
        self.__tipo = tipo
        self.__cor = cor
        self.__placa = placa
        self.__portas = portas

    def __str__(self):
        return "Tipo = {}, Cor = {}, Placa = {}, Portas = {}".format(self.__tipo, self.__cor, self.__placa, self.__portas)

    @property
    def tipo(self):
        return self.__tipo

    @tipo.setter
    def tipo(self, tipo):
        self.__tipo = tipo

    @property
    def cor(self):
        return self.__cor

    @cor.setter
    def cor(self, cor):
        self.__cor = cor

    @property
    def placa(self):
        return self.__placa

    @placa.setter
    def placa(self, placa):
        self.__placa = placa

    @property
    def portas(self):
        return self.__portas

    @portas.setter
    def portas(self, portas):
        self.__portas = portas