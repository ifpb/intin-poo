from Haversine import distance

class CoordenadaGeografica:
    def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude

    def calcularDistancia(self, coordenada):
        lat1 = self.latitude
        long1 = self.longitude
        lat2 = coordenada.latitude
        long2 = coordenada.longitude
        distancia = (lat1+long1) - (lat2+long2)
        return distancia

    def calcularDistanciaReal(self, coordenada):
        lat1 = self.latitude
        long1 = self.longitude
        lat2 = coordenada.latitude
        long2 = coordenada.longitude
        distancia = distance((lat1,long1),(lat2,long2))
        return distancia
