# файл выделяет паталогии на рентген снимки, данные для выделения берутся из базы данных "ChestXray-NIHCC"

import os
import csv
import copy
import cv2

data_index = 750  # номер картинке в списке bbox


def load_bbox_csv():
    # функция открывает csv файл с информацией о координатах прамоугольников,
    # внутри которых находятся обрнаруженные паталогии.
    with open(os.path.dirname(__file__) + '/../Data/BBox_List_2017.csv') as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader, None)
        column = {}
        for h in header:
            column[h] = []
        for row in reader:
            for h, v in zip(header, row):
                column[h].append(v)
    return column


def make_sorted_dict():
    # функция создает словарь с отсортированными данными по файлу с bbox
    bbox_raw_dataset = load_bbox_csv()
    bbox_sorted_dataset = copy.deepcopy(bbox_raw_dataset)
    for lin in bbox_sorted_dataset:
        bbox_sorted_dataset[lin].clear()
    list_of_labels = bbox_raw_dataset['Finding Label']
    labels = []
    for label in list_of_labels:
        if label in labels:
            pass
        else:
            labels.append(label)
    for index, line in enumerate(list_of_labels):
        bbox_sorted_dataset['Image Index'].append(bbox_raw_dataset['Image Index'][index])
        bbox_sorted_dataset['Finding Label'].append(bbox_raw_dataset['Finding Label'][index])
        bbox_sorted_dataset['Bbox [x'].append(bbox_raw_dataset['Bbox [x'][index])
        bbox_sorted_dataset['y'].append(bbox_raw_dataset['y'][index])
        bbox_sorted_dataset['w'].append(bbox_raw_dataset['w'][index])
        bbox_sorted_dataset['h]'].append(bbox_raw_dataset['h]'][index])
    return bbox_sorted_dataset


def return_image_with_rictangle_data(data_index):
    image_with_bbox_dataset = make_sorted_dict()
    image_path = os.path.dirname(__file__) + '/../Data/images_001/images/' + \
                 image_with_bbox_dataset['Image Index'][data_index]
    start_bbox_points = (int(float(image_with_bbox_dataset['Bbox [x'][data_index])),
                         int(float(image_with_bbox_dataset['y'][data_index])))
    end_bbox_points = (int(float(image_with_bbox_dataset['Bbox [x'][data_index])) +
                       int(float(image_with_bbox_dataset['w'][data_index])),
                       int(float(image_with_bbox_dataset['y'][data_index])) +
                       int(float(image_with_bbox_dataset['h]'][data_index])))
    disease = image_with_bbox_dataset['Finding Label'][data_index]
    return image_path, start_bbox_points, end_bbox_points, disease


def snow_image_with_rectangle(image_index):
    image_path, start_bbox_points, end_bbox_points, desease = return_image_with_rictangle_data(image_index)
    image = cv2.imread(image_path)
    color = (0, 0, 255)
    tickness = 2
    image = cv2.rectangle(image, start_bbox_points, end_bbox_points, color, tickness)
    try:
        cv2.imshow('image', image)
    except cv2.error:
        pass
    print(desease)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def snow_all_images_by_disease(disease):
    bbox_sorted_dict = make_sorted_dict()
    for index, data in enumerate(bbox_sorted_dict['Image Index']):
        if bbox_sorted_dict['Finding Label'][index] == disease:
            snow_image_with_rectangle(index)


#snow_image_with_rectangle(data_index)
snow_all_images_by_disease('Pneumonia')
