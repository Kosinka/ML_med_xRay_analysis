#файл выполняющий сортировку данных из базы данных рентген снимков грудной клетки "ChestXray-NIHCC" по паталогиям

import os
import shutil
import csv


def load_csv():
    # функция загрузки файла csv с базой данных по рентген снимкам, идет вместе с базой данных
    with open(os.path.dirname(__file__) + '/../Data/Data_Entry_2017.csv') as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader, None)
        column = {}
        for h in header:
            column[h] = []
        for row in reader:
            for h, v in zip(header, row):
                column[h].append(v)
        list_of_table = makedir(column['Finding Labels'])
        file_list(list_of_table, column['Image Index'], column['Finding Labels'])


def makedir(labels):
    # функция создает папки для сортировки по ним рентген снимоков с разными паталогиями,
    # снимки с несколькими паталогиями не копируются
    list_of_labels = []
    new_list_of_lables = []
    os.chdir(os.path.dirname(__file__) + '/../Data/Sorted/')
    for i in labels:
        if i in list_of_labels:
            pass
        else:
            list_of_labels.append(i)
    for i in list_of_labels:
        if i.find('|') != -1:
            pass
        else:
            new_list_of_lables.append(i)
    for i in new_list_of_lables:
        os.mkdir(os.path.dirname(__file__) + '/../Data/Sorted/' + i + '/')
    return new_list_of_lables


def file_list(list_of_table, images, labels):
    # сортировка файлов рентген снимков по папкам в зависимости от паталогии
    print(os.listdir(os.path.dirname(__file__) + '/../Data/images_001/images'))
    for index, image in enumerate(images):
        if labels[index] in list_of_table:
            shutil.copyfile(os.path.dirname(__file__) + '/../Data/images_001/images/' + images[index], os.path.dirname(__file__) + '/../Data/Sorted/' + labels[index] + '/' + images[index])
        else:
            pass


load_csv()
