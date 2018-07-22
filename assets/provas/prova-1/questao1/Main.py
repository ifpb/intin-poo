from Pessoa import Pessoa
from CalculadoraAfinidade import CalculadoraAfinidade

pessoa1 = Pessoa("Coutinho", 27)
pessoa2 = Pessoa("Neymar", 26)
calculadora_afinidade = CalculadoraAfinidade()
afinidade = calculadora_afinidade.calcular_afinidade(pessoa1,pessoa2)

print("Afinidade entre %s e %s = %d " % (pessoa1.nome, pessoa2.nome, afinidade))