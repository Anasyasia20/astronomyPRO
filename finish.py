# Написать программу, обладающую графическим интерфейсом. В программе должны присутствовать:
# -окно ввода пути к fits -файлу
# -окна ввода координат интересующей звёзды
# -окна ввода радиуса звёзды и внешнего и внутреннего радиусов фона
# -кнопка, при нажатии которой выполняется фотометрия данной звёзды и поток(в отсчетах) выводится пользователю.
# - chekbutton или radiobutton, позволяющие пользователю выбрать, какие графики для данной звёзды он хотел бы получить (профиль по координате Х, профиль по координате Y, 3D профиль)
# -кнопка, в результате нажатия на которую, пользователю выводятся графики, выбранные в предыдущем пункте.
import tkinter
import astropy.io.fits as pf
import matplotlib.pyplot as plt
import numpy as np
from tkinter import *
from tkinter import messagebox

# Графики
def graph_3D(Colour='#11aa55'):
    dat = [] #создаём список
    for i in range(-r, r): #range-функция для создания списка чисел. Перебор последовательности
        for j in range(-r, r):
            dat.append([x + i, y + j, data[y + j][x + i]]) #создаём список, интервалы и отсчёты
    fig = plt.figure() #создаём пустой каркас
    axes = fig.add_subplot(111, projection='3d') #параметр для построения графика
    x_d = [p[0] for p in dat]
    y_d = [p[1] for p in dat]
    z_d = [p[2] for p in dat]
    axes.plot_trisurf(x_d, y_d, z_d, linewidth=0.2) #
    plt.show()

#графики в профиль 2д
def profile(xp, yp, type): #объявим функцию с параметрами
    global data, r #Глобальные переменные
    if type == "horisontal": #== операция сравнения
        abciss = list(range(xp - r, xp + r)) #создание списка
        plt.plot(abciss, data[yp][(xp - r):(xp + r)]) #задаём аргументы для графика
        plt.title("Горизонтальный профиль") #подзаголовок
        plt.show()
    if type == "vertical":
        abciss = list(range(yp - r, yp + r))
        data_ver=data.T #?
        plt.plot(abciss, data_ver[xp][(yp - r):(yp + r)])
        plt.title("Вертикальный профиль")
        plt.show()

# команда для интерфейса
def ok():
    global x, y, r, file, data
    try:
        photo = pf.open(txt.get(1.0, END).replace("\n", ""))
        data = photo[0].data
        photo.close()
        x = int(x_coord.get(1.0, END)) #аргумент с первого до конца
        y = int(y_coord.get(1.0, END))
        r = int(mesto_vvoda_r.get(1.0, END))

    except BaseException as e:
        messagebox.showinfo("Ошибка", f"Недопустимый ввод данных\n\n{e} ")
    if chk_X_state.get():
        profile(x, y, "horisontal")
    if chk_Y_state.get():
        profile(x, y, "vertical")
    if chk_3D_state.get():
        graph_3D()

# Открываем окно
window = Tk()
window.title("ASTRO")
window.geometry('600x300')

# оформление текста данных
lbl_file = Label(window, text="Путь к файлу:", font=("Arial Bold", 10))
lbl_file.grid(column=0, row=0)

txt = Text(window, width=40, height=1)
txt.insert(tkinter.END, r'C:\Users\Настя\PycharmProjects\pythonProject1\v523cas60s-001.fit') #вставка текста insert
txt.grid(column=1, row=0)

lbl_X = Label(window, text="Координата X:", font=("Arial Bold", 10))
lbl_X.grid(column=0, row=1) #гр размещает данных в сетке

x_coord = Text(window, width=40, height=1)
x_coord.insert(tkinter.END, "453")
x_coord.grid(column=1, row=1)

lbl_Y = Label(window, text="Координата Y:", font=("Arial Bold", 10))
lbl_Y.grid(column=0, row=2)

y_coord = Text(window, width=40, height=1)
y_coord.insert(tkinter.END, "678")
y_coord.grid(column=1, row=2)

lbl_r = Label(window, text="Радиус звезды:", font=("Arial Bold", 10))
lbl_r.grid(column=0, row=3)

mesto_vvoda_r = Text(window, width=40, height=1)
mesto_vvoda_r.insert(tkinter.END, "4")  # вставляем своё значение
mesto_vvoda_r.grid(column=1, row=3)


# Checkbuttons
chk_X_state = IntVar()
chk_X_state.set(1)
chk_X = Checkbutton(window, text='Профиль по X', var=chk_X_state)
chk_X.grid(column=1, row=6)

chk_Y_state = IntVar()
chk_Y_state.set(1)
chk_Y = Checkbutton(window, text='Профиль по Y', var=chk_Y_state)
chk_Y.grid(column=1, row=7)

chk_3D_state = IntVar()
chk_3D_state.set(1)
chk_3D = Checkbutton(window, text='3D график', var=chk_3D_state)
chk_3D.grid(column=1, row=8)


btn_ok = Button(window, text="OK", command=ok)
btn_ok.grid(column=1, row=10)

# Финиш
window.mainloop()
