class Usuario:
    def __init__(self, id, nome, login, senha):
        self.id = id
        self.nome = nome
        self.login = login
        self.senha = senha

    def __str__(self):
        return "id={}, nome={}, login={}, senha={}".format(self.id, self.nome, self.login, self.senha)