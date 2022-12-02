# Кузнецов Денис ИУ7-13Б
# Программа, которая позволит с использованием меню обеспечить работу с целочисленными матрицами
# Входные данные: номер функции

# Функция, которая выводит меню на экран

def menu():
    print('1. Ввести матрицу\n\
2. Добавить строку\n\
3. Удалить строку\n\
4. Добавить столбец\n\
5. Удалить столбец\n\
6. Найти строку, имеющую наибольшее количество чётных элементов\n\
7. Переставить местами строки с наибольшим и наименьшим количеством отрицательных элементов\n\
8. Найти столбец, имеющий наибольшее количество простых чисел\n\
9. Переставить местами столбцы с максимальной и минимальной суммой элементов\n\
10. Вывести текущую матрицу\n\
11. Завершеить работу')

# Функция для проверки на целое число

def simple_number(number):
    if number < 2:
        return 0
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return 0
    return 1

# Функция для ввода матрицы

def input_matrix():
    global row
    global col
    row = int(input('Введите количество строк в матрице: '))
    col = int(input('Введите количество столбцов в матрице: '))
    matrix = []
    for i in range(row):
        string = list(map(int, input('Введите {:} строку матрицы из {:} элементов: '.format(i+1, col)).split()))
        while len(string) != col:
            print('Неверный ввод строки матрицы')
            string = list(map(int, input('Введите {:} строку матрицы из {:} элементов: '.format(i+1, col)).split()))
        matrix.append(string)
    return matrix

# Функция для добавления строки в матрицу (алгоритмически)

def add_row_algorithm(matrix):
    index = int(input('Введите индекс строки в которую вы хотите добавить новую строку: '))
    while index > row:
        print('Неверно введенный индекс строки')
        index = int(input('Введите индекс строки в которую вы хотите добавить новую строку: '))
    string = list(map(int, input('Введите новую строку: ').split()))
    while len(string) != col:
        print('Неверный ввод строки матрицы')
        string = list(map(int, input('Введите новую строку: ').split()))
    matrix.append(matrix[len(matrix) - 1])
    for i in range(len(matrix) - 2,index, -1):
        matrix[i] = matrix[i-1]
    matrix[index] = string
    return matrix

# Функция для добавления строки в матрицу с использованием insert

def add_row(matrix):
    index = int(input('Введите индекс строки в которую вы хотите добавить новую строку: '))
    while index > row:
        print('Неверно введенный индекс строки')
        index = int(input('Введите индекс строки в которую вы хотите добавить новую строку: '))
    string = list(map(int, input('Введите новую строку: ').split()))
    while len(string) != col:
        print('Неверный ввод строки матрицы')
        string = list(map(int, input('Введите новую строку: ').split()))
    matrix.insert(index, string)
    return matrix

# Функция для удаления строки (алгоритмически)

def delete_row_algorithm(matrix):
    index = int(input('Введите индекс строки, которую вы хотите удалить: '))
    while index + 1 > row:
        print('Неверно введенный индекс строки')
        index = int(input('Введите индекс строки, которую вы хотите удалить: '))
    for i in range(index, len(matrix)-1):
        matrix[i] = matrix[i+1]
    matrix = matrix[0:len(matrix)-1]
    return matrix

# Функция для удаления строки с использованием pop

def delete_row(matrix):
    index = int(input('Введите индекс строки, которую вы хотите удалить: '))
    while index + 1 > row:
        print('Неверно введенный индекс строки')
        index = int(input('Введите индекс строки, которую вы хотите удалить: '))
    matrix.pop(index)
    return matrix

# Функция для добавления столбца (алгоритмически)

def add_col_algorithm(matrix):
    index = int(input('Введите индекс столбца, на который вы хотите добавить новый столбец: '))
    while index > col:
        print('Неверно введенный индекс столбца')
        index = int(input('Введите индекс столбца, на который вы хотите добавить новый столбец: '))
    for i in range(row):
        item = int(input('Введите элемент, который будет вставлен в {:} столбец, в {:} строчку: '.format(index + 1, i + 1)))
        matrix[i].append(matrix[i][col - 1])
        for j in range(col - 2, index, -1):
            matrix[i][j] = matrix[i][j-1]
        matrix[i][index] = item
    return matrix

# Функция для добавления столбца с использованием insert

def add_col(matrix):
    index = int(input('Введите индекс столбца, на который вы хотите добавить новый столбец: '))
    while index  > col:
        print('Неверно введенный индекс столбца')
        index = int(input('Введите индекс столбца, на который вы хотите добавить новый столбец: '))
    for i in range(row):
        item = int(input('Введите элемент, который будет вставлен в {:} столбец, в {:} строчку: '.format(index + 1, i + 1)))
        matrix[i].insert(index, item)
    return matrix

# Функция для удаления столбца (алгоритмически)

def delete_col_algorithm(matrix):
    index = int(input('Введите индекс столбца, который вы хотите удалить: '))
    while index + 1 > col:
        print('Неверно введенный индекс столбца')
        index = int(input('Введите индекс столбца, который вы хотите удалить: '))
    for i in range(row):
        for j in range(index, col - 1):
            matrix[i][j] = matrix[i][j+1]
        matrix[i] = matrix[i][0:col - 1]
    return matrix

