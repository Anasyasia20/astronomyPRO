import astropy.io.fits as pf
import matplotlib.pyplot as plt
import numpy as np
from tkinter import *
from tkinter import scrolledtext
from tkinter import messagebox
import math as m

#Графики

def graph_3D(colour=None, cmap_='BuPu_r'):
    points = []
    for i in range(-R, R):
        for j in range(-R, R):
            points.append([x + i, y + j, data[y + j][x + i]])
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    x_p = [p[0] for p in points]
    y_p = [p[1] for p in points]
    z_p = [p[2] for p in points]
    ax.plot_trisurf(x_p, y_p, z_p, linewidth=0.2, antialiased=True, color=colour, cmap = cmap_)
    plt.show()

def profile(xp, yp, type):
    global data, R
    if type == "horisontal":
        abciss = list(range(xp-R, xp+R))
        plt.plot(abciss, data[yp][(xp-R):(xp+R)])
        plt.title("Горизонтальный профиль")
        plt.show()
    if type == "vertical":
        abciss = list(range(yp - R, yp + R))
        data_vrem = data.T
        plt.plot(abciss, data_vrem[xp][(yp-R):(yp+R)])
        plt.title("Вертикальный профиль")
        plt.show()
# #Reds Blues_r BrBG_r BuPu_r