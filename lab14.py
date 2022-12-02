# Кузнецов Денис ИУ7-13Б
# Лабораторная 14


from time import time
from random import randint


# Пирамидальная сортировка

def heapify(arr, n, i):
    largest = i 
    l = 2 * i + 1   
    r = 2 * i + 2
    if l < n and arr[i] < arr[l]:
        largest = l
    if r < n and arr[largest] < arr[r]:
        largest = r
    if largest != i:
        arr[i],arr[largest] = arr[largest],arr[i]
        heapify(arr, n, largest)
        
def heapsort(arr):
    n = len(arr)
    for i in range(n, -1, -1):
        heapify(arr, n, i)
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i] 
        heapify(arr, i, 0)
    

array_user = [randint(1, 1000) for i in range(20)]
print('Список до сортировки: ', *array_user)
heapsort(array_user)
print('Список после сортировки: ', *array_user)

N1 = input('Введите первую размерность: ')
while not N1.isdigit():
    print('Некорректный ввод!')
    N1 = input('Введите первую размерность: ')

N2 = input('Введите вторую размерность: ')
while not N2.isdigit():
    print('Некорректный ввод!')
    N2 = input('Введите вторую размерность: ')

N3 = input('Введите первую размерность: ')
while not N3.isdigit():
    print('Некорректный ввод!')
    N3 = input('Введите вторую размерность: ')

N1 = int(N1)
N2 = int(N2)
N3 = int(N3)

array_random_1 = [randint(1, N1) for i in range(N1)]
array_random_2 = [randint(1, N2) for i in range(N2)]
array_random_3 = [randint(1, N3) for i in range(N3)]

array_sort_1 = [i for i in range(1, N1 + 1)]
array_sort_2 = [i for i in range(1, N2 + 1)]
array_sort_3 = [i for i in range(1, N3 + 1)]

reverse_array_sort_1 = [i for i in range(N1, 0, -1)]
reverse_array_sort_2 = [i for i in range(N2, 0, -1)]
reverse_array_sort_3 = [i for i in range(N3, 0, -1)]

arrays = []
arrays.append(array_sort_1)
arrays.append(array_sort_2)
arrays.append(array_sort_3)
arrays.append(array_random_1)
arrays.append(array_random_2)
arrays.append(array_random_3)
arrays.append(reverse_array_sort_1)
arrays.append(reverse_array_sort_2)
arrays.append(reverse_array_sort_3)

times = []
for i in range(9):
    t_start = time()
    array = heapsort(arrays[i])
    t_end = time()
    delta_time = t_end - t_start
    times.append(delta_time)

print('-'*111)
print('|',' '*38, '|', '{:^20}'.format(N1), '|', '{:^20}'.format(N2),  '|',\
      '{:^20}'.format(N3), '|')
print('-'*111)
print('| Упорядоченный список',' '*17, '|', '{:^20.10f}'.format(times[0]), '|',\
      '{:^20.10f}'.format(times[1]), '|', '{:^20.10f}'.format(times[2]), '|')
print('-'*111)
print('| Отсортированный список',' '*15, '|', '{:^20.10f}'.format(times[3]), '|'\
      , '{:^20.10f}'.format(times[4]), '|', '{:^20.10f}'.format(times[5]), '|')
print('-'*111)
print('| Упорядоченный в обратном порядке',' '*5, '|', '{:^20.10f}'.format(times[6]), '|',\
      '{:^20.10f}'.format(times[7]), '|', '{:^20.10f}'.format(times[8]), '|')
print('-'*111)
    

