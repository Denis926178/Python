# Кузнецов Денис ИУ7-23Б
# Данная программа может складывать и вычитать числа в 3 сс

import tkinter as tk
import tkinter.messagebox as box
import re


# Функция для сложения модулей чисел

def plus_numbers(number_one, number_two):
    number_one = str(number_one)
    number_two = str(number_two)
    whole_part_one, frac_part_one = number_one.split(".")[0], number_one.split(".")[1]
    whole_part_two, frac_part_two = number_two.split(".")[0], number_two.split(".")[1]

    if len(whole_part_one) > len(whole_part_two):
        whole_part_two = '0'*(len(whole_part_one) - len(whole_part_two)) + whole_part_two
    else:
        whole_part_one = '0'*(len(whole_part_two) - len(whole_part_one)) + whole_part_one

    if len(frac_part_one) > len(frac_part_two):
        frac_part_two += '0'*(len(frac_part_one) - len(frac_part_two))
    else:
        frac_part_one += '0'*(len(frac_part_two) - len(frac_part_one))

    whole_part_one += frac_part_one
    whole_part_two += frac_part_two
    whole_part_one = whole_part_one[::-1]
    whole_part_two = whole_part_two[::-1]

    flag = False
    whole_part = ''
    for i in range(len(whole_part_one)):
        figure_one = int(whole_part_one[i])
        figure_two = int(whole_part_two[i])
        if flag:
            figure_one += 1
            flag = False
        if figure_one + figure_two > 2:
            whole_part +=  str(figure_one + figure_two - 3)
            if i == len(whole_part_one) - 1:
                whole_part += '1'
            flag = True
        else:
            whole_part += str(figure_one + figure_two)

    number = whole_part[:len(frac_part_one)] + '.' + whole_part[len(frac_part_one):]
    number = number[::-1]
    return float(number)

# Функция, которая выводит сообщение об ошибке, в случае введения некорректных данных

def showerror():
    box.showerror('Некорректно введены данные', 'Вы ввели некорректные данные, ваш ввод содержит числа не в 3 сс\
 или ваш ввод содержит некоррентные символы')


# Функция вычислеяет модуль разности модулей чисел

def minus_numbers(number_one, number_two):
    number_one = str(number_one)
    number_two = str(number_two)
    if float(number_one) < float(number_two):
        number_one, number_two = number_two, number_one
    whole_part_one, frac_part_one = number_one.split(".")[0], number_one.split(".")[1]
    whole_part_two, frac_part_two = number_two.split(".")[0], number_two.split(".")[1]

    if len(whole_part_one) > len(whole_part_two):
        whole_part_two = '0'*(len(whole_part_one) - len(whole_part_two)) + whole_part_two
    else:
        whole_part_one = '0'*(len(whole_part_two) - len(whole_part_one)) + whole_part_one

    if len(frac_part_one) > len(frac_part_two):
        frac_part_two += '0'*(len(frac_part_one) - len(frac_part_two))
    else:
        frac_part_one += '0'*(len(frac_part_two) - len(frac_part_one))

    whole_part_one += frac_part_one
    whole_part_two += frac_part_two
    whole_part_one = whole_part_one[::-1]
    whole_part_two = whole_part_two[::-1]

    mass_whole_part_one = list(whole_part_one)
    mass_whole_part_two = list(whole_part_two)
    whole_part = ''
    for i in range(len(whole_part_one)):
        figure_one = int(mass_whole_part_one[i])
        figure_two = int(mass_whole_part_two[i])
        if figure_one < figure_two:
            mass_whole_part_one[i+1] = int(mass_whole_part_one[i+1]) - 1
            figure_one += 3
        whole_part += str(figure_one - figure_two)
    number = whole_part[:len(frac_part_one)] + '.' + whole_part[len(frac_part_one):]
    number = number[::-1]
    return float(number)


# функция, которая выводит информацию о программе

def showinfo():
    box.showinfo('Информационное окно', '''Автор программы: Кузнецов Денис ИУ7-23Б
Данная программа может складывать и вычитать числа в 3 системе счисления''')

# Функция, которая очищает поле ввода

def clear_fields():
    calc.delete(0, tk.END)

# Функции add_digit, add_operation, которые добавляют нужный символ при нажатии на кнопку

def add_digit(digit):
    value = calc.get() + str(digit)
    calc.delete(0, tk.END)
    calc.insert(0, value)

def add_operation(operation):
    value = calc.get()
    if len(value) > 0 and value[-1] in '-+.':
        value = value[:-1]
        value += str(operation)
        calc.delete(0, tk.END)
        calc.insert(0, value)
    else:
        value += str(operation)
        calc.delete(0, tk.END)
        calc.insert(0, value)

