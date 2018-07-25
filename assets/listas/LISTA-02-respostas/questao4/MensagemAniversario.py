from CartaoMensagem import CartaoMensagem

class MensagemAniversario(CartaoMensagem):
    def __init__(self, destinatario):
        CartaoMensagem.__init__(self, destinatario)

    def retornar_mensagem(self, remetente):
        return "{}, Feliz Aniversário! Te desejo as melhores coisas do mundo! Te amo! {}".format(self.destinatario, remetente)