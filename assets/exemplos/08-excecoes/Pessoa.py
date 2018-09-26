from IdadeInvalida import IdadeInvalida

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        if (self.idade > 100 or self.idade < 0):
            raise IdadeInvalida
