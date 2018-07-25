class CalculadoraAfinidade:
    def calcular_afinidade(self, p1, p2):
        afinidade = (len(p1.nome) + p1.idade) - (len(p2.nome) + p2.idade)
        if (afinidade < 0):
            afinidade = afinidade * -1
        return afinidade
