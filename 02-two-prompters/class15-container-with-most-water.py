# Problem: Container With Most Water

'''
En este desafío vas a recibir una lista de números que representan un grupo de líneas con diferentes alturas.
Encuentra las dos líneas que forman el contenedor que más agua puede contener.
Debes retornar esa máxima cantidad de agua que puede almacenar un contendor.

Ejemplo 1:

// Input
alturas = [1,8,6,2,5,4,8,3,7]

// Output
49

Ejemplo 2:

// Input
alturas = [8,1,6,2,5,4,1,3,7]

// Output
56

'''
from typing import List


def maxima_area(alturas: List)->int:
    left_pointer = 0                # left pointer
    right_pointer = len(alturas)-1  # right pointer
    max_area = -1

    while left_pointer < right_pointer:
        # compute area
        area = (right_pointer - left_pointer) * min(alturas[left_pointer], alturas[right_pointer])
        # get max. area
        max_area = max(area, max_area)
        print(f"Area: {max_area} y la diferencia de la base {left_pointer} y {right_pointer}: ", right_pointer-left_pointer)
        # discard smallest value
        if alturas[left_pointer] < alturas[right_pointer]:
            left_pointer += 1
        else:
            right_pointer -= 1
    return max_area


alturas = [1,8,6,2,5,4,8,3,7]
# alturas = [8,1,6,2,5,4,1,3,7]

print(maxima_area(alturas))
