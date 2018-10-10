class Voto:
    def __init__(self, data, candidato, eleitor):
        self.data = data
        self.candidato = candidato
        self.eleitor = eleitor

    def __str__(self):
        return "data={}, candidato={}".format(self.data, self.candidato)