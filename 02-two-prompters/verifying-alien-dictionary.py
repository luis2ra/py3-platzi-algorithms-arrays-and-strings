# class 04: Verifying Alien Dictionary: análisis del problema

'''
En una lengua alienígena, sorprendentemente, también utilizan 
letras del español, pero posiblemente en un orden diferente, 
una permutación de nuestro alfabeto.

Dada una secuencia de palabras escritas en el idioma terrícola, 
y el orden del alfabeto, devuelve verdadero si y solo si las palabras 
están ordenadas lexicográficamente en este idioma extraterrestre.
'''
palabras = ["conocer", "cono"]
orden_alfabeto = "abcdefghijklmnopqrstuvwxyz"

palabras = ["habito", "hacer", "lectura", "sonreir"]
orden_alfabeto = "hlabcdefgijkmnopqrstuvwxyz"


def encuentra_palabra(p1, p2):
    while p1 != orden_alfabeto[p2] and p2 < len(orden_alfabeto):
        print(p1, orden_alfabeto[p2])
        if p1 == orden_alfabeto[p2]:
            p2 += 1
            return True
    return False

p1 = 0
p2 = 0
for p in palabras:
    if encuentra_palabra(p[0], p2):
        p1 += 1
    else:
        print(False)
        break
print(True) if p1 == len(palabras) else print()
