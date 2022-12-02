# Кузнецов Денис ИУ7-23Б
# Лабораторная работа №2


from tkinter import *
from tkinter import ttk
from tkinter import messagebox

from math import *
import numpy as np

import matplotlib.pyplot as plt
from sympy import symbols, diff

# Проровека, что число типа float

def isfloat(value):
    try:
        float(value)
        return True
    except ValueError:
        return False
    
# Очистка полей

def clear():
    inp = window.focus_get()
    inp.delete(0, 'end')


# Информация о программе

def info():
    messagebox.showinfo("О программе", """Данная программа позволяет вычислять корни функции на отрезке [a, b] методом хорд
    Разработчик: Кузнецов Денис ИУ7-23Б""")

def add_figure(figure):
    inp = window.focus_get()
    inp.insert(END, figure)

# grid для кнопок
def grid_button(button, row, col):
    return button.grid(row=row, column=col, stick='wens', padx=5, pady=5)


def input_check_field(input):
    if len(input) == 0:
        messagebox.showerror("Неверный ввод", "Вы заполнили не все поля ввода")
        return False

# Проверка на ввод

def input_check():

    fields = [input_function.get(),
            input_start.get(),
            input_end.get(),
            input_step.get(),
            input_eps.get(),
            input_Nmax.get()
            ]

    for i in fields:
        if not input_check_field:
            return False
    try:
        diff_func = diff(fields[0])
    except:
        messagebox.showerror("Неверный ввод", "Введенаая формула неверно записана")

    if float(fields[3]) <= 0:
        messagebox.showerror("Неверный ввод", "Введенный шаг должен быть положительным")
        return False

    if float(fields[2]) - float(fields[1]) < float(fields[3]):
        messagebox.showerror("Неверный ввод", "Указанный интервал меньше, чем шаг")
        return False
    
    if not isfloat(fields[4]) and float(fields[4]) <= 0:
        messagebox.showerror("Неверный ввод", "Введенная точность должна быть положительным числом")
        return False
    
    try:
        if int(fields[5]) <= 0:
            print("hello_1")
            messagebox.showerror("Неверный ввод", "Введенное число итераций должно быть натуральным числом")
            return False
        else:
            print("Hello_2")
            return True
    except:
        messagebox.showerror("Неверный ввод", "Введенное число итераций должно быть натуральным числом")
        return False

    return True

# Функции

def f(dif, x):
    if dif == 0:
        return eval(input_function.get())
    if dif == 1:
        return eval(str(diff(input_function.get())))
    if dif == 2:
        return eval(str(diff(diff(input_function.get()))))

# Нахождение корней

def find_solution(dif, a, b, eps, Nmax):
    code = 0
    i = 1
    try:
        x0 = a * f(dif, b) - b * f(dif, a) / (f(dif, b) - f(dif, a))
    except:
        return "NO ROOT", "-", i, code
    if f(dif, a) * f(dif, x0) < 0:
        if (f(dif, a) - f(dif, x0)) == 0:
            print("X: ", x0, " f(x): ", f(dif, x0))
            return x0, f(dif, x0), i, code
        x1 = (x0 * f(dif, a) - a * f(dif, x0)) / (f(dif, a) - f(dif, x0))
    else:
        if (f(dif, b) - f(dif, x0)) == 0:
            print("X: ", x0, " f(x): ", f(dif, x0))
            return x0, f(dif, x0), i, code
        x1 = (x0 * f(dif, b) - b * f(dif, x0)) / (f(dif, b) - f(dif, x0))
    i += 1
    if f(dif, a) * f(dif, b) < 0:
        while abs(f(dif, x0) - f(dif, x1)) > eps and (i < Nmax):
            x0 = x1
            if f(dif, a) * f(dif, x1) < 0:
                if (f(dif, a) - f(dif, x1)) == 0:
                    print("X: ", x1, " f(x): ", f(dif, x1))
                    return x0, f(dif, x0), i, code
                x1 = (x1 * f(dif, a) - a * f(dif, x1)) / (f(dif, a) - f(dif, x1))
            else:
                if (f(dif, b) - f(dif, x1)) == 0:
                    print("X: ", x1, " f(x): ", f(dif, x1))
                    return x0, f(dif, x0), i, code
                x1 = (x1 * f(dif, b) - b * f(dif, x1)) / (f(dif, b) - f(dif, x1))
            i += 1
        if i == Nmax:
            code = 1
        print("X: ", x1, " f(x): ", f(dif, x1))
        return x0, f(dif, x0), i, code
    else:
        code = 2
        return "NO ROOT", "-" , i, code

# Построение таблицы и графика

