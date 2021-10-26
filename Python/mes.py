class Mes:
    nombre = ""
    maxima = 0
    minima = 0

    def getMedia(self):
        return (self.maxima + self.minima) / 2

    #Por comodidad, voy a devolver en el print del objeto
    #el nombre del mes, la maxima, minima y media
    def __str__(self):
        return (self.nombre + ", Maxima: " + str(self.maxima)
        + ", Minima: " + str(self.minima) + ", Media: " + str(self.getMedia()))