# Función para encontrar el número más frecuente en una lista
def numero_mas_frecuente(lista):
    # Creamos un diccionario para guardar la cantidad de veces que aparece cada número
    frecuencias = {}

    # Contamos cuántas veces aparece cada número en la lista
    for numero in lista:
        if numero in frecuencias:
            frecuencias[numero] += 1
        else:
            frecuencias[numero] = 1

    # Buscamos la frecuencia más alta
    mayor_frecuencia = 0
    for valor in frecuencias.values():
        if valor > mayor_frecuencia:
            mayor_frecuencia = valor

    # Creamos una lista con los números que tienen la mayor frecuencia
    candidatos = []
    for clave in frecuencias:
        if frecuencias[clave] == mayor_frecuencia:
            candidatos.append(clave)

    # Retornamos el menor de los candidatos
    return min(candidatos)


print(numero_mas_frecuente([1, 3, 1, 3, 2, 1]))
print(numero_mas_frecuente([4, 4, 5, 5]))
