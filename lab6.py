# Кузнецов Денис ИУ7-13Б
# Программa, которая позволит с использованием меню обеспечить работу с числовыми массивами
# Входные данные: номер действия в меню

# Функция для вывода меню
def menu():
    print('1. Проинициализировать список первыми N элементами заданного в л/р 5 ряда\n\
2. Очистить список и ввести его с клавиатуры\n\
3. Добавить элемент в произвольное место списка\n\
4. Удалить произвольный элемент из списка (по номеру)\n\
5. Очистить список\n\
6. Найти значение K-го экстремума в списке\n\
7. Найти наиболее длинную убывающую последовательность четных чисел\n\
8. Завершить работу программы')

# Функция для инициализации массива из N элементов, заданного в л/р 5

def function_1(N):
    mass = []
    t = 1
    x = input('Введите значение аргумента: ')
    while not check_material_number(x):
        print('Неверный формат ввода')
        x = input('Введите значение аргумента: ')
    x = float(x)
    for i in range(N):
        mass.append(t)
        t = t * (x**2) * (2*(i+1)-1)/(2*(i+1))
    for i in range(N):
        print('{:1.3g}'.format(mass[i]), end = " ")
    print()
    return(mass)

# Функция для очищения массива и ввода его с клавиатуры

def function_2(len_mass):
    mass = []
    for i in range(len_mass):
        item_mass = input('Введите элемент массива: ')
        while not(check_material_number(item_mass)):
            print('Неверный формат ввода')
            item_mass = input('Введите элемент массива: ')
        item_mass = float(item_mass)
        mass.append(item_mass)
    return mass

# Функция для добавления элемента в произвольное место списка

def function_3(mass, index, item):
    mass.insert(index, item)
    print(mass)
    return mass

# Функция для удаления произвольного элемента из списка (по номеру)

def function_4(mass, index):
    if len(mass) - 1 < index:
        print('Такого номера нет в списке')
        return mass
    mass.pop(index)
    return mass

# Функция для очистки списока

def function_5(mass):
    mass = []
    return mass

# Функция для нахождения значения K-го экстремума в списке

def function_6(mass, k):
    count = 0
    for i in range(1, len(mass)-1):
        if (mass[i] > mass[i-1] and mass[i] > mass[i+1])\
           or (mass[i] < mass[i-1] and mass[i] < mass[i+1]):
            count += 1
            if count == k:
                return mass[i]
    print('k-ого экстремума не найдено')
            
# Функция для нахождения самой длинной последовательности убывающих четных чисел

def function_7(mass):
    temp = []
    result = []
    for i in range(len(mass) - 1):
        if mass[i+1] < mass[i] and mass[i] % 2 == 0 and len(temp) == 0:
            temp.append(mass[i])
            if mass[i+1] % 2 == 0:
                temp.append(mass[i+1])
        elif mass[i+1] < mass[i] and mass[i+1] % 2 == 0 and len(temp) != 0:
            temp.append(mass[i+1])
        else:
            if len(result) < len(temp):
                result = temp
                temp = []
            else:
                temp = []
    if len(result) < len(temp):
        print(temp)
    elif len(result) == 0 and len(temp) == 0:
        print('Такой последовательности не нашлось')
    else:
        print(result)
        
    

# Функция для очистки незначащих пробелов

def delete_leading_spaces(string):
    while string[0] == " ":
        string = string.replace(" ", "", 1)
    string = string[::-1]
    while string[0] == " ":
        string = string.replace(" ", "", 1)
    string = string[::-1]
    return string

# Функция для проверки, что введено вещественное число

def delete_leading_spaces(string):
    if string == " ":
        return ""
    while string[0] == " ":
        string = string.replace(" ", "", 1)
        if string == " ":
            return ""
    string = string[::-1]
    while string[0] == " ":
        string = string.replace(" ", "", 1)
        if string == " ":
            return ""
    string = string[::-1]
    return string

