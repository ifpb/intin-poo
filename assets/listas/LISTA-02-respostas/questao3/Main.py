from Data import Data

data = Data(20, 7, 2018)
print("Data atual = ",data)
data.dia_seguinte()
print("Dia seguinte = ", data)

data = Data() #hoje
print("Data atual = ", data)
data.dia_seguinte()
print("Dia seguinte = ", data)

data = Data(28, 2, 2018)
print("Data fim do mês = ", data)
data.dia_seguinte()
print("Dia seguinte = ", data)

data = Data(31, 12, 2018)
print("Data no fim do ano = ",data)
data.dia_seguinte()
print("Dia seguinte = ", data)