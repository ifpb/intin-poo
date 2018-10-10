from Candidato import Candidato
from Partido import Partido
from CandidatoNaoExiste import CandidatoNaoExiste


class UrnaEletronica:
    def __init__(self):
        self.candidatos = []
        self.votos = []
        self.__inicializar()

    def __inicializar(self):
        pt = Partido(13, "PT")
        candidato01 = Candidato("Fernando Haddad", pt)
        psl = Partido(17, "PSL")
        candidato02 = Candidato("Jair Bolsonaro", psl)
        self.candidatos.append(candidato01)
        self.candidatos.append(candidato02)
        self.secao = 123
        self.zona = 321

    def adicionarVoto(self, voto):
        self.votos.append(voto)

    def listarTodosOsVotos(self):
        return self.votos

    def listarVotos(self, candidato):
        votosCandidato = []
        for voto in self.votos:
            if voto.candidato.partido.numero == candidato.partido.numero:
                votosCandidato.append(voto)
        return votosCandidato

    def recuperarCandidato(self, numero):
        candidato = None
        for c in self.candidatos:
            if c.partido.numero == numero:
                candidato = c
        if candidato == None:
            raise CandidatoNaoExiste
        return candidato
