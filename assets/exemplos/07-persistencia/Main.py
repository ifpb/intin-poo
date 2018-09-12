from Pessoa import Pessoa
from Endereco import Endereco
from Usuario import Usuario

import shelve

class Main:
    def __init__(self):
        self.db = shelve.open("db.db")

    def criarUsuarios(self):
        endereco = Endereco("Rua Y", "Cajazeiras", "PB")
        pessoa = Pessoa("Gastão", 40, endereco)
        usuario = Usuario("gastao", "321", pessoa)
        self.db[usuario.login] = usuario

    def validarLogin(self, login, senha):
        usuario = self.db[login]
        if usuario != None and usuario.login == login and usuario.senha == senha:
            print("Usuário logado!")
        else:
            print("Usuário invalido!")

    def exibirEndereco(self, login):
        usuario = self.db[login]
        print(usuario.pessoa.endereco)

    def listarUsuarios(self):
        usuarios = []
        for key in self.db.keys():
            usuarios.append(self.db[key])
        return usuarios

    def apagarUsuario(self, login):
        usuario = self.db[login]
        if (usuario != None):
            del self.db[login]

    def atualizarUsuario(self, usuario):
        self.db[usuario.login] = usuario

    def recuperarUsuario(self, login):
        return self.db[login]

main = Main()
usuario = main.recuperarUsuario("diego")
usuario.pessoa.endereco.rua = "Rua Dimas Andriola"
main.atualizarUsuario(usuario)
#main.apagarUsuario("gastao")
#main.criarUsuarios()
#main.validarLogin("diego", "123")
#main.exibirEndereco("diego")


for usuario in main.listarUsuarios():
    print(usuario.pessoa.nome)
    print(usuario.pessoa.endereco)