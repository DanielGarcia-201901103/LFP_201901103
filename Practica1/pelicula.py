class Pelicula:
    def __init__(self, nombre,actores, year, genero):
        self.nombrePelicula = nombre #string
        self.actores = actores # lista de nombres string
        self.year = year # numero
        self.generoPelicula = genero # string

    def setNombrePelicula(self, nombrePelicula):
        self.nombrePelicula = nombrePelicula
    
    def getNombrePelicula(self):
        return self.nombrePelicula
    
    def setYear(self, year):
        self.year = year
    
    def getYear(self):
        return self.year

    def setGeneroPelicula(self,genero):
        self.generoPelicula = genero

    def getGeneroPelicula(self):
        return self.generoPelicula