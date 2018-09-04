from Pessoa import Pessoa

class Funcionario(Pessoa):
    def __init__(self, nome, idade, endereco, salario):
        Pessoa.__init__(self, nome, idade, endereco)
        self.salario = salario

    def __str__(self):
        return "Nome = {}, idade = {}, salario = {}, endereço = {}".format(self.nome, self.idade, self.salario, self.endereco)

