# class 26: Algoritmo de Búsqueda Binaria


def binary_search(numeros, objetivo):
    izquierda = 0
    derecha = len(numeros) - 1
    while izquierda <= derecha:
        mitad = izquierda + (derecha - izquierda) // 2
        print(f"izq: {izquierda} - der: {derecha} - mitad: {mitad}")
        if numeros[mitad] == objetivo:
            return True
        elif numeros[mitad] < objetivo:
            izquierda = mitad + 1
        else:
            derecha = mitad - 1
    return None


numeros = [11, 56, 99, 1, 8, 5, 16, 72, 40, 23, 7]
print("data inicial: ", numeros)
numeros.sort()
print("ordenados: ", numeros)

nro_objetivo = int(input("Ingresa el numero a buscar: "))
if binary_search(numeros, nro_objetivo):
    print(f"El numero {nro_objetivo} esta en la lista")
else:
    print(f"El numero {nro_objetivo} no esta en la lista!")
