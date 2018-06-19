from random import randint

class Personagem:
    def __init__(self, hp, nome, forca,
                 destreza, constituicao, sabedoria,
                 inteligencia, carisma):
        self.hp = hp
        self.nome = nome
        self.forca = forca
        self.constituicao = constituicao
        self.sabedoria = sabedoria
        self.inteligencia = inteligencia
        self.carisma = carisma
        self.destreza = destreza

    def atacar(self):
        hp = randint(1, 20) * self.forca
        print("O seu ataque vai tirar %d de HP" % hp)
        return hp

    def defender(self):
        return self.constituicao

    def raciocionar(self):
        return self.sabedoria * randint(1,20)

    def convencer(self):
        return self.carisma * randint(1,20)

    def desviarAtaque(self):
        return self.destreza


class Anao(Personagem):
    def __init__(self, hp, nome, forca,
                 destreza, constituicao, sabedoria,
                 inteligencia, carisma):
        Personagem.__init__(self,hp, nome, forca,
                 destreza, constituicao, sabedoria,
                 inteligencia, carisma)

    def atacar(self):
        hp = randint(1, 6) * self.forca
        print("O seu ataque vai tirar %d de HP" % hp)
        return hp

    def defender(self):
        Personagem.defender() + 2


class Elfo(Personagem):
    def __init__(self,hp, nome, forca,
                 destreza, constituicao, sabedoria,
                 inteligencia, carisma):
        Personagem.__init__(self,hp,nome, forca,
                 destreza, constituicao, sabedoria,
                 inteligencia, carisma)

    def atacar(self):
        hp = randint(1, 6) * self.forca + self.destreza
        print("O seu ataque vai tirar %d de HP" % hp)
        return hp

    def desviarAtaque(self):
        Personagem.desviarAtaque() + 2


class Barbaro(Personagem):
    def __init__(self, hp,nome, forca,
                 destreza, constituicao, sabedoria,
                 inteligencia, carisma):
        Personagem.__init__(self,hp,nome, forca,
                 destreza, constituicao, sabedoria,
                 inteligencia, carisma)

    def desviarAtaque(self):
        Personagem.desviarAtaque() + 2

    def raciocionar(self):
        print("O seu raciocinio nao é muito bom")
        return randint(1,5) * self.inteligencia

class Humano(Personagem):
    def __init__(self, hp,nome, forca,
                 destreza, constituicao, sabedoria,
                 inteligencia, carisma):
        Personagem.__init__(self,hp,nome, forca,
                 destreza, constituicao, sabedoria,
                 inteligencia, carisma)

class Draconato(Personagem):
    def __init__(self, hp,nome, forca,
                 destreza, constituicao, sabedoria,
                 inteligencia, carisma):
        Personagem.__init__(self,hp,nome, forca,
                 destreza, constituicao, sabedoria,
                 inteligencia, carisma)

class Gnomo(Personagem):
    def __init__(self, hp,nome, forca,
                 destreza, constituicao, sabedoria,
                 inteligencia, carisma):
        Personagem.__init__(self, hp,nome, forca,
                 destreza, constituicao, sabedoria,
                 inteligencia, carisma)

    def raciocionar(self):
        print("O seu raciocinio  é muito bom")
        return randint(6,12) * self.inteligencia

class Ladrao(Personagem):
    def __init__(self, hp, nome, forca,
                 destreza, constituicao, sabedoria,
                 inteligencia, carisma):
        Personagem.__init__(self, hp, nome, forca,
                 destreza, constituicao, sabedoria,
                 inteligencia, carisma)


anao = Anao("Baixinho", 1000, 10, 5, 5, 10, 10, 1)
elfo = Elfo("Orelhudo", 1000, 10, 5, 5, 10, 10, 1)
barbaro = Barbaro("Barbudo", 1000, 10, 5, 5, 10, 10, 1)
gnomo = Gnomo("Gnomo", 1000, 10, 5, 5, 10, 10, 1)
draconato = Draconato("Draconato", 1000, 10, 5, 5, 10, 10, 1)

print(anao.atacar())
print(elfo.atacar())
print(gnomo.atacar())
print(draconato.atacar())