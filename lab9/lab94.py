# Кузнецов Денис ИУ7-13Б
# Программа для поворота квадратной матрицы на 90 градусов по часовой стрелке

from def_fool import check_int_number, check_material_number


def rotate_90(A):
    N = len(A[0])
    M = len(A)
    if N != M:
        print('Данная матрица не является квадратной')
        return 0
    for i in range(N // 2):
        for j in range(i, N - i - 1):
            A[i][j], A[j][N - i - 1], A[N - 1 - i][N - 1 - j], A[N - 1 - j][i] = \
                     A[N - 1 - j][i], A[i][j], A[j][N - i - 1], A[N - i - 1][N - 1 - j]
    for i in range(N):
        for j in range(N):
            print('{:6.2f}'.format(A[i][j]), end="")
        print('\n')
    for i in range(N // 2):
        for j in range(i, N - i - 1):
            A[i][j], A[j][N - i - 1], A[N - 1 - i][N - 1 - j], A[N - 1 - j][i] = \
                     A[j][N - i - 1], A[N - 1 - i][N - 1 - j], A[N - 1 - j][i], A[i][j]
        
K = input('Введите порядок матрицы: ')
while not check_int_number(K):
    K = input('Введите порядок матрицы: ')
    
K = int(K)
matrix = []

for i in range(K):
    matrix_str = list(map(str,\
                          input('Введите строку матрицы состоящую из {:} элементов: '.format(K)).split()))
    while len(matrix_str) != K:
        print('Неверно введенная строка матрицы')
        matrix_str = list(map(str,\
                          input('Введите строку матрицы состоящую из {:} элементов: '.format(K)).split()))
    for i in range(K):
        while not check_material_number(matrix_str[i]):
            print('Неверно введенный массив, все элементы должны быть числами')
            matrix_str[i] = input('Введите заново {:} элемент массива: '.format(i+1))
        else:
            matrix_str[i] = float(matrix_str[i])
            
    matrix.append(matrix_str)
matrix = rotate_90(matrix)
