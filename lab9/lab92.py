# Кузнецов Денис ИУ7-13Б
# Программа для нахождения максимального значения над главной диагональю
# И минимального - под побочной диагональю

from def_fool import check_int_number, check_material_number


def find_max_min(A):
    max_el = float('-inf')
    min_el = float('+inf')
    N = len(A[0])
    M = len(A)
    if N != M:
        print('Данная матрица не является квадратной')
        return 0
    for i in range(N):
        for j in range(i + 1, N):
            if A[i][j] > max_el:
                max_el = A[i][j]
    for i in range(1, N):
        for j in range(N - 1, N - 1 - i, -1):
            if A[i][j] < min_el:
                min_el = A[i][j]
                
            

    print('Максимальное значение над главной диагональю: {:}'.format(max_el))
    print('Минимальное значение под побочной диагональю: {:}'.format(min_el))
    return max_el, min_el

    

N = input('Введите порядок квадратной матрицы: ')
while not check_int_number(N):
    print('Неверно введенный порядок квадратной матрицы')
    N = input('Введите порядок квадратной матрицы: ')
    
N = int(N)    
matrix = []

for i in range(N):
    matrix_str = list(map(str,\
                          input('Введите строку матрицы состоящую из {:} элементов: '.format(N)).split()))
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
            
    matrix.append(matrix_str)
find_max_min(matrix)
                      
            