def check_material_number(string):
    string = delete_leading_spaces(string)
    k = 0
    if len(string) == 0:
        return 0
    for i in range(len(string)):
        if string[i] == 'E':
            string = string.replace("E", "e", 1)
        if string[i] == ',':
            strnig = string.replace(",", ".", 1)
            
    if string.count('e') == 1:
        if string[0] == '-':
            string = string.replace("-", "", 1)
        for i in range(len(string)):
            if string[i] == 'e':
                k = i
        if k + 1 == len(string):
            return 0
        if len(string) < 3:
            return 0
        if string[0] == '.':
            return 0
        if k > 1 and string[0] == '0' and string[1] != '.':
            return 0
        if string[k+1] == '-':
            string = string.replace("-", "", 1)
        if string[k-1] == '.':
            string = string.replace(".", "", 1)
            k = k - 1
        for i in range(k):
            if string[i] not in '0123456789':
                return 0
        if len(string) - k - 1 == 0:
            return 0
        if len(string) - k - 1 > 0:
            if string[k+1] == '0':
                return 0
            if string[k-1] == '.':
                string = string.replace(".", "", 1)
            for i in range(k+1, len(string)):
                if string[i] not in '0123456789':
                    return 0
        return 1                    
    elif string.count('e') == 0:
        if string[0] == '-':
            string = string.replace("-", "", 1)
        if len(string) == 0:
            return 0
        if len(string) > 1 and string[0] == '0' and string[1] != '.':
            return 0
        if string[0] == '.':
            return 0
        for i in range(len(string)):
            if string[i] not in '0123456789.':
                return 0
        return 1
    else:
        return 0

# Функция для проверки, что введено натуральное число

def check_int_number(string):
    if check_material_number(string):
        string = float(string)
        if int(string) == string:
            return 1
        else:
            return 0
        
menu()
mass = []
x = 0
counter = 0

# Цикл для выполения операций над числовым массивом до тех пор,
# пока пользователь не завершит работу

while x != -1:
    counter += 1
    if counter % 5 == 0:
        menu()
    number = input('Выберите номер действия из меню: ')
    while not check_int_number(number):
        print('Неверный формат ввода')
        number = input('Выберите номер действия из меню: ')
    number = int(number)
    
    if number == 1:
        N = input('Введите количество чисел массива: ')
        while not check_int_number(N):
            print('Неверный формат ввода')
            N = input('Введите количество чисел массива: ')
        N = int(N)
        mass = function_1(N)
        
    elif number == 2:
        len_mass = input('Введите количество чисел в массиве: ')
        while not (check_int_number(len_mass)):
            print('Неверный формат ввода')
            len_mass = input('Введите количество числе в массиве: ')
        len_mass = int(len_mass)
        mass = function_2(len_mass)
        print(mass)
        
    elif number == 3:
        item = input('Введите число, которое надо добавить в массив: ')
        while not check_material_number(item):
            print('Неверный формат ввода')
            item = input('Введите число, которые надо добавить в массив: ')
        item = float(item)
        index = input('Введите номер ячейки, в которое надо записать данное число: ')
        while not check_int_number(index):
            print('Неверный формат ввода')
            index = input('Введите номер ячейки, в которое надо записать данное число: ')
        index = int(index)
        mass = function_3(mass, index, item)
        
    elif number == 4:
        index = input('Введите индекс элемента, который нужно удалить: ')
        while not check_int_number(index):
            print('Неверный формат ввода')
            index = input('Введите индекс элемента, который нужно удалить: ')
        index = int(index)
        mass = function_4(mass, index)
        print(mass)
        
    elif number == 5:
        mass = function_5(mass)
        print(mass)
        
    elif number == 6:
        k = input('Введите k-го значения для вычисления k-го экстремума в массиве: ')
        while not check_int_number(k):
            print('Неверный формат ввода')
            k = input('Введите k-го значения для вычисления k-го экстремума в массиве: ')
        k = int(k)
        extreme = function_6(mass, k)
        print(extreme)
        
    elif number == 7:
        sequence = function_7(mass)
        
    elif number == 8:
        x = int(input('Введите -1, чтобы заверишь работу: '))
    
    else:
        print('Неверно введенный номер функции')
