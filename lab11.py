# Кузнецов Денис ИУ7-13Б
# Программa для выполнения некоторых операций с текстом


from def_fool import check_int_number, check_material_number,\
     delete_leading_spaces


def menu():
    print('1. Выровнять текст по левому краю\n\
2. Выровнять текст по правому краю\n\
3. Выровнять текст по ширине\n\
4. Удаление заданного слова\n\
5. Замена одного слова другим во всём тексте\n\
6. Вычисление арифметических выражений для операций умножение и деление\n\
7. Предложение с максимальным количеством слов, в котором гласные \
чередуются с согласными.')


def print_text(text):
    for row in text:
        print(row)
        
def text_align_left():
    global text
    n = len(text)
    for i in range(n):
        text[i] = ' '.join(text[i].split())
        print(text[i])
        
def text_align_right():
    global text
    n = len(text)
    max_item = 0
    if n > 0:
        max_count = len(text[0])
    else:
        max_count = 0
    for i in range (1,n):
        if len(text[i]) > max_count:
            max_count = len(text[i])
            max_item = i
    for i in range (n):
        text[i] = ' '.join(text[i].split())
        text[i] = (' '*(max_count - len(text[i]))+text[i])
        print(text[i])

def text_align_width():
    global text
    n = len(text)
    max_item = 0
    if n > 0:
        max_count = len(text[0])
    else:
        max_count = 0
    for i in range (1,n):
        if len(text[i]) > max_count:
            max_count = len(text[i])
            max_item = i
    for i in range (n):
        text[i] = delete_leading_spaces(text[i])
        now = max_count - len(text[i])
        zn = text[i].count(' ')
        if zn == 0:
            print(text[i])
            continue
        remainder = now % zn
        ch = now // zn + 1
        str_now = ''
        for j in text[i].split():
            str_now += j + ' '*ch
            if remainder:
                str_now += ' '
                remainder -= 1
        str_now = delete_leading_spaces(str_now)
        text[i] = str_now
        print(str_now)
        
def delete_word(text):
    word = input('Введите слово, которое нужно удалить: ')
    length_word = len(word)
    for i in range(len(text)):
        flag = 1
        while flag:
            for j in range(len(text[i]) - length_word + 1):
                if text[i][j:j+length_word] == word:
                    if j == 0 and j + length_word == len(text[i]):
                        text[i] = text[i].replace(text[i][j:j+length_word], '', 1)
                        flag = 1
                        break
                    elif j > 0 and j + length_word == len(text[i]):
                        if text[i][j-1] == ' ':
                            text[i] = text[i].replace(text[i][j-1:j+length_word], '', 1)
                            flag = 1
                            break
                        elif text[i][j-1] == '(':
                            text[i] = text[i].replace(text[i][j:j+length_word], '', 1)
                            flag = 1
                            break
                    elif j == 0 and j + length_word < len(text[i]):
                        if text[i][j + length_word] in ' ,.;:!?)':
                            text[i] = text[i].replace(text[i][j:j+length_word+1], '', 1)
                            flag = 1
                            break
                    else:
                        if text[i][j-1] == ' ' and text[i][j+length_word] in ' ,.;:!?)':
                            text[i] = text[i].replace(text[i][j-1:j+length_word], '', 1)
                            flag = 1
                            break
                        elif text[i][j-1] == '(' and text[i][j+length_word] in ' ,.;:!?)':
                            text[i] = text[i].replace(text[i][j:j+length_word], '', 1)
                            flag = 1
                            break
            else:
                flag = 0
    
def change_word(text):
    word = input('Введите слово, которое хотите заменить: ')
    new_word = input('Введите слово, на которое нужно заменить старое: ')
    flag = 1
    length_word = len(word)
    for i in range(len(text)):
        flag = 1
        while flag:
            for j in range(len(text[i]) - length_word + 1):
                if text[i][j:j+length_word] == word:
                    if j == 0 and j + length_word == len(text[i]):
                        text[i] = text[i].replace(text[i][j:j+length_word], new_word + ' ', 1)
                        flag = 0
                        break
                    elif j > 0 and j + length_word == len(text[i]):
                        if text[i][j-1] == ' ':
                            text[i] = text[i].replace(text[i][j-1:j+length_word], ' ' + new_word, 1)
                            flag = 0
                            break
                        elif text[i][j-1] == '(':
                            text[i] = text[i].replace(text[i][j:j+length_word], ' ' + new_word, 1)
                            flag = 0
                            break
                    elif j == 0 and j + length_word < len(text[i]):
                        if text[i][j + length_word] in ' ,.;:!?)':
                            text[i] = text[i].replace(text[i][j:j+length_word+1], new_word + ' ', 1)
                            flag = 0
                            break
                    else:
                        if text[i][j-1] == ' ' and text[i][j+length_word] in ' ,.;:!?)':
                            text[i] = text[i].replace(text[i][j-1:j+length_word], ' '+new_word, 1)
                            flag = 0
                            break
                        elif text[i][j-1] == '(' and text[i][j+length_word] in ' ,.;:!?)':
                            text[i] = text[i].replace(text[i][j:j+length_word], ' '+new_word, 1)
                            flag = 0
                            break
            else:
                flag = 0


