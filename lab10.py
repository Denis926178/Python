# Кузнецов Денис ИУ7-13Б
# Программа для вычисления приближенного значения интеграла

# Метод 1 - метод левых прямоугольников
# Метод 2 - метод Уэддля


from def_fool import check_int_number, check_material_number


def antiderivative(start, end):
    integral = f_antiderivative(end) - f_antiderivative(start)
    return integral
    
def f_antiderivative(x):
    return x**3/3

def f(x):
    return x**2

def left_rectangle(N, start, end):
    temp = start
    step = (end - start)/N
    integral = 0
    
    for i in range(N):
        integral += f(temp) * step
        temp += step
    return integral

def weddle(N, start, end):
    if N % 6 != 0:
        return '-'
    
    temp = start
    step = (end - start) / N
    integral = 0
    
    while temp < end:
        integral += 3*step/10 * (f(temp) + 5*f(temp+step) + f(temp+2*step)+\
                         6*f(temp+3*step) + f(temp+4*step)+\
                         5*f(temp+5*step) + f(temp+6*step))
        temp += step*6
    return integral

def find_N(start, end, epsilon, integral):
    
    N = 1
    step = (end - start) / N
    if integral == weddle:
        N = 6
        while abs(integral(N, start, end) - integral(2*N, start, end)) > epsilon:
            N *= 2
        print('Метод уэддля менее точный, чтобы посчитать интеграл с точностью \
{:} нужно разбить отрезок на {:} частей.'.format(epsilon, N))
    else:
        while abs(integral(N, start, end) - integral(2*N, start, end)) > epsilon:
            N *= 2
        print('Метод левых прямоугольников менее точный, чтобы посчитать интеграл с точностью \
{:} нужно разбить отрезок на {:} частей.'.format(epsilon, N))
        
# Ввод данных

start = input('Введите начало отрезка: ')
while not check_material_number(start):
    print('Неверный ввод данных')
    start = input('Введите начало отрезка: ')
    
end = input('Введите конец отрезка: ')
while not check_material_number(end):
    print('Неверный ввод данных')
    end = input('Введите конец отрезка: ')

N1 = input('Введите количество участков разбиения для численного интегрирования 1 способом: ')
while not check_int_number(N1):
    print('Неверный ввод данных')
    N1 = input('Введите количество участков разбиения для численного интегрирования 1 способом: ')

N2 = input('Введите количество участков разбиения для численного интегрирования 2 способом: ')
while not check_int_number(N2):
    print('Неверный ввод данных')
    N2 = input('Введите количество участков разбиения для численного интегрирования 2 способом: ')

epsilon = input('Введите эпсилон: ')
while not check_material_number(epsilon):
    epsilon = input('Введите эпсилон: ')

    
start = float(start)
end = float(end)
N1 = int(N1)
N2 = int(N2)
epsilon = float(epsilon)


i1 = left_rectangle(N1, start, end)
i2 = left_rectangle(N2, start, end)
i3 = weddle(N1, start, end)
i4 = weddle(N2, start, end)

# Вывод таблицы

print('-'*67)
print('|',' '*23, '|', '{:^17}'.format('N1'), '|', '{:^17}'.format('N2'), '|')
print('-'*67)
print('|','{:^23}'.format('Левые прямоугольники'), '|', '{:^17.7}'.format(i1), '|', '{:^17.7}'.format(i2), '|')
print('-'*67)
print('|', '{:^23}'.format('Уэддля'), '|', '{:^17.7}'.format(i3), '|', '{:^17.7}'.format(i4), '|')
print('-'*67)

# Вычисление погрешности

absolutely_error_i1 = abs(i1 - antiderivative(start, end))
absolutely_error_i2 = abs(i2 - antiderivative(start, end))
relative_error_i1 = absolutely_error_i1 * 100/antiderivative(start, end)
relative_error_i2 = absolutely_error_i2 * 100/antiderivative(start, end)
print('Абсолютная погрешность для метода левых прямоугольников N1: {:.7g}'.format(absolutely_error_i1))
print('Относительная погрешность для метода левых прямоугольников N1: {:.7g}%'.format(relative_error_i1))
print('Абсолютная погрешность для метода левых прямоугольников N2: {:.7g}'.format(absolutely_error_i2))
print('Относительная погрешность для метода левых прямоугольников N2: {:.7g}%'.format(relative_error_i2))

if i3 != '-':
    absolutely_error_i3 = abs(i3 - antiderivative(start, end))
    relative_error_i3 = absolutely_error_i3 * 100/antiderivative(start, end)
    print('Абсолютная погрешность для метода Уэддля N1: {:.7g}'.format(absolutely_error_i3))
    print('Относительная погрешность для метода Уэддля N1: {:.7g}%'.format(relative_error_i3))
if i4 != '-':
    absolutely_error_i4 = abs(i4 - antiderivative(start, end))
    relative_error_i4 = absolutely_error_i4 * 100/antiderivative(start, end)
    print('Абсолютная погрешность для метода Уэддля N2: {:.7g}'.format(absolutely_error_i4))
    print('Относительная погрешность для метода Уэддля N2: {:.7g}%'.format(relative_error_i4))
    
print('\n')

# Вывод минимального количества итераций

if i3 != '-':
    print('Вычисление для N1:')
    if abs(i1 - antiderivative(start, end)) > abs(i3 - antiderivative(start, end)):
        find_N(start, end, epsilon, left_rectangle)
    else:
        find_N(start, end, epsilon, weddle)
        
if i4 != '-':
    print('Вычисление для N2:')
    if abs(i2 - antiderivative(start, end)) > abs(i4 - antiderivative(start, end)):
        find_N(start, end, epsilon, left_rectangle)
    else:
        find_N(start, end, epsilon, weddle)

                         
    



