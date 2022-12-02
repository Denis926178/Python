# Кузнецов Денис ИУ7-13Б
# Программа для замены все гласных букв на точки

from def_fool import check_int_number


def change_vowels_pag(A):
    N = len(A)
    M = len(A[0])
    for i in range(N):
        for j in range(M):
            string = A[i][j]
            for k in range(len(string)):
                if string[k] in 'EYUIOAeyuioa':
                    string = string.replace(string[k], '.', 1)
            A[i][j] = string
    for i in range(N):
        for j in range(M):
            print('{:^10}'.format(A[i][j]), end="")
        print('\n')

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
    matrix_str = list(map(str, input('Введите строку матрицы\
состояющую из {:} элементов: '.format(M)).split()))
    while len(matrix_str) != M:
        print('Неверно введенная строка матрицы')
        matrix_str = list(map(str, input('Введите строку матрицы\
состояющую из {:} элементов: '.format(M)).split()))
        
    matrix.append(matrix_str)
change_vowels_pag(matrix)
