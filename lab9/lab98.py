# Кузнецов Денис ИУ7-13Б
# Программа для формирования новой матрицы с помощью перемножения двух матриц одинаковой размерности

from def_fool import check_int_number, check_material_number


def multiplication(A,B):
    C = []
    for i in range(len(A)):
        C_str = []
        for j in range(len(A[0])):
            C_el = A[i][j] * B[i][j]
            C_str.append(C_el)
        C.append(C_str)
    V = []
    for i in range(len(A[0])):
        sum_col = 0
        for j in range(len(A)):
            sum_col += C[j][i]
        V.append(sum_col)
    for i in range(len(A)):
        for j in range(len(A[0])):
            print('{:^6}'.format(C[i][j]), end="")
        print('\n')
    print(*V)
    return 0

N = input('Введите количество строчек в матрицах A, B: ')
while not check_int_number(N):
    N = input('Введите количество строчек в матрицах A, B: ')

M = input('Введите количество столбцов в матрбицах A, B: ')
while not check_int_number(M):
    M = input('Введите количество столбцов в матрицах A, B: ')

N = int(N)
M = int(M)
A = []
B = []

for i in range(N):
    matrix_str = list(map(str,\
                          input('Введите строку матрицы A, состоящую из {:} элементов: '.format(M)).split()))
    while len(matrix_str) != M:
        print('Неверно введенная строка матрицы')
        matrix_str = list(map(str,\
                          input('Введите строку матрицы состоящую из {:} элементов: '.format(M)).split()))
    for i in range(M):
        while not check_material_number(matrix_str[i]):
            print('Неверно введенный массив, все элементы должны быть числами')
            matrix_str[i] = input('Введите заново {:} элемент массива: '.format(i+1))
        matrix_str[i] = float(matrix_str[i])
        
    A.append(matrix_str)
    
for i in range(N):
    matrix_str = list(map(str,\
                          input('Введите строку матрицы B, состоящую из {:} элементов: '.format(M)).split()))
    while len(matrix_str) != M:
        print('Неверно введенная строка матрицы')
        matrix_str = list(map(str,\
                          input('Введите строку матрицы состоящую из {:} элементов: '.format(M)).split()))
    for i in range(len(matrix_str)):
        while not check_material_number(matrix_str[i]):
            print('Неверно введенный массив, все элементы должны быть числами')
            matrix_str[i] = input('Введите заново {:} элемент массива: '.format(i+1))
        matrix_str[i] = float(matrix_str[i])
        
    B.append(matrix_str)

multiplication(A,B)
            
            
            
