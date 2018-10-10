class Candidato:
    def __init__(self, nome, partido):
        self.nome = nome
        self.partido = partido

    def __str__(self):
        return "nome={},partido={}".format(self.nome, self.partido)