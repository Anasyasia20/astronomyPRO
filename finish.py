# Написать программу, обладающую графическим интерфейсом. В программе должны присутствовать:
# -окно ввода пути к fits -файлу
# -окна ввода координат интересующей звёзды
# -окна ввода радиуса звёзды и внешнего и внутреннего радиусов фона
# -кнопка, при нажатии которой выполняется фотометрия данной звёзды и поток(в отсчетах) выводится пользователю.
# - chekbutton или radiobutton, позволяющие пользователю выбрать, какие графики для данной звёзды он хотел бы получить (профиль по координате Х, профиль по координате Y, 3D профиль)
# -кнопка, в результате нажатия на которую, пользователю выводятся графики, выбранные в предыдущем пункте.

import astropy.io.fits as pf
import matplotlib.pyplot as plt
import numpy as np
from tkinter import *
from tkinter import scrolledtext
from tkinter import messagebox
import math as m


# Графики
def graph_3D(Colour='#11aa55'):
    points = []
    for i in range(-r, r):
        for j in range(-r, r):
            points.append([x + i, y + j, data[y + j][x + i]])
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    x_p = [p[0] for p in points]
    y_p = [p[1] for p in points]
    z_p = [p[2] for p in points]
    ax.plot_trisurf(x_p, y_p, z_p, linewidth=0.2, antialiased=True)
    plt.show()


def profile(xp, yp, type):
    global data, r
    if type == "horisontal":
        abciss = list(range(xp - r, xp + r))
        plt.plot(abciss, data[yp][(xp - r):(xp + r)])
        plt.title("Горизонтальный профиль")
        plt.show()
    if type == "vertical":
        abciss = list(range(yp - r, yp + r))
        data_vrem = data.T
        plt.plot(abciss, data_vrem[xp][(yp - r):(yp + r)])
        plt.title("Вертикальный профиль")
        plt.show()

# Поток в отсчетах

# Command OK
def ok():
    global x, y, r, file, data
    try:
        snimok = pf.open(txt.get(1.0, END).replace("\n", ""))
        data = snimok[0].data
        snimok.close()
        x = int(x_coord.get(1.0, END))
        y = int(y_coord.get(1.0, END))
        r = int(mesto_vvoda_r.get(1.0, END))

    except BaseException as e:
        messagebox.showinfo("Ошибка", f"Недопустимый ввод данных\n\n{e} ")
    global sum_otchetov
    if chk_X_state.get():
        profile(x, y, "horisontal")
    if chk_Y_state.get():
        profile(x, y, "vertical")
    if chk_3D_state.get():
        graph_3D()



# Открываем окно
window = Tk()
window.title("THE STAR")
window.geometry('600x300')
# Вводные данные

lbl_file = Label(window, text="Путь к файлу:", font=("Arial Bold", 10))
lbl_file.grid(column=0, row=0)

txt = Text(window, width=40, height=1)
txt.insert(INSERT, r'C:\Users\Настя\PycharmProjects\pythonProject1\v523cas60s-001.fit')
txt.grid(column=1, row=0)

lbl_X = Label(window, text="Координата X:", font=("Arial Bold", 10))
lbl_X.grid(column=0, row=1)

x_coord = Text(window, width=40, height=1)
x_coord.insert(INSERT, "453")
x_coord.grid(column=1, row=1)

lbl_Y = Label(window, text="Координата Y:", font=("Arial Bold", 10))
lbl_Y.grid(column=0, row=2)

y_coord = Text(window, width=40, height=1)
y_coord.insert(INSERT, "678")
y_coord.grid(column=1, row=2)

lbl_r = Label(window, text="Радиус звезды(r):", font=("Arial Bold", 10))
lbl_r.grid(column=0, row=3)

mesto_vvoda_r = Text(window, width=40, height=1)
mesto_vvoda_r.insert(INSERT, "4")  # вставляем своё значение
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
chk_3D = Checkbutton(window, text='3D график      ', var=chk_3D_state)
chk_3D.grid(column=1, row=8)


btn_ok = Button(window, text="OK", command=ok)
btn_ok.grid(column=2, row=7)

# Финиш
window.mainloop()
