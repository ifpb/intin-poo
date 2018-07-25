class CartaoMensagem:
    def __init__(self, destinatario):
        self.__destinatario = destinatario

    def retornar_mensagem(self, remetente, destinatario):
        pass

    @property
    def destinatario(self):
        return self.__destinatario

    @destinatario.setter
    def destinatario(self, destinatario):
        self.__destinatario = destinatario