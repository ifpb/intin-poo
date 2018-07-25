from datetime import datetime
from datetime import timedelta

class Data:
    def __init__(self, dia=0, mes=0, ano=0):
        if dia == 0:
            dia = datetime.today().day
        self.__dia = dia
        if mes == 0:
            mes = datetime.today().month
        self.__mes = mes
        if ano == 0:
            ano = datetime.today().year
        self.__ano = ano

    def __str__(self):
        return '{}/{}/{}'.format(self.__dia,self.__mes,self.__ano)

    def dia_seguinte(self):
        date = datetime(self.__ano, self.__mes, self.__dia, 0, 0, 0) + timedelta(days=1)
        self.__dia = date.day
        self.__mes = date.month
        self.__ano = date.year

    @property
    def dia(self):
        return self.__dia

    @dia.setter
    def dia(self, dia):
        self.__dia = dia

    @property
    def mes(self):
        return self.__mes

    @mes.setter
    def mes(self, mes):
        self.__mes = mes

    @property
    def ano(self):
        return self.__ano

    @ano.setter
    def ano(self, ano):
        self.__ano = ano