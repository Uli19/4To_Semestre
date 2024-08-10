import matplotlib.pyplot as plt

# Datos para el histograma
datos = [2.2, 4.1, 3.5, 4.5, 3.2, 3.7, 3.0, 2.6,
        3.4, 1.6, 3.1, 3.3, 3.8, 3.1, 4.7, 3.7,
        2.5, 4.3, 3.4, 3.6, 2.9, 3.3, 3.9, 3.1,
        3.3, 3.1, 3.7, 4.4, 3.2, 4.1, 1.9, 3.4,
        4.7, 3.8, 3.2, 2.6, 3.9, 3.0, 4.2, 3.5]

# Crear el histograma
plt.hist(datos, bins=7, range=(1.5, 4.9))# Especifica el número de contenedores y el color del borde
plt.xlabel('Valor')
plt.ylabel('Frecuencia')
plt.title('Histograma')

# Mostrar el histograma
plt.show()
