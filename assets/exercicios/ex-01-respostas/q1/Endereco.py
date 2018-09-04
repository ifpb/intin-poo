class Endereco:
    def __init__(self, rua, numero, bairro, cidade, estado, pais):
        self.rua = rua
        self.numero = numero
        self.bairro = bairro
        self.cidade = cidade
        self.estado = estado
        self.pais = pais

    def __str__(self):
        return "Rua = {}, numero = {}, bairro = {}, cidade = {}, estado = {}, pais = {}".format(self.rua, self.numero, self.bairro, self.cidade, self.estado, self.pais)
