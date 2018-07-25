from CartaoMensagem import CartaoMensagem

class MensagemDiaDosNamorados(CartaoMensagem):
    def __init__(self, destinatario):
        CartaoMensagem.__init__(self, destinatario)

    def retornar_mensagem(self, remetente):
        return "{}, Feliz Dia dos Namorados, meu amor! Espero que goste do meu cartão, foi escrito com muito amor! De todo meu coração, {}".format(self.destinatario, remetente)