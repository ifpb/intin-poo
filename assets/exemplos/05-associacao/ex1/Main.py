from Aviao import Aviao
from CoordenadaGeografica import CoordenadaGeografica

#Avião está em cajazeiras:
coordenadacjz = CoordenadaGeografica(-6.889579, -38.543901)
aviaocjz = Aviao("Boing 733", "GOL-1234", coordenadacjz)

#Avião está em João Pessoa:
coordenadajp = CoordenadaGeografica(-7.134814, -34.874397)
aviaojp = Aviao("Boing123", "AZUL-1233", coordenadajp)

print("Distancia entre os avioes = ", aviaocjz.distancia(aviaojp), "km")