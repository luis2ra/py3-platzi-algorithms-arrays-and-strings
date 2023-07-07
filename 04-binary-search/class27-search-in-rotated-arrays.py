# class 27: Search in Rotated Arrays

'''
Tienes una lista de números enteros ordenada de forma ascendente y sin valores repetidos.
Pero posiblemente la lista se encuentre rotada en un índice pivote desconocido.

Por ejemplo, [0,1,2,4,5,6,7] podría girar en el índice pivote 3 y convertirse en [4,5,6,7,0,1,2].

Dado un array nums (después de la posible rotación) y un entero objetivo, si objetivo se encuentra 
en nums, devuelve su índide o posición en el array, si no, devuelve -1.

Ejemplo 1:

// Input
lista = [4,5,6,7,0,1,2]
objetivo = 3

// Output
-1

Ejemplo 2:

// Input
lista = [12,13,9,10,11]
objetivo = 10

// Output
3

'''
from typing import List

def search_in_rotated_array(lista: List, objetivo: int):
    izquierda = 0
    derecha = len(lista) - 1
    while izquierda <= derecha:
        mitad = izquierda + (derecha - izquierda) // 2
        print(f"izq: {izquierda} - der: {derecha} - mitad: {mitad}")
        if lista[mitad] == objetivo:
            return mitad
        # se compara por los valores (a diferencia del binario base)
        if lista[mitad] >= lista[izquierda]:
            if objetivo >= lista[izquierda] and objetivo < lista[mitad]:
                derecha = mitad - 1
            else:    
                izquierda = mitad + 1
        else:
            if objetivo <= lista[derecha] and objetivo < lista[mitad]:
                izquierda = mitad + 1
            else:    
                derecha = mitad - 1
            
    return None


# lista = [12,13,9,10,11]
lista = [12,13,15,20,7,9,10,11]
objetivo = 10
print(search_in_rotated_array(lista, objetivo))