def delim(a):
    if a==' ':
        return True
    return False

def process_op(r,l,op):
    if op=='+':
        return r+l
    if op=='-':
        return l-r
    if op=='*':
        return r*l
    if op=='/':
        if r == 0:
            return "ERROR"
        return l/r
    if op=='%':
        return l%r

def priority(a):
    if a in ['+','-']:
        return 1
    if a in ['*','/','%']:
        return 2
    return -1

def calculation(s):
    st =[]
    op = []
    t = len(s)
    i = 0
    while i < t:
        if delim(s[i]):
            i += 1
            continue
        if s[i]=='(':
            op.append('(')
        elif s[i]==')':
            while op[-1]!='(':
                u = process_op(st[-1],st[-2],op[-1])
                st.pop()
                st.pop()
                st.append(u)
                op.pop()
            op.pop()
        elif s[i] in ['*','/']:
            curop=s[i]
            f=priority(curop)
            while op!=[] and priority(op[-1])>=f:
                u = process_op(st[-1],st[-2],op[-1])
                st.pop()
                st.pop()
                st.append(u)
                op.pop()
            op.append(curop)
        else:
            operand=s[i]
            while i+1<t and s[i+1] not in ['*','/','(',')',' ']:
                i+=1
                operand+=s[i]
            st.append(int(operand))
        i+=1
    while op!=[]:
        u=process_op(st[-1],st[-2],op[-1])
        st.pop()
        st.pop()
        st.append(u)
        op.pop()
    return st[-1]

def count_expression(text):
    for i in range(len(text)):
        str_now = ''
        now = ''
        for j in text[i]:
            if j in '0123456789*/ ':
                now += j
            else:
                ostatok_start = ''
                ostatok_end = ''
                while now != '' and now[-1] in ' */':
                    ostatok_end = now[-1] + ostatok_end
                    now = now[:-1]
                while now != '' and now[0] in ' */':
                    ostatok_start = now[0] + ostatok_start
                    now = now[1:]
                str_now += ostatok_start
                if now != '':
                    str_now += ' ' + str(calculation(now))
                str_now += ostatok_end + j
                now = ''
        text[i] = str_now
    
def check_vowels_consonants(word):
    flag = 1
    consonants = 'йцкнгшщзхъфвпрлджчсмтьбЙЦКНГШЩЗХЪФВПРЛДЖЧСМТЬБqwrtpsdfghjklzxcvbnmQWRTPSDFGHJKLZXCVBNM'
    vowels = 'уеыаоэяиюУЕЫАОЭЯИЮeyuioaEYUIOA'
                 
    for i in range(len(word)-1):
        if word[i] in consonants and word[i+1] in vowels\
           or word[i] in vowels and word[i+1] in consonants:
            flag = 1
        else:
            flag = 0
            break
    return flag
        

def find_max_words(text):
    temp_count = 0
    max_count = float('-inf')
    sentence_words = []
    search_sentence = ''
    temp_sentence = ''
    
    for i in range(len(text)):
        temp_string = list(map(str, text[i].split()))
        for j in range(len(temp_string)):
            sentence_words.append(temp_string[j])
            
    flag = 1
    
    for i in range(len(sentence_words)):
        temp_word = sentence_words[i]
        if temp_word[len(temp_word)-1] in '.!?':
            flag = 0
            temp_sentence += temp_word
            if check_vowels_consonants(temp_word[:len(temp_word)-1]):
                temp_count += 1
            if temp_count > max_count:
                max_count = temp_count
                search_sentence = temp_sentence
            temp_sentence = ''
            temp_count = 0

        elif temp_word[len(temp_word)-1] == ',;:':
            if check_vowels_consonants(temp_word[:len(temp_word)-1]):
                temp_count += 1
                
        else:
            if check_vowels_consonants(temp_word):
                temp_count += 1
                
        if not flag:
            flag = 1
        else:
            temp_sentence += temp_word + ' '
        
    print(search_sentence)                     
                                 
length = float('-inf') 
text = ['Я Октябрь уж Я наступил — уж роща отряхает Я',
        'Последние 2*2*2/ 5 листы. с 2 + 2 нагих своих ветвей;',
        'Дохнул осенний хлад — дорога промерзает',
        'Журча еще бежит за мельницу ручей,',
        '2      *2     *     2. Но пруд уже застыл; сосед мой поспешает',
        'В отъезжие поля. амам мама олол лол с охотою своей рор оро вав ава оло оло оло оло оло оло оло ,',
        'И страждут озими от бешеной забавы,',
        'И будит лай собак уснувшие дубравы.',
        '',
        'lksdjf']

for i in range(len(text)):
    if len(text[i]) > length:
        length = len(text[i])

menu()
x = 0
print_text(text)
while x != -1:
    x = input('Введите номер функции: ')
    while not check_int_number(x):
        x = input('Введите номер функции: ')
    x = int(x)
    if x == 1:
        text_align_left()
    elif x == 2:
        text_align_right()
    elif x == 3:
        text_align_width()
    elif x == 4:
        delete_word(text)
    elif x == 5:
        change_word(text)
    elif x == 6:
        count_expression(text)
    elif x == 7:
        find_max_words(text)
    else:
        print('Неверно введен номер функции!')
    


