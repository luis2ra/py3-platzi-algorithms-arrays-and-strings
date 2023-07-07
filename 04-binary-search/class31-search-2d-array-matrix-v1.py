# 

'''
Escribir un algoritmo eficiente que busque un valor objetivo en una matriz de m x n enteros.

La matriz tiene las siguientes propiedades:
- Los enteros de cada fila están ordenados de izquierda a derecha.
- El primer entero de cada fila es mayor al último entero de la fila anterior.

Retorna True si el valor objetivo se encuentra en la matriz. Si no, retorna False.

Ejemplo 1:

# Input
matriz = [
  [1,3,5,7],
  [10,11,16,20],
  [23,30,34,60],
]

# Output
True


Ejemplo 2:

# Input
matriz = [
  [1,3,5,7],
  [10,11,16,20],
  [23,30,34,60],
]
searchInMatrix(matriz, 12)

# Output
False

'''
from typing import List


def search_in_matrix(matriz: List[List[int]], objetivo: int) -> bool:
    arriba = 0
    abajo = len(matriz) - 1
    counter = 0
    while arriba < abajo:
        counter += 1
        mitad = arriba + (abajo - arriba) // 2
        if matriz[mitad][0] == objetivo:
            print("lo consegui!!!")  # si esta en la primera columna
            return True
        if matriz[mitad][0] < objetivo:
            arriba = mitad + 1
            print(f"matriz[{mitad}][0] = {matriz[mitad][0]} - arriba: {arriba} - abajo: {abajo} - actualizado arriba")
        else:
            abajo = mitad - 1
            print(f"matriz[{mitad}][0] = {matriz[mitad][0]} - arriba: {arriba} - abajo: {abajo} - actualizado abajo")
        if counter > 10: return False
    fila = matriz[mitad]
    izquierda = 0
    derecha = len(fila) - 1
    while izquierda <= derecha:
        mitad2 = izquierda + (derecha - izquierda) // 2
        if fila[mitad2] == objetivo:
            print("lo consegui!!!")
            return True
        if fila[mitad2] < objetivo:
            izquierda = mitad2 + 1
            print(f"fila[{mitad2}] = {fila[mitad2]} - izquierda: {izquierda} - derecha: {derecha} - actualizado izquierda")
        else:
            derecha = mitad2 - 1
            print(f"fila[{mitad2}] = {fila[mitad2]} - izquierda: {izquierda} - derecha: {derecha} - actualizado derecha")
    return False


matriz = [
    [1,3,5,7],
    [10,11,16,20],
    [23,30,34,60],
]

# matriz = [
#     [ 1, 3, 5, 7, 9,11,13],
#     [17,19,21,23,27,29,30],
#     [33,35,37,39,41,44,47],
#     [51,53,55,57,59,63,67],
#     [70,73,75,77,79,81,88],
# ]

print(matriz)

response = search_in_matrix(matriz, int(input()))
print(response)

# response2 = search_in_matrix(matriz, 12)
# print(response2)

# response3 = search_in_matrix(matriz, 20)
# print(response3)

# response4 = search_in_matrix(matriz, 34)
# print(response4)
