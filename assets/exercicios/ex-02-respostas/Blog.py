from datetime import datetime

class Blog:
    def __init__(self):
        self.postagens = []

    def adicionarPostagem(self, postagem):
        self.postagens.append(postagem)

    def publicarPostagem(self, postagem):
        postagem.dataPublicacao = datetime.now()
        for postagemExistente in self.postagens:
            if postagemExistente.id == postagem.id:
                self.postagens.remove(postagemExistente)
        self.postagens.append(postagem)

    def listarPostagensPublicadas(self):
        postagensPublicadas = []
        for postagem in self.postagens:
            if postagem.dataPublicacao < datetime.now():
                postagensPublicadas.append(postagem)
        return postagensPublicadas

    def listarTodasAsPostagens(self):
        return self.postagens

    def apagarPostagem(self, postagem):
        for postagemExistente in self.postagens:
            if postagemExistente.id == postagem.id:
                self.postagens.remove(postagem)
