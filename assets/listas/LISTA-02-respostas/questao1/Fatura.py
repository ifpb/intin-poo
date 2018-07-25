class Fatura:

    def __init__(self, num_item, descricao, quantidade=0, preco_unitario=0):
        self.__num_item = num_item
        self.__descricao = descricao
        if (quantidade < 0):
            quantidade = 0
        self.__quantidade = quantidade
        if (preco_unitario < 0):
            preco_unitario = 0
        self.__preco_unitario = preco_unitario

    def calcular_valor_fatura(self):
        return self.__quantidade * self.__preco_unitario

    @property
    def num_item(self):
        return self.__num_item

    @num_item.setter
    def num_item(self, num_item):
        self.__num_item = num_item

    @property
    def descricao(self):
        return self.__descricao

    @descricao.setter
    def descricao(self, descricao):
        self.__descricao = descricao

    @property
    def quantidade(self):
        return self.__quantidade

    @quantidade.setter
    def quantidade(self, quantidade):
        if (quantidade < 0):
            quantidade = 0
        self.__quantidade = quantidade

    @property
    def preco_unitario(self):
        return self.__preco_unitario

    @preco_unitario.setter
    def preco_unitario(self, preco_unitario):
        if (preco_unitario < 0):
            preco_unitario = 0
        self.__preco_unitario = preco_unitario