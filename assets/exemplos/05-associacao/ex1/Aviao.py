class Aviao:
    def __init__(self, nome, numero, coordenada):
        self.nome = nome
        self.numero = numero
        self.coordenada = coordenada

    def distancia(self, aviao):
        return self.coordenada.calcularDistanciaReal(aviao.coordenada)