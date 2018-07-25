from CartaoMensagem import CartaoMensagem

class MensagemNatal(CartaoMensagem):
    def __init__(self, destinatario):
        CartaoMensagem.__init__(self, destinatario)

    def retornar_mensagem(self, remetente):
        return "{}, Feliz Natal! Feliz por passarmos mais uma data especial juntos. Amo você e nossos filhos! De todo meu coração, {}".format(self.destinatario, remetente)