def graph_table():

    check = input_check()

    if check:
        
        i = 1
        root_num = []
        segment = []
        root = []
        mean = []
        N = []
        code = []

        graph_x = []
        graph_y = []

        function = input_function.get()
        a = float(input_start.get())
        b = float(input_end.get())
        eps = float(input_eps.get())
        Nmax = int(input_Nmax.get())
        h = float(input_step.get())

        
        while a + h <= b:
            root_num.append(i)
            temp_mass = find_solution(0, a, a+h, eps, Nmax)
            i += 1
            segment.append("[ {:}; {:} ]".format(a, a+h))
            
            root.append(temp_mass[0])
            mean.append(temp_mass[1])
            N.append(temp_mass[2])
            code.append(temp_mass[3])
            a += h

        a = float(input_start.get())
        print(root)
        print(mean)
        while a + h <= b:
            print(a)
            temp_mass_1 = find_solution(1, a, a+h, eps, Nmax)
            temp_mass_2 = find_solution(2, a, a+h, eps, Nmax)
            
            if type(temp_mass_1[0]) == float:
                graph_x.append(temp_mass_1[0])
                graph_y.append(f(0, temp_mass_1[0]))
            if type(temp_mass_2[0]) == float:
                graph_x.append(temp_mass_2[0])
                graph_y.append(f(0, temp_mass_2[0]))
            a += h
        print(graph_x)
        print(graph_y)
        window_t = Toplevel()
        window_t.title("Таблица")
        window_t.geometry("500x500")

        lst=[]
        for i in range(len(root_num)):
            lst.append((root_num[i], segment[i], root[i], mean[i], N[i], code[i]))
            
        f_top = Frame(window_t)
        f_down = Frame(window_t)
        table = ttk.Treeview(f_top, show="headings")
        heads = ["root_num", "segment", "root", "mean", "N", "code"]
        table['columns'] = heads
        table['displaycolumns'] = ["root_num", "segment", "root", "mean", "N", "code"]
        
        for header in heads:
            table.heading(header, text=header, anchor='center')
            table.column(header, anchor='center')
        for row in lst:
            table.insert('', END, values=row)

        scroll_y = ttk.Scrollbar(f_top, command=table.yview)
        scroll_x = ttk.Scrollbar(f_top, orient='horizontal', command=table.xview)
        table.configure(yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)
        f_top.pack()
        f_down.pack()
        scroll_y.pack(side='right', fill=Y)
        table.pack(side='top', fill=BOTH)
        scroll_x.pack(side='top', fill=X)

        a = float(input_start.get())
        
        x = np.linspace(a, b, 100000)
        y = []
        function = input_function.get().replace("x", "i")
        print(x)
        for i in x:
            y.append(eval(function))

        plt.plot(x,y)
        plt.plot(graph_x, graph_y, ls="", marker="o", label="points")
        plt.show()

# функция для создания кнопок

def button_symbol(symbol, row, col):
    if symbol == 'C':
        return grid_button(Button(text=symbol, command=lambda: clear()), row, col)
    elif symbol == '=':
        return grid_button(Button(text=symbol, command=lambda: graph_table()), row, col)
    
    return grid_button(Button(text=symbol, command=lambda: add_figure(symbol)), row, col)

# Интерфейс

def main():

    global window
    window = Tk()
    window.title("Лабораторная работа №2")
    window.resizable(False, False)
    window.geometry("500x500")

    global label_function
    label_function = Label(window, text="Функция:")
    global input_function
    input_function = Entry(window)

    global label_start
    label_start = Label(window, text="Начало отрезка:")
    global input_start
    input_start = Entry(window)

    global label_end
    label_end = Label(window, text="Конец отрезка:")
    global input_end
    input_end = Entry(window)

    global label_step
    label_step = Label(window, text="Шаг:")
    global input_step
    input_step = Entry(window)

    global label_eps
    label_eps = Label(window, text="Точность:")
    global input_eps
    input_eps = Entry(window)

    global label_Nmax
    label_Nmax = Label(window, text="Максимум итераций:")
    global input_Nmax
    input_Nmax = Entry(window)

    label_function.grid(row=0, column=0, stick='wens', padx=5, pady=5)
    input_function.grid(row=0, column=1, stick='wens', padx=5, pady=5)
    label_start.grid(row=1, column=0, stick='wens', padx=5, pady=5)
    input_start.grid(row=1, column=1, stick='wens', padx=5, pady=5)
    label_end.grid(row=2, column=0, stick='wens', padx=5, pady=5)
    input_end.grid(row=2, column=1, stick='wens', padx=5, pady=5)
    label_step.grid(row=3, column=0, stick='wens', padx=5, pady=5)
    input_step.grid(row=3, column=1, stick='wens', padx=5, pady=5)
    label_eps.grid(row=4, column=0, stick='wens', padx=5, pady=5)
    input_eps.grid(row=4, column=1, stick='wens', padx=5, pady=5)
    label_Nmax.grid(row=5, column=0, stick='wens', padx=5, pady=5)
    input_Nmax.grid(row=5, column=1, stick='wens', padx=5, pady=5)

    symbols=['С', '(', ')', '/', 7, 8, 9, '*', 4, 5, 6, '-', 1, 2, 3, '+', 0, 'x', '.', '=']
    
    for i in range(20):
        
        row = 6 + i // 4
        col = i % 4
        button_symbol(symbols[i], row, col)
        
    
if __name__ == "__main__":

    window = None
    label_function = None
    input_function = None
    label_start = None
    input_start = None
    label_end = None
    input_end = None
    label_step = None
    input_step = None
    label_eps = None
    input_eps = None
    label_Nmax = None
    input_Nmax = None

    main()
    
