# Creacion del array
import random
def crear_array():
    arr = []
    for i in range(100):
        arr.append(random.randint(1, 100))
    return arr