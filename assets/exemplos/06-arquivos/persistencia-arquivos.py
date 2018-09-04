import json

class Pessoa:
    def __init__(self, id=0, nome='', idade=0):
        self.id = id
        self.nome = nome
        self.idade = idade

    def __str__(self):
        return "id = {}, nome = {}, idade = {}".format(self.id, self.nome, self.idade)

def salvarDados():
    pessoas = []
    p1 = Pessoa(1, "Diego", 30)
    pessoas.append(p1.__dict__)
    p2 = Pessoa(2, "Joao", 30)
    pessoas.append(p2.__dict__)

    arq = open("/tmp/objetos.json", 'w')
    arq.write(json.dumps(pessoas))
    arq.close()

def lerDados():
    arq = open("/tmp/objetos.json", 'r')
    pessoas = json.load(arq)

    for pessoa in pessoas:
        print(pessoa)

salvarDados()
lerDados()