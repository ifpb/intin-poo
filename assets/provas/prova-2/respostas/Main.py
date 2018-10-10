from UrnaEletronica import UrnaEletronica
from CandidatoNaoExiste import CandidatoNaoExiste
from Eleitor import Eleitor
from Voto import Voto
from datetime import datetime

urna = UrnaEletronica()

sair = "nao"
while(sair == "nao"):
    print("Bem-vindo à Urna Eletrônica")
    nome = input("Digite o seu nome: ")
    tituloEleitor = input("Digite o numero do titulo de eleitor: ")
    numero = int(input("Digite o número do candidato que deseja votar para presidente: "))
    try:
        candidato = urna.recuperarCandidato(numero)
        eleitor = Eleitor(nome, tituloEleitor)
        voto = Voto(datetime.now(), candidato, eleitor)
        urna.adicionarVoto(voto)
        sair = input("Deseja sair? (sim,nao)")
    except CandidatoNaoExiste:
        print("Candidato não existe, tente novamente")

print("Votação Encerrada")

print("----------------")
todosOsVotos = urna.listarTodosOsVotos()
print("Total de Votos: ",len(todosOsVotos))
for voto in todosOsVotos:
    print(voto)

print("----------------")
haddad = urna.recuperarCandidato(13)
votosHaddad = urna.listarVotos(haddad)
print("Total de Votos de Fernando Haddad: ", len(votosHaddad))
for voto in votosHaddad:
    print(voto)

print("----")
bolsonaro = urna.recuperarCandidato(17)
votosBolsonaro = urna.listarVotos(bolsonaro)
print("Total de Votos de Jair Bolsonaro: ", len(votosBolsonaro))
for voto in votosBolsonaro:
    print(voto)
