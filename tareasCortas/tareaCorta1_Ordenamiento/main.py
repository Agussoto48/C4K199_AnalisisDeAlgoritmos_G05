from lib import arrays, calculos, vista

def main():
    #Array para saber el numero de cambios por ordenamiento
    cambios = []
    # 0: insercion
    # 1: seleccion
    # 2: burbuja
    matriz = []
    for i in range(10):
        matriz.append(arrays.crear_array())
    
    promedios = [0] * 3
    desviaciones = [0] * 3
    calculos.promedio(matriz, cambios, promedios)
    calculos.desviacion(cambios, desviaciones)

    vista.imprimirTabla(promedios, desviaciones)
    
    
main()
