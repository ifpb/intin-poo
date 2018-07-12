from Ingresso import Ingresso

class IngressoVIP(Ingresso):
    def __init__(self, valor, adicional):
        Ingresso.__init__(self, valor + adicional)