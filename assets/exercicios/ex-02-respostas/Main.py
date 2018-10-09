from Blog import Blog
from Postagem import Postagem
from Usuario import Usuario
from datetime import datetime
from datetime import timedelta


usuario = Usuario(1, "admin", "admin", "123")
login = input("Digite o login do usuario: ")
senha = input("Digite a senha do usuario: ")

if login != usuario.login or senha != usuario.senha:
    print("Usuario ou senha invalidos")
    exit()

blog = Blog()
postagem01 = Postagem(1, "Olá, pessoal!", "Lorem ipsum", datetime.now())
blog.adicionarPostagem(postagem01)
postagem02 = Postagem(2, "Essa notícia só vai entrar amanhã", "Lorem lorem", datetime.now() + timedelta(days=1))
blog.adicionarPostagem(postagem02)
postagem03 = Postagem(3, "Essa notícia vai entrar daqui a pouco", "Lorem lorem", datetime.now() + timedelta(hours=1))
blog.adicionarPostagem(postagem03)
blog.publicarPostagem(postagem03)
postagem04 = Postagem(4, "Essa notícia vai entrar e será removida logo após", "Lorem lorem", datetime.now())
blog.adicionarPostagem(postagem04)
blog.apagarPostagem(postagem04)

print("Postagens publicadas:")
for postagem in blog.listarPostagensPublicadas():
    print(postagem)

print("Todas as postagens:")
for postagem in blog.listarTodasAsPostagens():
    print(postagem)