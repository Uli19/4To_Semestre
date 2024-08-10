import math

class Main:
    def __init__(self):
        self.datos = [2.2, 4.1, 3.5, 4.5, 3.2, 3.7, 3.0, 2.6,
                      3.4, 1.6, 3.1, 3.3, 3.8, 3.1, 4.7, 3.7,
                      2.5, 4.3, 3.4, 3.6, 2.9, 3.3, 3.9, 3.1,
                      3.3, 3.1, 3.7, 4.4, 3.2, 4.1, 1.9, 3.4,
                      4.7, 3.8, 3.2, 2.6, 3.9, 3.0, 4.2, 3.5]

    def run(self):
        print(" Media: ", self.media())
        print(" Mediana: ", self.mediana())
        print(" Varianza: ", self.varianza())
        print(" Desviación Estandar: ", self.desviacion_estandar())

    def media(self):
        media = 0
        for x in self.datos:
            media += x
        media /= len(self.datos)
        return media
    
    def mediana(self):
        datos_ordenados = sorted(self.datos)
        n = len(datos_ordenados)
        if n % 2 == 0:
            return (datos_ordenados[((n//2)-1)] + datos_ordenados[(n//2)]) / 2
        else:
            return datos_ordenados[((n+1)//2)-1]
    
    def varianza(self):
        var = 0
        n = len(self.datos)
        media = self.media()
        for x in self.datos:
            var += ((x - media) ** 2) / (n - 1)
        return var
    
    def desviacion_estandar(self):
        varianza = self.varianza()
        return math.sqrt(varianza)


if __name__ == '__main__':
    main = Main()
    main.run()