# Функция для удаления столбца с использованием pop

def delete_col(matrix):
    index = int(input('Введите индекс столбца, который вы хотите удалить: '))
    while index + 1 > col:
        print('Неверно введенный индекс столбца')
        index = int(input('Введите индекс столбца, который вы хотите удалить: '))
    for i in range(row):
        matrix[i].pop(index)
    return matrix

# Функция для нахождения ряда с наибольшим количестовом четных элементов

def find_row(matrix):
    max_even_items = 0
    number_string = 0
    for i in range(row):
        count_even_items = 0
        for j in range(col):
            if matrix[i][j] % 2 == 0:
                count_even_items += 1
                if count_even_items > max_even_items:
                    max_even_items = count_even_items
                    number_string = i
    print(matrix[number_string])
    return matrix

# Функция для нахождения столбца с наибольшим количеством простых чисел

def find_col(martix):
    number_col = 0
    max_count_simple_number = 0
    for i in range(col):
        count_simple_number = 0
        for j in range(row):
            if simple_number(matrix[j][i]):
                count_simple_number += 1
                if max_count_simple_number < count_simple_number:
                    max_count_simple_number = count_simple_number
                    number_col = i
    print(number_col)
    for i in range(row):
        print(matrix[i][number_col], end = " ")
    return matrix

# Функция для перестановки ряда с наибольшим и наименьшим количеством отрицательных элементов

def change_min_row_max_row(matrix):
        min_negative_count = 1000
        index_min_negative_count = 0
        max_negative_count = 0
        index_max_negative_count = 0
        negative_count = 0
        for i in range(row):
            for j in range(col):
                if matrix[i][j] < 0:
                    negative_count += 1
            if min_negative_count > negative_count:
                min_negative_count = negative_count
                index_min_negative_count = i
            if max_negative_count < negative_count:
                max_negative_count = negative_count
                index_max_negative_count = i
        matrix[index_max_negative_count], matrix[index_min_negative_count]\
                                          = matrix[index_min_negative_count], matrix[index_max_negative_count]
        return matrix
    
# Функция для перестановки столбцов с наибольшей и наименьшей суммой

def change_min_col_max_col(matrix):
    max_sum = float('-inf')
    min_sum = float('inf')
    index_max_sum = 0
    index_min_sum = 0
    for i in range(col):
        summa = 0
        for j in range(row):
            summa += matrix[j][i]
        if summa > max_sum:
            max_sum = summa
            index_max_sum = i
        if summa < min_sum:
            min_sum = summa
            index_min_sum = i
    for i in range(row):
        matrix[i][index_max_sum], matrix[i][index_min_sum]\
                                  = matrix[i][index_min_sum], matrix[i][index_max_sum]
    return matrix
menu()
matrix = []

x = -1

# Цикл для выполения операций над матрицей до тех пор, пока пользователь не завершит работу

while x != 0:
    number_fuction = int(input('Введите номер функции: '))
    if number_fuction == 1:
        matrix = input_matrix()
    if number_fuction == 2:
        print('Можно посчитать двумя способами: \n\t\
1. Алгоритмически\n\t\
2. Используя встроенные функции языка Python')
        option_function = int(input('Введите номер способа, которым вы хотите посчитать: '))
        if option_function == 1:
            matrix = add_row_algorithm(matrix)
        elif option_function == 2:
            matrix = add_row(matrix)
        row += 1
    if number_fuction == 3:
        print('Можно посчитать двумя способами: \n\t\
1. Алгоритмически\n\t\
2. Используя встроенные функции языка Python')
        option_function = int(input('Введите номер способа, которым вы хотите посчитать: '))
        if option_function == 1:
            matrix = delete_row_algorithm(matrix)
        elif option_function == 2:
            matrix = delete_row(matrix)
        row -= 1
    if number_fuction == 4:
        print('Можно посчитать двумя способами: \n\t\
1. Алгоритмически\n\t\
2. Используя встроенные функции языка Python')
        option_function = int(input('Введите номер способа, которым вы хотите посчитать: '))
        if option_function == 1:
            matrix = add_col_algorithm(matrix)
        elif option_function == 2:
            matrix = add_col(matrix)
        col += 1
    if number_fuction == 5:
        print('Можно посчитать двумя способами: \n\t\
1. Алгоритмически\n\t\
2. Используя встроенные функции языка Python')
        option_function = int(input('Введите номер способа, которым вы хотите посчитать: '))
        if option_function == 1:
            matrix = delete_col_algorithm(matrix)
        elif option_function == 2:
            matrix = delete_col_algorithm(matrix)
        col -= 1
    if number_fuction == 6:
        matrix = find_row(matrix)
    if number_fuction == 7:
        matrix = change_min_row_max_row(matrix)
    if number_fuction == 8:
        matrix = find_col(matrix)
    if number_fuction == 9:
        matrix = change_min_col_max_col(matrix)
    if number_fuction == 10:
        print('\n')
        for i in range(row):
            for j in range(col):
                print('{:7}'.format(matrix[i][j]), end="")
            print('\n')
    if number_fuction == 11:
        x = int(input('Введите 0, чтобы завершить работу: '))
    


    

