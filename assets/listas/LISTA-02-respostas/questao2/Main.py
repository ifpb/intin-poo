from Empregado import Empregado

empregado1 = Empregado("Jose", "Ailton", 2500)
empregado2 = Empregado("Francisco", "Alves", 2000)

print("Salario mensal de %s %s = %f" % (empregado1.primeiro_nome, empregado1.segundo_nome, empregado1.salario_mensal))
print("Salario anual de %s %s = %f" % (empregado1.primeiro_nome, empregado1.segundo_nome, empregado1.salario_anual()))
print("Salario mensal de %s %s = %f" % (empregado2.primeiro_nome, empregado2.segundo_nome, empregado2.salario_mensal))
print("Salario anual de %s %s = %f" % (empregado2.primeiro_nome, empregado2.segundo_nome, empregado2.salario_anual()))

empregado1.salario_mensal *= 1.1
empregado2.salario_mensal *= 1.1
print("Concedido aumento de 10% para todos os funcionários")

print("Salario mensal de %s %s = %f" % (empregado1.primeiro_nome, empregado1.segundo_nome, empregado1.salario_mensal))
print("Salario anual de %s %s = %f" % (empregado1.primeiro_nome, empregado1.segundo_nome, empregado1.salario_anual()))
print("Salario mensal de %s %s = %f" % (empregado2.primeiro_nome, empregado2.segundo_nome, empregado2.salario_mensal))
print("Salario anual de %s %s = %f" % (empregado2.primeiro_nome, empregado2.segundo_nome, empregado2.salario_anual()))