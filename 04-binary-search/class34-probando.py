from typing import List


def searchInMatrix(matriz: List[List[int]], objetivo: int) -> bool:
    left = 0
    right = len(matriz[0])-1
    middle_col = 0
    top = 0
    bottom = len(matriz)-1
    middle_row = 0

    while(top<=bottom):
        middle_row = top + (bottom-top)//2

        if middle_row == bottom or middle_row == top:
            break

        if matriz[middle_row][-1] > objetivo:
            bottom = middle_row - 1
        else:
            top = middle_row + 1

    while(left<=right):
        middle_col = left + (right-left)//2
        if matriz[middle_row][middle_col] == objetivo:
            return True

        if matriz[middle_row][middle_col]>objetivo:
            right = middle_col - 1
        else:
            left = middle_col +1

    return False

matriz = [
    [1,3,5,7],
    [10,11,16,20],
    [23,30,34,60],
]
print(matriz)

response = searchInMatrix(matriz, int(input()))
print(response)
