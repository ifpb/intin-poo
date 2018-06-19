from Pessoa import Pessoa
from pprint import pprint

pessoa = Pessoa("Diego", 29, 95, 1.88)

pessoa.envelhecer(1)
print("Nova altura: %f " % pessoa.altura)

imc = Pessoa.imc(pessoa.peso, pessoa.altura)
print("IMC = %f "% imc)

pessoa.nome = "Teste"

pprint(vars(pessoa))

