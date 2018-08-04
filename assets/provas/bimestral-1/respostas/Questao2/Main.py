from VeiculoImportado import VeiculoImportado
from VeiculoNacional import VeiculoNacional

importado = VeiculoImportado("Ferrari", "Azul", "ABC-1234", 2, 100000)
nacional = VeiculoNacional("Gol", "Branco", "AXZ-1132", 4, 25000)

print("Preco do importado = ", importado.preco)
print("Preco do nacional = ", nacional.preco)

print(importado)
print(nacional)