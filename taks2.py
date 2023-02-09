import time
f = open('task2_data.dat', 'r')  #открытие файла на чтение
stars = f.read().split('\n')  #считывание файла, разделяя по строкам
#создание списка
entries = []  # метод для удаления повторяющихся элементов из списка, создание списка списков
for entry in stars:  # перебор всех рядов
    entries.append(entry.split())  # разделяем ряды по пробелам
entries = entries[1:]  # 1: удаляем первое значение (названия столбцов) срез массива выделяем конкретный элемент
stars = entries  # переобозначаем списки
entries = []  # обнуляем список, оно полностью не очищает
# создает новый список и привязывает его к переменной, но старый список остаются в памяти
# objects = []  # имена объектов
# filters = []  # фильтры
objects = set() # set создание набора из списка
filters = set()

# entry = [имя объекта, дата, фильтр, звездная величина] массив это список списков
for entry in stars:
    name = ''  # формируем одинаковое имя
    if len(entry) > 4:  # в имени есть пробел
        name = entry[0] + ' ' + entry[1]  # первая часть имени и пробел и вторая часть имени
        entry = [name] + entry[2:]  # обновляем ряд и добавляем первые 3 элемента
    elif len(entry) < 4:  # ряд не рассматриваем
        continue
    else:
        name = entry[0]
# Оператор ветвления. Если If ложно, то выполняется elif, если и это ложно, то точно выполняется else
    # suhor в одно имя
    name = name.replace('_', '') #способ замены символа
    name = name.replace(' ', '')
    name = name[:2].upper() + ' ' + name[2:].title()
    #: срез строки первые два индекса в верхнем регистре снова преобразовываем
    #преобразует первые два индекса элемента в заглавный регистр, suhor => SU Hor

    entry[0] = name  # обновляем ряд
    entry[1] = float('24' + entry[1])  # float число с плавающей запятой
    # преобразуем дату и звездную величину в числа из строк
    entry[3] = float(entry[3])
    # проверяем на новое имя объекта
    objects.add(entry[0]) #Метод set add() добавляет заданный элемент в набор
    # проверяем на новый фильтр
    filters.add(entry[2].title())
    entries.append(entry)  # добавляем элемент в конец списка ( элементы списка в другой список методом extend())
stars = entries  # замена
entries = []  # обнуление

print('Объекты:', objects)
print('Фильтры:', filters)

#  3 part
objects_names = None #ничего не существует Множество
while objects_names not in objects:
    objects_names = input('Введите имя объекта: ') # просим пользователя ввести имя объекта

filters_names = set() #множество- неупорядоченные уникальные объекты
# intersection - пересечение множеств из множества filters
while len(filters.intersection(filters_names)) == 0: # проверка равняется ли длина нулю (Проверяет равенство значений выражений)
    i = input('Введите фильтр: ')  # то же самое, но с фильтром
    filters_names = set(i.split(','))
filters_names = filters.intersection(filters_names)

# перевод в дни и часы

unix_epoch = 2440587.5  # 1 января 1970 года в юлианских днях

def julian_to_unix(date):
    days = date - unix_epoch
    seconds = days * 24 * 60 * 60
    return seconds

def unix_to_grigorian(seconds):
    tm = time.gmtime(seconds)
    # код time.gmtime(seconds) возвращает структуру с информацией о дне, месяце и т.д.
    # из секунд с начала эпохи юникс (1 января 1970)
    day = str(tm.tm_mday)
    if len(day) == 1:  # если день - это одна цифра, то добавляем 0 в начало
        day = '0' + day
    mon = str(tm.tm_mon)
    if len(mon) == 1:
        mon = '0' + mon
    year = tm.tm_year
    hour = str(tm.tm_hour)
    if len(hour) == 1:
        hour = '0' + hour
    min = str(tm.tm_min)
    if len(min) == 1:
        min = '0' + min
    sec = str(tm.tm_sec)
    if len(sec) == 1:
        sec = '0' + sec
    return f'{day}.{mon}.{year} {hour}:{min}:{sec}'

astro = {}  # словарь с обработанной информацией из stars
for entry in stars:
    if entry[0] != objects_names:  # объект не введенный пользователем - пропускаем
        continue

    if entry[2] not in filters_names:  # фильтр не введенный пользователем - пропускаем
        continue

    if entry[1] not in astro:  # если даты нет в astro, то
        astro[entry[1]] = {'date': unix_to_grigorian(julian_to_unix(entry[1]))}
        # создаем в словаре astro и сразу вычисляем дату в нужном формате
        for filter_name in filters_names:
            astro[entry[1]][filter_name] = '-'  # назначаем всем столбцам-фильтрам значение '-'
        astro[entry[1]][entry[2]] = entry[3]  # назначаем нужному столбцу-фильтру значение звездной величины

#создание файла

f = open(f'{objects_names}.dat', 'w')  # создаем файл с нужным именем, открытие в режиме записи
headers = 'Date, HJD, '  # создаем ряд-заголовок
for filter in filters_names:
    headers = headers + filter + '\n' # добавляем столбцы-фильтры
f.write(headers)  # записываем

data = list(astro.keys())
data.sort()
for date in data:
    value = astro[date] #проходит цикл и не записывает прошлые
    j = value['date'] + '\t' + str(date) + '\t' # str приводит объект к строке value возвращает объект представления
    for filter in filters_names:
        j = j + str(value[filter]) + '\n'
    f.write(j)

