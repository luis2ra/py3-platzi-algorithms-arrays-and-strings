# Patrón 2: Los dos punteros — Triunfando en la entrevista de código
# https://medium.com/gdg-ipn/patr%C3%B3n-2-los-dos-punteros-triunfando-en-la-entrevista-de-c%C3%B3digo-cba42268e088

'''
Dada una lista de enteros, regresa los índices de los dos números que sumen un valor específico.

Puedes asumir que sólo habrá una solución y que no puedes utilizar el mismo elemento dos veces.

Ejemplo:

Entradas:
lista = [1, 2, 7, 11, 19]
suma = 9

Salida:
solución = [1, 2]

'''

def find_two_addends(lista, suma):
    puntero_izquierdo = 0
    puntero_derecho = len(lista) - 1

    while puntero_izquierdo < puntero_derecho:
        suma_actual = lista[puntero_izquierdo] + lista[puntero_derecho]
    
        if suma_actual == suma:
            return [puntero_izquierdo, puntero_derecho]
        if suma > suma_actual:
            puntero_izquierdo += 1
        else:
            puntero_derecho -= 1
    return None


def main():
    resultado = find_two_addends([1, 2, 7, 11, 19], 9)
    if resultado is not None:
        print(f"Indices: {resultado}")
    else:
        print(f"No existe solucion!!!")


main()
