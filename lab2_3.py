# Кузнецов Денис ИУ7-23Б
# Лабораторная работа №3

from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfilename

from PIL import Image
import numpy as np

# открытие проводника

def open_img():
    path = askopenfilename()
    try:
        img = Image.open(path, 'r')
        return img, path
    except:
        messagebox.showerror("Неверный выбор", "Вы выбрали неверную картинку")

# шифрование картинки

def cryp_text(text, img, path, isimg):
    pixel_array = np.array(img)
    width, height = img.size
    if (width * height * 3 <= len(text)):
        messagebox.showerror("Неверный ввод", "Вы ввели слишком длинное сообщение для выбранной картинки")
    else:
        
        text_bit = ''
        for i in range(len(text)):
            ascii_symbol = bin(ord(text[i]))[2:]
            ascii_symbol = '0'*(8-len(ascii_symbol)) + ascii_symbol
            text_bit += ascii_symbol

        text_bit += '00000000'
        counter = 0
        flag = 1
        
        for i in range(len(pixel_array)):
            for j in range(len(pixel_array[0])):
                for z in range(len(pixel_array[0][0])):
                    if counter + 1 != len(text_bit):
                        if pixel_array[i][j][z] % 2 == 0 and int(text_bit[counter]) % 2 == 1:
                            pixel_array[i][j][z] += 1
                        elif pixel_array[i][j][z] % 2 == 1 and int(text_bit[counter]) % 2 == 0:
                            pixel_array[i][j][z] -= 1
                            
                        counter += 1
                    else:
                        if flag:
                            img = Image.fromarray(pixel_array, 'RGBA')
                            img.save(path)
                            if isimg.get() == 0:
                                pass
                            else:
                                img.show()
                            flag = 0

# Вызов шифрования в картинку

def cryption(isimg):
    img, path = open_img()

    window_input = Toplevel()
    window_input.title("Ввод слова")

    label_input = Label(window_input, text="Введите сообщение: ")
    input_message = Entry(window_input)
    button_ok = Button(window_input, text="Зашифровать сообщение", command=lambda: cryp_text(input_message.get(), img, path, isimg))

    label_input.grid(row=0, column=0)
    input_message.grid(row=0, column=1)
    button_ok.grid(row=1, column=0)

    mainloop()
    
# Дешифровка картинки

def encryption():
    img, path = open_img()
    pixel_array = np.array(img)
    
    flag = 1
    counter = 0
    symbol = ''
    text = ''
    
    for i in range(len(pixel_array)):
        for j in range(len(pixel_array[0])):
            for z in range(len(pixel_array[0][0])):
                if flag:
                    symbol += bin(pixel_array[i][j][z])[-1]
                    if len(symbol) == 8 and (int(symbol, 2) > 127 or int(symbol, 2) < 32):
                        flag = 0
                    elif len(symbol) == 8:
                        text += chr(int(symbol, 2))
                        symbol = ''
                    elif symbol == '00000000':
                        flag = 0
    if text == '':
        messagebox.showerror("Ошибка", "В выбранной картинке нет зашифрованного сообщения")
    else:
        messagebox.showinfo("Зашифрованное сообщение", "В выбранной картинке обнаружено зашифрованное сообщение: {:}".format(text)) 

# Интерфейс

def main():

    window = Tk()
    window.title("Лабораторная работа №3")
    window.resizable(False, False)

    isimg=IntVar()
    
    label_win = Label(window, text="Выберите режим работы")
    img_check = Checkbutton(text="Показать картинку после завершения работы", variable=isimg)
    button_cryp = Button(window, text="Зашифровать", command=lambda: cryption(isimg))
    button_encryp = Button(window, text="Дешифровать", command=lambda: encryption())

    label_win.grid(row=0, column=0)
    button_cryp.grid(row=1, column=0)
    button_encryp.grid(row=1, column=1)
    img_check.grid(row=2, column=0)

    mainloop()
    
if __name__ == "__main__":
    main()


