class Pedido:

    def __init__(self, valor_total=0.0):
        self.valor_total = valor_total
        self.itens_pedido = []

    def adicionar_item(self, item):
        self.itens_pedido.append(item)

    def obter_total(self):
        total = 0.0
        for item in self.itens_pedido:
            total += (item.produto.valor*item.quantidade)
        return total