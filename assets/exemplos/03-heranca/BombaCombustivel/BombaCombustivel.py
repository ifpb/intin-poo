class BombaCombustivel:

    def __init__(self, quantidadeCombustivel, tipo, preco):
        self.quantidadeCombustivel = quantidadeCombustivel
        self.tipo = tipo
        self.preco = preco

    def abastecer_por_valor(self, valor):
        # Existe gasolina suficiente na bomba?
        litros = valor / self.preco
        print("Abastecendo litros: %s"% litros)
        if (self.quantidadeCombustivel >= litros):
            self.diminuir_quantidade(litros)
            print("Abastecimento por valor concluído")
        else:
            print("Não há combustivel suficiente na bomba")

    def abastecer_por_litro(self, litros):
        if (self.quantidadeCombustivel >= litros):
            valor = litros * self.preco
            print("Valor a pagar: %f" % valor)
            self.diminuir_quantidade(litros)
            print("Abastecimento por valor concluído")
        else:
            print("Não há combustivel suficiente na bomba")

    def alterar_valor(self, novoPreco):
        self.preco = novoPreco

    def alterar_tipo(self, tipo):
        self.tipo = tipo

    def alterar_quantidade(self, quantidade):
        self.quantidadeCombustivel = quantidade

    def aumentar_quantidade(self, quantidade):
        self.quantidadeCombustivel += quantidade

    def diminuir_quantidade(self, quantidade):
        self.quantidadeCombustivel -= quantidade

    ## Representação formal do objeto (usado para debug)
    def __repr__(self):
        return "Bomba de Combustivel, tipo: %s, quantidade: %d e preço: %f" % (self.tipo, self.quantidadeCombustivel, self.preco)

    ##
    def __str__(self):
        return "Bomba de %s" % self.tipo

