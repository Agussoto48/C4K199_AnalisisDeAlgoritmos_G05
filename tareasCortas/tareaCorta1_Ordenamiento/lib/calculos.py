from lib import ordenamientos
import statistics

#Promedios
def promedioInsercion(matriz, cambios):
    swaps = [0] * 10
    for i in range(10):
        swaps[i] += ordenamientos.insercion(matriz[i])
    cambios.append(swaps)
    return statistics.mean(swaps)

def promedioSeleccion(matriz, cambios):
    swaps = [0] * 10
    
    for i in range(10):
        swaps[i] += ordenamientos.seleccion(matriz[i])
    cambios.append(swaps)
    return statistics.mean(swaps)

def promedioBurbuja(matriz, cambios):
    swaps = [0] * 10
    for i in range(10):
        swaps[i] += ordenamientos.burbuja(matriz[i])
    cambios.append(swaps)
    return statistics.mean(swaps)

def promedio(matriz, cambios, promedios):
    promedios[0] = promedioInsercion(matriz, cambios)
    promedios[1] = promedioSeleccion(matriz, cambios)
    promedios[2] = promedioBurbuja(matriz, cambios)

#Desviacion estandar 
def desviacion(cambios, desviaciones):
    for i in range(3):
        desviaciones[i] += statistics.stdev(cambios[i]) 

