# class 19: Patrón de Ventana Deslizante

'''
Modelo de recorrido usando el patrón de ventana deslizante

'''

def ventana_deslizante(lista, k):
    inicio_ventana = 0
    for fin_ventana in range(len(lista)):
        resultado = 0
        # Aca se aplica alguna logica segun el tipo de problema
        if fin_ventana >= k - 1:
            # Aca complementaria la logica para controlar la solucion
            print(f"sublista: {lista[inicio_ventana:fin_ventana+1]}")
            inicio_ventana += 1

    return resultado


def main():
    resultado = ventana_deslizante(lista, k)


k = 3
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]

main()
