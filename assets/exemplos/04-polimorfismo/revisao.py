class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def __str__(self):
        return self.nome

    def maiorDeIdade(self):
        return (self.idade >= 18)

class PessoaFisica(Pessoa):
    def __init__(self, nome, idade, cpf):
        Pessoa.__init__(self, nome, idade)
        self.cpf = cpf

class PessoaJuridica(Pessoa):
    def __init__(self, nome, idade, cnpj):
        Pessoa.__init__(self, nome, idade)
        self.cnpj = cnpj


pessoa = PessoaFisica("Isaque", 16, "231.123.123-21")
print(pessoa)
print(pessoa.maiorDeIdade())

pessoaJuridica = PessoaJuridica("IFPB", 40, "24048120480218412")
print(pessoaJuridica)
print(pessoa.maiorDeIdade())