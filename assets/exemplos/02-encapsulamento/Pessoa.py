class Pessoa:
    __nome="",
    idade=0,
    peso=0.0,
    altura=0.0

    def __init__(self, nome, idade, peso, altura):
        self.__nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def envelhecer(self, anos):
        self.idade += anos
        if (self.idade < 21):
            self.altura += 0.05

    def engordar(self, peso):
        self.peso += peso

    def emagrecer(self, peso):
        if (peso > self.peso):
            self.peso = 0
        else:
            self.peso -= peso

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @staticmethod
    def imc(peso, altura):
        return peso / (altura * altura)