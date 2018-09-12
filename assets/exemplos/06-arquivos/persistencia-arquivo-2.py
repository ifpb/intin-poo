import shelve

class Pessoa:
    def __init__(self, id, nome, idade):
        self.id = id
        self.nome = nome
        self.idade = idade

class Main:
    def persistir(self):
        p1 = Pessoa(1, "Jiraya", 80)
        p2 = Pessoa(2, "Gyban", 75)
        p3 = Pessoa(3, "Black Kamen Rider", 65)

        db = shelve.open("persistencia.db")
        for obj in (p1, p2, p3):
            db[str(obj.id)] = obj

        db.close()

    def ler(self):
        db = shelve.open("persistencia.db")
        print(list(db.keys()))
        for p in db.keys():
            print("Pessoa id %s é %s" % (db[p].id, db[p].nome))

    def apagar(self):
        db = shelve.open("persistencia.db")


main = Main()
main.ler()