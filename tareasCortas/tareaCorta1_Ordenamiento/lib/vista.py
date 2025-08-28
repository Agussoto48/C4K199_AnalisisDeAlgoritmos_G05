from tabulate import tabulate

def imprimirTabla(promedios, desviaciones):
    datos = [
        ["Insercion ", promedios[0], desviaciones[0]],
        ["Seleccion ", promedios[1], desviaciones[1]],
        ["Burbuja ", promedios[2], desviaciones[2]],
    ]
    print(tabulate(datos, headers=["Ordenamiento", "Promedio", "Desviacion"], tablefmt="grid"))