# Кузнецов Денис ИУ7-13Б
# Программая, которая позволит с изпользованием меню обеспечить работу со строковым массивом
def menu():
    print('1. Очистить список и вввести его с клавиатуры\n\
2. Добавить элемент в произвольное место списка\n\
3. Удалить произвольный элемент из списка\n\
4. Очистить список\n\
5. Поиск элемента с наибольшим числом подряд идущих цифр\n\
6. Замена всех строчных гласных английский букв на заглавные\n\
7. Завешение работы')

def new_input_mass(mass):
    mass = []
    t = ''
    N = input('Введите количество элементов: ')
    while float(N) != int(N):
        N = input('Введите количество элементов: ')
    N = int(N)
    for i in range(N):
        t = input('Введите элемент массива: ')
        mass.append(t)
    print(mass)
    return mass

def add_item(mass, index, item):
    mass.append(mass[len(mass) - 1])
    for i in range(len(mass) - 2,index, -1):
        mass[i] = mass[i-1]
    mass[index] = item
    print(mass)
    return mass

def delete_item(mass, index):
    for i in range(index, len(mass)-1):
        mass[i] = mass[i+1]
    mass = mass[0:len(mass)-1]
    print(mass)
    return mass

def clear_mass(mass):
    mass = []
    return mass

def find_item(mass):
    temp = ''
    now_lenth = 0
    max_lenth = 0
    search_item = ''
    for i in range(len(mass)):
        temp = mass[i]
        now_lenth = 0
        for j in range(len(temp)):
            if temp[j] in '0123456789':
                now_lenth += 1
                if max_lenth < now_lenth:
                    max_lenth = now_lenth
                    search_item = mass[i]
            else:
                now_lenth = 0
    print('Элемент, в котором наибольшее количество цифр подряд: {:}'.format(search_item))
    return search_item

def change_letters(mass):
    new_letter = ''
    for i in range(len(mass)):
        temp = mass[i]
        for j in range(len(temp)-1):
            if temp[j] in 'eyuioa':
                new_letter = chr(ord(temp[j]) - 32)
                temp = temp.replace(temp[j], new_letter, 1)
                mass[i] = temp
    print(mass)
    return mass


mass = []
x = 0
menu()
counter = 0
while x != -1:
    counter += 1
    if counter % 7 == 0:
        menu()
    number = input('Введите номер функции: ')
    while float(number) != int(number):
        number = input('Введите номер функции: ')
    number = int(number)
    if number == 1:
        mass = new_input_mass(mass)
    if number == 2:
        index = input('Введите номер ячейки, в которую нужно добавить элемент: ')
        while float(index) != int(index):
            index = input('Введите номер ячейки, в которую нужно добавить элемент: ')
        index = int(index)
        item = input('Введите значение элемента, который нужно добавить: ')
        mass = add_item(mass,index,item)
    if number == 3:
        index = input('Введите номер элемента, который нужно удалить: ')
        while float(index) != int(index):
            index = input('Введите номер элемента, который нужно удалить: ')
        index = int(index)
        mass = delete_item(mass,index)
    if number == 4:
        mass = clear_mass(mass)
    if number == 5:
        find_item(mass)
    if number == 6:
        mass = change_letters(mass)
    if number == 7:
        x = int(input('Введите -1, чтобы завершить работу'))
