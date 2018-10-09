class Postagem:
    def __init__(self, id, titulo, texto, dataPublicacao):
        self.id = id
        self.titulo = titulo
        self.texto = texto
        self.dataPublicacao = dataPublicacao

    def __str__(self):
        return "id={}, titulo={}, texto={}, dataPublicacao={}".format(self.id, self.titulo, self.texto, self.dataPublicacao)