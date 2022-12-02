# Кузнецов Денис ИУ7-13Б
# Лабораторная работа 13

import struct as s

# Вывод меню

def menu():
    print("""1. Выбрать файл для работы
2. Инициализировать базу данных
3. Вывести содержимое базы данных
4. Добавить запись в базу данных
5. Удалить запись из базы данных (по номеру в файле)
6. Поиск по одному полю (по имени)
7. Поиск по двум полям (по фамилии и количеству балллов)""")
    
# Удаление символов с кодом 0

def delete_zero_el(string):
    el = ''
    for i in string:
        if ord(i) == 0:
            break
        el += i
    return el

# Проверка на открытие файла

def check_open_file(FILE):
    try:
        with open(FILE, 'ab+'):
            return 1
    except:
        return 0

# Функция выбора файла

def choose_file():
    global FIlE    
    try:
        FILE = input('Введите путь до файла: ')
        if FILE[-4:] != '.bin':
            print('Некорректное имя файла, можно работать только с бинарными файлами')
            return None
        with open(FILE, 'ab+') as f:
            string = f.read()
            f.write(b'')
            return FILE
    except OSError as e:
        if type(e) == PermissionError:
            print('Ошибка прав доступа!')
        else:
            print('Некорректное имя файла')
        return None

# Проверка на корректность ввода для третьего столбца (хранение количества баллов за экзамен)

def check_result(result):
    while True:
        try:
            while float(result) != int(result) or int(result) > 100 or int(result) < 0:
                print('Вы ввели неверые данные, результат не может быть не целым числом или быть больше 100 или меньше 0')
                result = input('Введите количество баллов: ')
            else:
                return result
        except:
            print('Вы ввели не число')
            result = input('Введите количество баллов: ')

# Инициализация базы данных

def initialization_database():
    global FILE, old_records
    FILE = input('Введите полный путь до файла: ')
    print("""Данные хранятся в бинарной кодировке:
имя, фамилия, количество баллов за экзамен (по 100 балльной шкале)""")
    N = input('Введите количество записей, которые надо инициализировать: ')
    while not N.isdigit():
        N = input('Введите количество записей, которые надо инициализировать: ')
    N = int(N)
    with open(FILE, 'wb') as f:
        if check_open_file(FILE):
            for i in range(N):
                name = input('Введите имя: ').strip()
                surname = input('Введите фамилию: ').strip()
                result = input('Введите количество баллов: ').strip()
                result = check_result(result)
                string = s.pack('<20s20s20s', name.encode(), surname.encode(), result.encode())
                f.write(string)
        else:
            print('Ошибка открытия файла!')

# Вывод базы данных

def print_database():
    global FILE
    if FILE is not None:
        if check_open_file(FILE):
            with open(FILE, 'rb') as f:
                pack_line = f.read(60)
                if len(pack_line) != 60:
                    print('Ошибка распаковки файла!')
                    return 0
                counter = 1
                while pack_line:
                    try:
                        temp_line = list(s.unpack('20s20s20s', pack_line))
                    except:
                        print('Ошибка распаковки файла!')
                        break
                    name = delete_zero_el(temp_line[0].decode())
                    surname = delete_zero_el(temp_line[1].decode())
                    result = delete_zero_el(temp_line[2].decode())
                    print('{:5}) {:20}{:20}{:20}'.format(counter, name, surname, result))
                    pack_line = f.read(60)
                    counter += 1
        else:
            print('Ошибка открытия файла!')
    else:
        print('Файл не выбран, нажмите 1, чтобы выбрать файл!')

# Добавление записи в БД

def add_record():
    global FILE, old_records
    if FILE is not None:
        if check_open_file(FILE):
            with open(FILE, 'ab+') as f:
                name = input('Введите имя: ').strip()
                surname = input('Введите фамилию: ').strip()
                result = input('Введите количество баллов: ').strip()
                result = check_result(result)
                string = s.pack('<20s20s20s', name.encode(), surname.encode(), result.encode())
                f.write(string)
        else:
            print('Ошибка откртия файла!')
    else:
        print('Файл не выбран, нажмите 1, чтобы выбрать файл!')

# Удаление записи из БД

def delete_record():
    global FILE
    if FILE is not None:
        if check_open_file(FILE):
            number = input('Введите номер записи, который нужно удалить: ')
            while not number.isdigit():
                number = input('Введите номер записи, который нужно удалить: ')
            number = int(number)
            with open(FILE, 'rb+') as f:
                flag = False
                pack_line = f.read(60)
                try:
                    f.seek(60*(number-1))
                    pack_line = f.read(60)
                    while pack_line:
                        pack_line = f.read(60)
                        f.seek(-120,1)
                        f.write(pack_line)
                        f.seek(60, 1)
                        pack_line
                    f.truncate()
                except:
                    print('Корректно введен номер строки, которую нужно удалить!')
        else:
            print('Ошибка открытия файла!')
    else:
        print('Файл не выбран, нажмите 1, чтобы выбрать файл!')

# Поиск по одному полю (по имени)

def search_one_field():
    global FILE
    if FILE is not None:
        if check_open_file(FILE):
            with open(FILE, 'rb') as f:
                search = s.pack('20s', input('Введите имя: ').encode())
                pack_line = f.read(60)
                if len(pack_line) != 60:
                    print('Ошибка распаковки файла!')
                    return 0
                while pack_line:
                    if pack_line[0:20] == search:
                        try:
                            pack_line = list(s.unpack('20s20s20s', pack_line))
                        except:
                            print('Ошибка распаковки файла!')
                            break
                        name = delete_zero_el(pack_line[0].decode())
                        surname = delete_zero_el(pack_line[1].decode())
                        result = delete_zero_el(pack_line[2].decode())
                        print('{:20}{:20}{:20}'.format(name, surname, result))
                    pack_line = f.read(60)
        else:
            print('Ошибка открытия файла!')
                
    else:
        print('Файл не выбран, нажмите 1, чтобы выбрать файл!')

# Поиск по двум полям (по фамилии и количеству баллов)

def search_two_fields():
    global FILE
    if FILE is not None:
        if check_open_file(FILE):
            with open(FILE, 'rb') as f:
                search_1 = s.pack('20s', input('Введите фамилию: ').encode())
                search_2 = s.pack('20s', input('Введите количество баллов: ').encode())
                pack_line = f.read(60)
                if len(pack_line) != 60:
                    print('Ошибка распаковки файла')
                    return 0
                while pack_line:
                    if pack_line[20:40] == search_1 and pack_line[40:60] == search_2:
                        try:
                            pack_line = list(s.unpack('20s20s20s', pack_line))
                        except:
                            print('Ошибка распаковки файла!')
                            break
                        name = delete_zero_el(pack_line[0].decode())
                        surname = delete_zero_el(pack_line[1].decode())
                        result = delete_zero_el(pack_line[2].decode())
                        print('{:20}{:20}{:20}'.format(name, surname, result))
                    pack_line = f.read(60)
        else:
            print('Ошибка открытия файла!')
    else:
        print('Файл не выбран, нажмите 1, чтобы выбрать файл!')

choice = None
FILE = None
old_records = 0
x = 0
menu()

while True:
    choice = input('Введите номер функции: ')
    if choice == '1':
        FILE = choose_file()
    elif choice == '2':
        initialization_database()
    elif choice == '3':
        print_database()
    elif choice == '4':
        add_record()
    elif choice == '5':
        delete_record()
    elif choice == '6':
        search_one_field()
    elif choice == '7':
        search_two_fields()
    else:
        print('Неверно введен номер функции!')
            
