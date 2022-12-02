# Кузнецов Денис Евгеньевич ИУ7-13Б
# Программа для вычисления суммы бесконечного ряда с точностью до члена ряда эпсилон.

# Ввод данных
x = float(input('Задайте значение аргумента: '))
step = int(input('Задайте шаг печати: '))
epsilon = float(input('Задайте точность: '))
max_iteration = int(input('Задайте максимальное количество итераций: '))

# Проверка на корректность данных
while max_iteration <= 0:
    print('Неверное значение входных данных. Количество итераций должно быть положительным')
    max_iteration = int(input('Задайте максимальное количество итераций: '))

# Вывод заголовка таблицы
print('-'*40)
print('| № итерации |     t      |      s     |')
print('|', '-'*38, '|', sep = '')
s = 0
t = 1

# Вычисление суммы ряда
for i in range (max_iteration):
    s += t
    if i % step == 0:
        # Вывод таблицы
        print('|{:12}|{:12.3g}|{:12.3g}|'.format(i+1, t, s))
    if abs(t) <= epsilon:
        print('-'*40)
        # Вывод суммы ряда и количества итераций
        print('Сумма бесконечного ряда - {:1.3g}, вычислена за {:} итераций.'.format(s, i + 1))
        break
    # Динамическое вычисление следующего члена ряда
    t = t * (x**2) * (2*(i+1)-1) / (2*(i+1))
else:
    print('-'*40)
    print('За указанное число итераций необходимой точности достичь не удалось.')
