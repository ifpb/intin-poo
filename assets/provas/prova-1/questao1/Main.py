from Pessoa import Pessoa
from CalculadoraAfinidade import CalculadoraAfinidade

pessoa1 = Pessoa("Coutinho", 27)
pessoa2 = Pessoa("Neymar", 26)
calculadora = CalculadoraAfinidade()
afinidade = calculadora.calcular_afinidade(pessoa1,pessoa2)

print("Afinidade entre %s e %s = %d " % (pessoa1.nome, pessoa2.nome, afinidade))