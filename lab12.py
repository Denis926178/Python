from random import randint
from def_fool import check_int_number
    
NAMES = ['Артем', 'Александр', 'Михаил', 'Максим',
         'Иван', 'Роман', 'Дмитрий', 'Сергей', 'Андрей',
         'Алексей', 'Артур', 'Илья','Константин', 'Кирилл',
         'Никита', 'Матвей', 'Егор', 'Арсений'
         ]

SURNAMES = ['Иванов', 'Смирнов', 'Кузнецов', 'Попов',
            'Васильев', 'Петров', 'Соколов', 'Михайлов',
            'Новиков', 'Федоров', 'Морозов', 'Волков',
            'Алексеев', 'Лебедев', 'Семенов'
            ]

FILE = None

#Менюшка

def menu():
    print("""1. Выбрать файл для работы
2. Инициализировать базу данных
3. Вывести содержимое базы данных
4. Добавить запись в базу данных
5. Поиск по одному полю
6. Поиск по двум полям""")

# Рандомно генерит базу данных из списков выше (чтобы долго не вводить много ячеек)

def generator_database(N):
    global FILE
    with open(FILE, 'w') as f:
        for i in range(N):
            string = ''
            string += NAMES[randint(0,len(NAMES))-1] + '|'
            string += SURNAMES[randint(0,len(SURNAMES))-1] + '|'
            string += str(randint(0,100)) + '\n'
            f.write(string)

# Функция для выбора файла (Если файла нет - создаст его,
# если некоректное имя - выведет ошибку)

def choose_file():
    try:
        file = input('Введите полный путь до файла: ')
        if file[-4:] != '.txt':
            print('Некорректное имя файла')
            return None
        with open(file, 'a+') as f:
            f.readline()
            f.write('')
            return file
    except OSError as e:
        if type(e) == PermissionError:
            print('Не хватает прав доступа к файлу')
        else:
            print('Некорректное имя файла!')
        return None

def check_open_file(file):
    try:
        with open(FILE, 'r') as f:
            return 1
    except:
        return 0

# Проверка, что в третьем столбце целое число от 0 до 100

def check_result(result):
    while True:
        try:
            while float(result) != int(result) or int(result) > 100 or int(result) < 0:
                print('Вы вввели неверный результат, число не может быть больше 100, или меньше 0, или быть не целым')
                result = input('Введите количество баллов: ').strip()
            else:
                return result
        except:
            print('Вы ввели не число')
            result = input('Введите количество баллов: ').strip()
            
# Инициализация базы данных

def initialization_database():
    print('Данные хранятся в формате: имя, фамилия, количество баллов за экзамен (по 100 балльной шкале)')
    N = input('Введите количество записей, которые надо инициализировать: ')
    while not check_int_number(N):
        N = input('Введите количество записей, которые надо инициализировать: ')
    N = int(N)
    try:
        global FILE
        FILE = input('Введите полный путь до файла: ')
        with open(FILE, 'w') as f:
            for i in range(N):
                name = input('Введите имя: ').strip()
                while name.count('|') > 0:
                    print('Неверно введено имя!')
                    name = input('Введите имя: ').strip()
                surname = input('Введите фамилию: ').strip()
                while surname.count('|') > 0:
                    print('Неверно введена фамилия!')
                    surname = input('Введите фамилию: ').strip()
                result = input('Введите количество баллов: ').strip()
                check_result(result)
                string = name + '|' + surname + '|' + result + '\n'
                try:
                    f.write(string)
                except UnicodeError:
                    print('Неверная кодировка!')
                    return 0
    except OSError:
        print('Введен неверный путь до файла!')
            
# Вывод базы данных

def print_database():
    global FILE
    if FILE is not None and check_open_file(FILE):
        with open(FILE, 'r') as f:
            try:
                string = f.readline().strip()
            except UnicodeError:
                print('Неверная кодировка файла!')
                return 0
            while len(string.strip()) > 0:
                if string.count('|') == 2:
                    name, surname, result = map(str, string.split('|'))
                    print('{:20}{:20}{:5}'.format(name, surname, result))
                try:
                    string = f.readline().strip()
                except UnicodeError:
                    print('Неверная кодировка файла!')
                    return 0
    else:
        print('Вы не выбрали файл, введите 1, чтобы выбрать файл')
        
# Добавление записи в базу данных

def add_record_database():
    global FILE
    if FILE is not None and check_open_file(FILE):
        with open(FILE, 'w+') as f:
            name = input('Введите имя: ').strip()
            while name.count('|') > 0:
                print('Неверно введено имя!')
                name = input('Введите имя: ').strip()
            surname = input('Введите фамилию: ').strip()
            while surname.count('|') > 0:
                print('Неверно введена фамилия')
                surname = input('Введите фамилию: ').strip()
            result = input('Введите количество баллов: ').strip()
            result = check_result(result)
            record = name.strip() + '|' + surname.strip() + '|' + result.strip()
            f.write(record)
    else:
        print('Вы не выбрали файл, введите 1, чтобы выбрать файл')

# Поиск по одному полю (по имени)

def search_one_field():
    global FILE
    if FILE is not None and check_open_file(FILE):
        with open(FILE, 'r') as f:
            search = input('Введите имя: ').strip()
            try:
                string = f.readline().strip()
            except UnicodeError:
                print('Неверная кодировка')
                return 0
            count = False
            while string != '':
                if string.count('|') != 2:
                    continue
                name, surname, result = map(str, string.split('|'))
                if search == name:
                    print('{:20}{:20}{:5}'.format(name, surname, result))
                    count = True
                try:
                    string = f.readline().strip()
                except UnicodeError:
                    print('Неверная кодировка')
                    return 0
            if not count:
                print('Записей с таким полем не нашлось')
    else:
        print('Вы не выбрали файл, введите 1, чтобы выбрать файл')

# Поиск по двум полям (по фамилии и баллам)

def search_two_fields():
    global FILE
    if FILE is not None and check_open_file(FILE):
        with open(FILE, 'r') as f:
            search_1 = input('Введите фамилию: ').strip()
            search_2 = input('Введите количество баллов: ').strip()
            while search_1 == search_2:
                search_2 = input('Поля для поиска совпадают, введите заново второе поле для поиска: ').strip()
            try:
                string = f.readline().strip()
            except UnicodeError:
                print('Неверная кодировка')
                return 0
            count = False
            while string != '':
                if string.count('|') != 2:
                    continue
                name, surname, result = map(str, string.split('|'))
                if surname == search_1 and result == search_2:
                    print('{:20}{:20}{:5}'.format(name, surname, result))
                    count = True
                try:
                    string = f.readline().strip()
                except UnicodeError:
                    print('Неверная кодировка')
                    return 0
            if not count:
                print('Записей с такими полями не нашлось')
    else:
        print('Вы не выбрали файл, введите 1, чтобы выбрать файл')

choice = None
menu()

while choice != -1:
    choice = input('Введите номер функции: ')
    while not check_int_number(choice):
        choice = input('Введите номер функции: ')
    choice = int(choice)
    
    if choice == 1:
        FILE = choose_file()
    elif choice == 2:
        initialization_database()        
    elif choice == 3:
        print_database()       
    elif choice == 4:
        add_record_database()        
    elif choice == 5:
        search_one_field()        
    elif choice == 6:
        search_two_fields()        
    else:
        print('Неверно введен номер функции!')
        
        
