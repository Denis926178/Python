# Кузнецов Денис ИУ7-23Б
# Лабораторная работа №4

from tkinter import *
from tkinter import messagebox

array_points_k_B = []
array_points_b_B = []

array_points_x_A = []
array_points_y_A = []

# Рисование точки мышкой

def draw_yellow_point(event):
    array_points_x_A.append(event.x)
    array_points_y_A.append(event.y)
    x1, y1 = (event.x-4), (event.y-4)
    x2, y2 = (event.x+4), (event.y+4)
    canvas.create_oval(x1, y1, x2, y2, fill="yellow")

# Рисование прямой мышкой

def draw_blue_line(event):
    x1, y1 = event.x, event.y
    if canvas.old_coords:
        x2, y2 = canvas.old_coords
        canvas.create_line(x1, y1, x2, y2, fill="Blue", width=4)
        array_points_k_B.append((y2 - y1)/(x2 - x1))
        array_points_k_B.append(y1 - (y2 - y1) * x1 / (x2 - x1))
        canvas.old_coords = None
    else:
        canvas.old_coords = x1, y1

# Рисование линии через ввод

def insert_line():
    try:
        x1_1 = float(entry_blue_line_x1.get())
        y1_1 = float(entry_blue_line_y1.get())
        x2_2 = float(entry_blue_line_x2.get())
        y2_2 = float(entry_blue_line_y2.get())
        canvas.create_line(x1_1, y1_1, x2_2, y2_2, fill="Blue", width=4)
        array_points_k_B.append((y2_2 - y1_1)/ (x2_2 - x1_1))
        array_points_k_B.append(y1_1 - (y2_2 - y1_1) * x1_1 / (x2_2 - x1_1))
    except:
        pass

# Рисование точки через ввод

def insert_point():
    try:
        x1_1 = float(entry_yellow_point_x.get()) - 4
        x2_2 = float(entry_yellow_point_x.get()) + 4
        y1_1 = float(entry_yellow_point_y.get()) - 4
        y2_2 = float(entry_yellow_point_y.get()) + 4
        canvas.create_oval(x1_1, y1_1, x2_2, y2_2, fill="Yellow")
        array_points_x_A.append(float(entry_yellow_point_x.get()))
        array_points_y_A.append(float(entry_yellow_point_y.get()))
    except:
        pass

# Нахождение двух искомых точек

def find_two_points():
    max_counter = -1
    print(array_points_k_B)
    print(array_points_x_A)
    print(array_points_y_A)
    
    for i in range(len(array_points_x_A)-1):
        for j in range(i + 1, len(array_points_x_A)):
            counter = 0
            x1 = array_points_x_A[i]
            x2 = array_points_x_A[j]
            y1 = array_points_y_A[i]
            y2 = array_points_y_A[j]
            temp_k = (y2 - y1)/(x2 - x1)
            temp_b = y1 - (y2 - y1) * x1 / (x2 - x1)
            print(temp_k)
            for k in range(len(array_points_k_B)):
                if temp_k == array_points_k_B[k]:
                    counter += 1
                    
            if counter > max_counter:
                max_counter = counter
                max_x1 = x1
                max_x2 = x2
                max_y1 = y1
                max_y2 = y2
    
    if max_counter == -1:
        messagebox.showinfo("Ошибка", "Нет такой пары точек, через которую проходила бы прямая параллельная хотя бы одной из множества В")
    else:
        canvas.create_line(max_x1, max_y1, max_x2, max_y2, fill="Red", width=8)

# Интерфейс

window = Tk()
window.resizable(False, False)

left_frame = Frame()
right_frame = Frame()
bottom_frame = Frame()

label_yellow_point = Label(left_frame, text="Points A")
coordinate_yellow_point_x = Label(left_frame, text="X: ")
coordinate_yellow_point_y = Label(left_frame, text="Y: ")
entry_yellow_point_x = Entry(left_frame, width=5)
entry_yellow_point_y = Entry(left_frame, width=5)
paint_yellow_point = Button(left_frame, text="Paint yellow point", command=lambda: canvas.bind('<Button-1>', draw_yellow_point))

label_blue_line = Label(right_frame, text="Lines B")
coordinate_blue_line_x1 = Label(right_frame, text="X1: ")
coordinate_blue_line_y1 = Label(right_frame, text="Y1: ")
coordinate_blue_line_x2 = Label(right_frame, text="X2: ")
coordinate_blue_line_y2 = Label(right_frame, text="Y2: ")
entry_blue_line_x1 = Entry(right_frame, width=5)
entry_blue_line_y1 = Entry(right_frame, width=5)
entry_blue_line_x2 = Entry(right_frame, width=5)
entry_blue_line_y2 = Entry(right_frame, width=5)
paint_blue_line = Button(right_frame, text="Paint blue line", command=lambda: canvas.bind('<Button-1>', draw_blue_line))

canvas = Canvas(bottom_frame, width = 1000, height = 500, background="white")
canvas.old_coords = None
canvas.bind('<Button-1>', draw_blue_line)
find_points = Button(bottom_frame, text="Find points", command=find_two_points)
insert_point = Button(bottom_frame, text="insert_point", command=insert_point)
insert_line = Button(bottom_frame, text="insrt_line", command=insert_line)

label_yellow_point.grid(row=0, column=0)
coordinate_yellow_point_x.grid(row=1, column=0)
coordinate_yellow_point_y.grid(row=2, column=0)
entry_yellow_point_x.grid(row=1, column=1)
entry_yellow_point_y.grid(row=2, column=1)
paint_yellow_point.grid(row=3, column=0)
left_frame.pack(side=LEFT)

label_yellow_point.grid(row=0, column=0)
coordinate_blue_line_x1.grid(row=1, column=0)
coordinate_blue_line_y1.grid(row=2, column=0)
coordinate_blue_line_x2.grid(row=3, column=0)
coordinate_blue_line_y2.grid(row=4, column=0)
entry_blue_line_x1.grid(row=1, column=1)
entry_blue_line_y1.grid(row=2, column=1)
entry_blue_line_x2.grid(row=3, column=1)
entry_blue_line_y2.grid(row=4, column=1)
paint_blue_line.grid(row=5, column=0)
right_frame.pack(side=RIGHT)

canvas.grid(row=0, column=0)
find_points.grid(row=1, column=0)
insert_point.grid(row=2, column=0)
insert_line.grid(row=3, column=0)

bottom_frame.pack()

window.mainloop()







