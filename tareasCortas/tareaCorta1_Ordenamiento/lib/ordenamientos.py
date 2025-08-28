
# Funcion por insercion
def insercion(array):
    #Se crea una copia del array para que no salga ordenado para las demas algoritmos
    arrayAux = array[:]
    swaps = 0
    for i in range(1, len(arrayAux)):
        key = arrayAux[i]
        j = i - 1
        while j >= 0 and key < arrayAux[j]:
            arrayAux[j + 1] = arrayAux[j]
            swaps += 1
            j -= 1
        arrayAux[j + 1] = key
    return swaps

# Funcion por seleccion
def seleccion(array):
    #Se crea una copia del array para que no salga ordenado para las demas algoritmos
    arrayAux = array[:]
    swaps = 0
    n = len(arrayAux)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if arrayAux[j] < arrayAux[min_idx]:
                min_idx = j
        if min_idx != i:
            swaps += 1
            arrayAux[i], arrayAux[min_idx] = arrayAux[min_idx], arrayAux[i]
    return swaps

# Funcion por orden burbuja
def burbuja(array):
    #Se crea una copia del array para que no salga ordenado para las demas algoritmos
    arrayAux = array[:]
    swaps = 0
    n = len(arrayAux)
    for i in range(n):
        intercambio = False
        for j in range(0, n-i-1):
            if arrayAux[j+1] < arrayAux[j]:
                arrayAux[j], arrayAux[j+1] = arrayAux[j+1], arrayAux[j]
                swaps += 1
                intercambio = True
        if not intercambio:
            break
    return swaps