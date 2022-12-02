# Кузнецов Денис ИУ7-13Б
# Программа для определения среднего арифметического положительных чисел
# каждой строки матрицы и количества элементов, меньших среднего арифметического

from math import sin
from def_fool import check_int_number, check_material_number

def create_matrix():
    D = list(map(str, input('Введите массив D: ').split()))
    for i in range(len(D)):
        while not check_material_number(D[i]):
            print('Неверно массив, все элементы должны быть числами')
            D[i] = input('Введите заново {:} элемент массива: '.format(i+1))
        else:
            D[i] = float(D[i])
            
    F = list(map(str, input('Введите массив F: ').split()))
    for i in range(len(F)):
        while not check_material_number(F[i]):
            print('Неверно введенный массив, все элементы должны быть числами')
            F[i] = input('Введите заново {:} элемент массива: '.format(i+1))
        else:
            F[i] = float(F[i])
    A = []
    AV = []
    L = []
    
    for i in range(len(D)):
        matrix_str = []
        sum_str = 0
        counter_pos = 0
        counter_less = 0
        for j in range(len(F)):
            matrix_el = sin(D[i] + F[j])
            if matrix_el > 0:
                sum_str += matrix_el
                counter_pos += 1
            matrix_str.append(matrix_el)
        if counter_pos != 0:
            arithmetic_mean = sum_str/counter_pos
        else:
            arithmetic_mean = 0
        AV.append(arithmetic_mean)
        A.append(matrix_str)
        
        for j in range(len(matrix_str)):
            if matrix_str[j] < arithmetic_mean:
                counter_less += 1
        L.append(counter_less)
    for i in range(len(D)):
        for j in range(len(F)):
            print('{:6.2f}'.format(A[i][j]), end="")
        print('\t{:6.2f}\t{:6.2f}'.format(AV[i], L[i]))
    return A
create_matrix()
