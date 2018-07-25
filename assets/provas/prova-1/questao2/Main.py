from Cliente import Cliente
from ClienteEstudante import ClienteEstudante
from ClienteComDeficiencia import ClienteComDeficiencia

passagem_jp_cjz = 120

cliente_comum = Cliente("José", 22)
valor = cliente_comum.calcular_valor_final_passagem(passagem_jp_cjz)
print("Cliente {} deverá pagar {}" % (cliente_comum.nome, valor))

cliente_estudante = ClienteEstudante("Ana", 17)
valor = cliente_estudante.calcular_valor_final_passagem(passagem_jp_cjz)
print("Cliente %s deverá pagar %d" % (cliente_estudante.nome, valor))

cliente_idoso = Cliente("Ribamar", 67)
valor = cliente_idoso.calcular_valor_final_passagem(passagem_jp_cjz)
print("Cliente %s deverá pagar %d" % (cliente_idoso.nome, valor))

cliente_com_deficiencia = ClienteComDeficiencia("João", 25)
valor = cliente_com_deficiencia.calcular_valor_final_passagem(passagem_jp_cjz)
print("Cliente %s deverá pagar %d" % (cliente_com_deficiencia.nome, valor))

