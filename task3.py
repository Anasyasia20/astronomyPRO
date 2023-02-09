import numpy as np
import astropy.io.fits as pyfits
import matplotlib.pyplot as plt

list = pyfits.open("v523cas60s-001.fit") # открываем файл
scidata = list[0].data # 1 слой

a = np.transpose(scidata) # трансопнирование матрицы
plt.subplot(121) #число строк и столбцов, индекс текущих координатных осей
plt.plot(a[453][673:683]) # срез по строкам

plt.xlabel('Кривая блеска по оси Y')#подписи к графику
plt.ylabel('Число отсчётов')
plt.title('Вертикальный профиль', fontsize=11, fontname='Times New Roman')

plt.subplot(122)#число строк и столбцов, индекс текущих координатных осей
plt.plot(scidata[678][448:458]) #срез по столбцам

plt.xlabel('Кривая блеска по оси X') #подписи к графику
plt.ylabel('Число отсчётов')
plt.title('Горизонтальный профиль', fontsize=11, fontname='Times New Roman')


plt.show()
