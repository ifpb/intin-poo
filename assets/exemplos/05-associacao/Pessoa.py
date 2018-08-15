class Pessoa:
    def __init__(self, nome, cpf, idade):
        self.nome = nome
        self.cpf = cpf
        self.idade = idade
        self.enderecos = []

    def adicionarEndereco(self, endereco):
        self.enderecos.append(endereco)
