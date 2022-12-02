# Кузнецов Денис ИУ7-13Б
# Программа для вывода среза по 2 индеку из трехмерного массива

from def_fool import check_int_number


def print_slice(A, X, Y, Z):
    index = int(input('Введите значение индекса, ко которому будет делаться срез: '))
    for i in range(Z):
        for j in range(X):
            for k in range(index, Y):
                print('{:^5}'.format(A[i][j][k]), end="")
            print('\n')
        print('-----'*(Y-index))
    return 0

X = input('Введите количество строк в трехмерном массиве: ')
while not check_int_number(X):
    X = input('Введите количество строк в трехмерном массиве: ')

Y = input('Введите количество столбцов в трехмерном массиве: ')
while not check_int_number(Y):
    Y = input('Введите количество столбоцв в трехмерном массиве: ')

Z = input('Введите количество слоев в трехмерном массиве: ')
while not check_int_number(Z):
    Z = input('Введите количество столев в трехмерном массиве: ')

X = int(X)
Y = int(Y)
Z = int(Z)
matrix_Z = []

for i in range(Z):
    matrix = []
    for j in range(X):
        matrix_str = list(map(str,\
                              input('Введите строку матрицы,\
состоящую из {:} элементов {:} слоя: '.format(Y, i+1)).split()))
        while len(matrix_str) != Y:
            print('Неверный ввод строки трехмерного массива')
            matrix_str = list(map(str,\
                              input('Введите строку матрицы,\
состоящую из {:} элементов {:} слоя: '.format(Y, i+1)).split()))
            
        matrix.append(matrix_str)
    matrix_Z.append(matrix)
print('\n')
print_slice(matrix_Z, X, Y, Z)
