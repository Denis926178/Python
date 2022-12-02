from tkinter import *
import tkinter.messagebox as box


def add_symbol():
    pass

def show_info():
    box.showinfo('Информационное окно', '''Автор программы: Кузнецов Денис ИУ7-23Б
Данная программа может складывать и вычитать числа в 3 система счисления''')

def clear_fields():
    first_number.delete(0, len(first_number.get()))
    second_number.delete(0, len(second_number.get()))

def plus():
    number_one = int(first_number.get())
    number_two = int(second_number.get())
    box.showinfo('Результат', "Сумма чисел равна: {}".format(number_one + number_two))

def minus():
    number_one = int(first_number.get())
    number_two = int(second_number.get())
    box.showinfo('Результат', "Разница чисела равна: {}".format(number_one - number_two))

root = Tk()
root.title("Сложение и вычетание в 3 СС")
menu = Menu(root)
fmenu = Menu(menu)
menu_act = Menu(menu)
menu_act.add_command(label="сложение", command=plus)
menu_act.add_command(label="вычитание", command=minus)

fmenu.add_cascade(label="действия", menu=menu_act)
fmenu.add_command(label="очистка полей", command=clear_fields)
fmenu.add_command(label="информация", command=show_info)
root.config(menu=fmenu)

first_number = Entry(fg="yellow", bg="blue", width=70)
second_number = Entry(fg="red", bg="black", width=70)

frame_figures = Frame()
btn0 = Button(master=frame_figures, text = "0", height=3, width=5, command=add_symbol)
btn1 = Button(master=frame_figures, text = "1", height=3, width=5, command=add_symbol)
btn2 = Button(master=frame_figures, text = "2", height=3, width=5, command=add_symbol)
btn_pag = Button(master=frame_figures, text = ".", height=3, width=5, command=add_symbol)
btn_symbol_minus = Button(master=frame_figures, text = "-", height=3, width=5, command=add_symbol)
btn_plus = Button(text = "сложить", command=plus)
btn_minus = Button(text = "вычесть", command=minus)

first_number.pack()
second_number.pack()
frame_figures.pack()
btn0.pack(side=LEFT)
btn1.pack(side=LEFT)
btn2.pack(side=LEFT)
btn_pag.pack(side=LEFT)
btn_plus.pack()
btn_minus.pack()

root.mainloop()
