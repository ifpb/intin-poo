class Empregado:
    def __init__(self, primeiro_nome, segundo_nome, salario_mensal):
        self.__primeiro_nome = primeiro_nome
        self.__segundo_nome = segundo_nome
        if (salario_mensal < 0):
            salario_mensal = 0
        self.__salario_mensal = salario_mensal

    def salario_anual(self):
        return self.__salario_mensal * 13

    @property
    def primeiro_nome(self):
        return self.__primeiro_nome

    @primeiro_nome.setter
    def primeiro_nome(self, primeiro_nome):
        self.__primeiro_nome = primeiro_nome

    @property
    def segundo_nome(self):
        return self.__segundo_nome

    @segundo_nome.setter
    def segundo_nome(self, segundo_nome):
        self.__segundo_nome = segundo_nome

    @property
    def salario_mensal(self):
        return self.__salario_mensal

    @salario_mensal.setter
    def salario_mensal(self, salario_mensal):
        if (salario_mensal < 0):
            salario_mensal = 0
        self.__salario_mensal = salario_mensal