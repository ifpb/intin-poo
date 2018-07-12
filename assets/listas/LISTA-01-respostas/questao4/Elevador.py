class Elevador:
    def __init__(self, andaresPredio=0, andarAtual=0, capacidadeMaxima=0, pessoasDentro=0):
        self.__andaresPredio = andaresPredio
        self.__andarAtual = andarAtual
        self.__capacidadeMaxima = capacidadeMaxima
        self.__pessoasDentro = pessoasDentro

    def inicializar(self, andaresPredio, capacidadeMaxima):
        self.__init__(andaresPredio, 0, capacidadeMaxima, 0)

    def entrar(self):
        if (self.__pessoasDentro < self.__capacidadeMaxima):
            self.__pessoasDentro += 1
        else:
            print("Capacidade maxima do elevador excedida")

    def sair(self):
        if (self.__pessoasDentro > 0):
            self.__pessoasDentro -= 1
        else:
            print("Não há ninguem no elevador")

    def subir(self):
        if (self.__andarAtual < self.__andaresPredio):
            self.__andarAtual += 1
        else:
            print("O elevador já se encontra no último andar, não é possível subir")

    def descer(self):
        if (self.__andarAtual > 0):
            self.__andarAtual -= 1
        else:
            print("O elevador já se encontra no térreo, não é possível descer")

    @property
    def andaresPredio(self):
        return self.__andaresPredio

    @andaresPredio.setter
    def andaresPredio(self, andaresPredio):
        self.__andaresPredio = andaresPredio

    @property
    def andarAtual(self):
        return self.__andarAtual

    @andarAtual.setter
    def andarAtual(self, andarAtual):
        self.__andarAtual = andarAtual

    @property
    def capacidadeMaxima(self):
        return self.__capacidadeMaxima

    @capacidadeMaxima.setter
    def capacidadeMaxima(self, capacidadeMaxima):
        self.__capacidadeMaxima = capacidadeMaxima

    @property
    def pessoasDentro(self):
        return self.__pessoasDentro

    @pessoasDentro.setter
    def pessoasDentro(self, pessoasDentro):
        self.__pessoasDentro = pessoasDentro