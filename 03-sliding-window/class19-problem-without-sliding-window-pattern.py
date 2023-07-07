# class 19: Patrón de Ventana Deslizante
# referencia a blog: https://medium.com/gdg-ipn/patr%C3%B3n-1-la-ventana-deslizante-triunfando-en-la-entrevista-de-c%C3%B3digo-b3d3738218ce

'''
Problema resuelto sin usar el patron de ventana deslizante:

Dada una lista de calificaciones, encuentra el promedio de todas las sublistas contiguas de tamaño “k”

'''
def promedio_sublistas(k, calificaciones):
    resultado = []
    for i in range(len(calificaciones)-k+1):
        suma = 0.0
        for j in range(i, i+k):
            suma += calificaciones[j]
        resultado.append(suma/k)

    return resultado


def main():
    resultado = promedio_sublistas(k, notas)
    print("Promedios: " + str(resultado))


k = 3
notas = [10.0, 7.8, 6.5, 8.0, 9.2]
main()