# Функция для удаления последнего символа в строке

def delete_symbol():
    value = calc.get()
    value = value[:-1]
    calc.delete(0, tk.END)
    calc.insert(0, value)

# Функция, которая считает итоговое выражение

def calculate():
    mass_number = []
    value = calc.get()
    temp = ''
    for i in range(len(value)):
        if value[i] in '012.':
            temp += value[i]
        elif temp != '':
            temp = float(temp)
            mass_number.append(temp)
            temp = ''
        elif value[i] in '+- ':
            pass
        else:
            showerror()
            return 0

    try:
        temp = float(temp)
    except:
        return 0
    mass_number.append(temp)

    mass_operations_cur = []

    if calc.get()[0] != '-':
        mass_operations_cur += ['+']
    mass_operations_cur += list(map(str, re.split("0|1|2|", calc.get())))
    mass_operations = []

    for i in range(len(mass_operations_cur)):
        if mass_operations_cur[i] =="+" or mass_operations_cur[i] == "-":
            mass_operations.append(mass_operations_cur[i])
    if len(mass_operations) < 2 or len(mass_number) < 2:
        return 0
    if len(mass_operations) != len(mass_number):
        showerror()
        return 0

    result = float(mass_number[0])
    flag = False
    if mass_operations[0] == '-':
        result = -result
    for i in range(1, len(mass_number)):
        if result <= 0 and mass_operations[i] == '-':
            result = plus_numbers(abs(result), mass_number[i])
            result = -result
        elif result <= 0 and mass_operations[i] == '+':
            if abs(result) > mass_number[i]:
                flag = True
            result = minus_numbers(abs(result), mass_number[i])
            if flag:
                result = -result
                flag = False
        elif result > 0 and mass_operations[i] == '-':
            if abs(result) < mass_number[i]:
                flag = True
            result = minus_numbers(result, mass_number[i])
            if flag:
                result = -result
                flag = False
        elif result > 0 and mass_operations[i] == '+':
            result = plus_numbers(result, mass_number[i])

        calc.delete(0, tk.END)
        calc.insert(0, result)

# Создание интерфейса

window = tk.Tk()
window.title("Сложение и вычитание 2 числе в 3 СС")
photo = tk.PhotoImage(file='img_522338.png')

menu=tk.Menu(window)
fmenu = tk.Menu(menu)
menu_act = tk.Menu(menu)

menu_act.add_command(label='Посчитать', command=calculate)
fmenu.add_cascade(label='действия', menu=menu_act)

fmenu.add_command(label='очистка ', command=lambda: calc.delete(0, tk.END))

fmenu.add_command(label='информация', command=showinfo)

window.config(menu=fmenu)

calc = tk.Entry(window, font='Arial')
btn0 = tk.Button(text="0", font='Arial', command=lambda: add_digit(0))
btn1 = tk.Button(text="1", font='Arial', command=lambda: add_digit(1))
btn2 = tk.Button(text="2", font='Arial', command=lambda: add_digit(2))
btn_m = tk.Button(text="-", font='Arial', command=lambda: add_operation('-'))
btn_pl = tk.Button(text="+", font='Arial', command=lambda: add_operation('+'))
btn_pag = tk.Button(text=".", font='Arial', command=lambda: add_operation('.'))
btn_eq = tk.Button(text='=', font="Arial", command=calculate)
btn_delete = tk.Button(image=photo, width=50, height=50, command=delete_symbol)

calc.grid(row=0, column=0, columnspan=3, rowspan=2, stick="wens")
btn0.grid(row=3, column=0, stick="wens")
btn1.grid(row=2, column=0, stick="wens")
btn2.grid(row=2, column=1, stick="wens")
btn_m.grid(row=4, column=0, stick="wens")
btn_pl.grid(row=4, column=1, stick="wens")
btn_pag.grid(row=3, column=1, stick="wens")
btn_delete.grid(row=2, column=2, rowspan=2, stick="wens")
btn_eq.grid(row=4, column=2, stick="wens") 

window.grid_columnconfigure(0, minsize=50)
window.grid_columnconfigure(1, minsize=50)
window.grid_columnconfigure(2, minsize=50)
window.grid_rowconfigure(0, minsize=50)
window.grid_rowconfigure(1, minsize=50)
window.grid_rowconfigure(2, minsize=50)
window.grid_rowconfigure(3, minsize=50)
window.grid_rowconfigure(4, minsize=50)

window.mainloop()
