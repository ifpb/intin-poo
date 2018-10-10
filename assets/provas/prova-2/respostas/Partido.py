class Partido:
    def __init__(self, numero, nome):
        self.numero = numero
        self.nome = nome

    def __str__(self):
        return "numero={}, nome={}".format(self.numero, self.nome)