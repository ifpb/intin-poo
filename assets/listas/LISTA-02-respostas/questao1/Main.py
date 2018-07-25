from Fatura import Fatura


fatura = Fatura(1, "Livros de programacao", 1, 80.00)

print("Total da fatura = ",fatura.calcular_valor_fatura())