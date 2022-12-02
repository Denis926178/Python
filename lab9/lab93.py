# Кузнецов Денис ИУ7-13Б
# Программа для траинспонирования матрицы

from def_fool import check_int_number, check_material_number


def transposition(A):
    N = len(A[0])
    M = len(A)

    if N != M:
        print('Данная матрица не является квадратной')
        return 0
    for i in range(N):
        for j in range(i + 1, N):
            A[i][j], A[j][i] = A[j][i], A[i][j]
    for i in range(N):
        for j in range(N):
            print('{:6.2f}'.format(matrix[i][j]), end="")
        print('\n')
    return A

N = input('Введите порядок матрицы: ')
while not check_int_number(N):
    print('Неверно введенный порядок матрицы')
    N = input('Введите порядок матрицы: ')
    
N = int(N)
matrix = []

for i in range(N):
    matrix_str = list(map(str,\
                          input('Введите строку матрицы состоящую из {:} элементов: '\
                                .format(N)).split()))
    while len(matrix_str) != N:
        print('Неверно введенная строка матрицы')
        matrix_str = list(map(str,\
                          input('Введите строку матрицы состоящую из {:} элементов: '\
                                .format(N)).split()))
    for i in range(N):
        while not check_material_number(matrix_str[i]):
            print('Неверно введенный массив, все элементы должны быть числами')
            matrix_str[i] = input('Введите заново {:} элемент массива: '.format(i+1))
        else:
            matrix_str[i] = float(matrix_str[i])
            
    matrix.append(matrix_str)
transposition(matrix)
