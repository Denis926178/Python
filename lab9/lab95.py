# Кузнецов Денис ИУ7-13Б
# Программа для преобразования матрицы D

from def_fool import check_int_number, check_material_number


def change_matrix_D(D, Z):
    N = len(D)
    M = len(D[0])
    G = []
    for i in range(N):
        counter = 0
        sum_str_Z = sum(Z[i])
        for j in range(M):
            if D[i][j] > sum_str_Z:
                counter += 1
        G.append(counter)
    max_el = max(G)
    for i in range(N):
        for j in range(M):
            print('{:6.2f}'.format(D[i][j]), end="")
            D[i][j] *= max_el
        print('\n')
    print('-------------------------------')
    for i in range(N):
        for j in range(M):
            print('{:6.2f}'.format(D[i][j]), end="")
        print('\n')
    print(*G)
        
N = input('Введите количество строк в матрице D: ')
while not check_int_number(N):
    N = input('Введите количество строк в матрице D: ')

M = input('Введите количество столбцов в матрице D: ')
while not check_int_number(M):
    M = input('Введите количество столбцов в матрице D: ')

N = int(N)
M = int(M)
D = []

for i in range(N):
    matrix_str = list(map(str,\
                          input('Введите строку матрицы D,\
состояющую из {:} элементов: '.format(M)).split()))
    while len(matrix_str) != N:
        print('Неверно введенная строка матрицы')
        matrix_str = list(map(str,\
                          input('Введите строку матрицы состоящую из {:} элементов: '.format(M)).split()))
    for i in range(N):
        while not check_material_number(matrix_str[i]):
            print('Неверно введенный массив, все элементы должны быть числами')
            matrix_str[i] = input('Введите заново {:} элемент массива: '.format(i+1))
        else:
            matrix_str[i] = float(matrix_str[i])
    D.append(matrix_str)

N = input('Введите количество строк в матрице Z: ')
while not check_int_number(N):
    N = input('Введите количество строк в матрице Z: ')

M = input('Введите количество столбцов в матрице Z: ')
while not check_int_number(M):
    M = input('Введите количество столбцов в матрице Z: ')

N = int(N)
M = int(M)
Z = []

for i in range(N):
    matrix_str = list(map(str,\
                          input('Введите строку матрицы Z,\
состояющую из M элементов: ').split()))
    while len(matrix_str) != N:
        print('Неверно введенная строка матрицы')
        matrix_str = list(map(str,\
                          input('Введите строку матрицы состоящую из {:} элементов: '.format(N)).split()))
    for i in range(N):
        while not check_material_number(matrix_str[i]):
            print('Неверно введенный массив, все элементы должны быть числами')
            matrix_str[i] = input('Введите заново {:} элемент массива: '.format(i+1))
        else:
            matrix_str[i] = float(matrix_str[i])
    Z.append(matrix_str)
change_matrix_D(D,Z)
            
        
    
