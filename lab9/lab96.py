# Кузнецов Денис ИУ7-13Б
# Программа для нахождения максимальных элементах в строках матрицы

from def_fool import check_int_number, check_material_number


def calculation_R(D, L):
    R = []
    for i in range(len(L)):
        string_number = L[i]
        if string_number > 0 and string_number < len(D[0]):
            max_el = max(D[string_number - 1])
        else:
            print('В матрице нет строки с номером {:}'.format(string_number))
        R.append(max_el)
    if len(R) == 0:
        arithmetic_mean = 0
    else:
        arithmetic_mean = sum(R) / len(R)
    for i in range(len(D)):
        for j in range(len(D[0])):
            print('{:6.2f}'.format(D[i][j]), end="")
        print('\n')

    print(*L)
    print(*R)
    print(arithmetic_mean)

N = input('Введите количество строк в матрице: ')
while not check_int_number(N):
    N = input('Введите количество строк в матрице: ')

M = input('Введите количество столбцов в матрице: ')
while not check_int_number(M):
    M = input('Введите количество столбцов в матрице: ')

N = int(N)
M = int(M)
matrix = []

for i in range(N):
    matrix_str = list(map(str,\
                          input('Введите строку матрицы, состояющую из {:} элементов: '.format(M)).split()))
    while len(matrix_str) != N:
        print('Неверно введенная строка матрицы')
        matrix_str = list(map(str,\
                          input('Введите строку матрицы, состоящую из {:} элементов: '.format(N)).split()))
    for i in range(len(matrix_str)):
        while not check_material_number(matrix_str[i]):
            print('Неверно введенный массив, все элементы должны быть числами')
            matrix_str[i] = input('Введите заново {:} элемент массива: '.format(i+1))
        else:
            matrix_str[i] = float(matrix_str[i])
            
    matrix.append(matrix_str)
L = list(map(str,\
             input('Введите массив L: ').split()))
for i in range(len(L)):
            while not check_int_number(L[i]):
                print('Неверно введенный массив, все элементы должны быть целыми числами')
                L[i] = input('Введите заново {:} элемент массива: '.format(i+1))
            else:
                L[i] = int(L[i])
calculation_R(matrix, L)
