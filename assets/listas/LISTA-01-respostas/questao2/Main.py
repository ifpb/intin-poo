from ContaImposto import ContaImposto

conta = ContaImposto("12345-6", "123-1", 1000, "01", 0.25)

print("Saldo da conta após o desconto dos impostos %d " % conta.calcularImposto())