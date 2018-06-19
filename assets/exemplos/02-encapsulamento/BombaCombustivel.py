class BombaCombustivel:
    def __init__(self, tipoCombustivel, valorLivro, quantidadeCombustivel):
        self.setTipoCombustivel(tipoCombustivel)
        self.setValorLitro(valorLivro)
        self.setQuantidadeCombustivel(quantidadeCombustivel)

    def setTipoCombustivel(self, tipoCombustivel):
        self.tipoCombustivel = tipoCombustivel

    def setValorLitro(self, valorLitro):
        self.valorLitro = float(valorLitro)

    def setQuantidadeCombustivel(self, quantidadeCombustivel):
        self.quantidadeCombustivel = quantidadeCombustivel

    def abastecerPorValor(self, valor):
        totalLitros = valor / self.valorLitro
        if (totalLitros <= self.quantidadeCombustivel):
            self.setQuantidadeCombustivel(
                self.quantidadeCombustivel - totalLitros)

    def abastecerPorLitro(self, totalLitros):
        if (totalLitros <= self.quantidadeCombustivel):
            self.setQuantidadeCombustivel(
                self.quantidadeCombustivel - totalLitros)


bomba1 = BombaCombustivel('Gasolina Aditivada', 4.30, 10000)
bomba1.abastecerPorLitro(100)
print(bomba1.quantidadeCombustivel)
bomba1.abastecerPorValor(100)
print(bomba1.quantidadeCombustivel)