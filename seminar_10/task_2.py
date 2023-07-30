"""Привожу пример одного из моего класса, который написал для работы с dicom изображениями"""



# coding=utf-8
import io

import numpy as np

import requests
from PIL import Image


class DicomPost:
    def __init__(self, dic_config):
        self.server_address = "http://{}:{}".format(dic_config["server_ip"], dic_config["html_port"])
        self.login = dic_config["login_orthanc"]
        self.password = dic_config["pass_orthanc"]

    def find_patient_by_ID(self, target_patient_i):
        url = "{}/patients".format(self.server_address)
        response = requests.get(url, auth=(self.login, self.password))
        if response.status_code == 200:
            patients_data = response.json()
            for patient_id in patients_data:
                url_patient_id = "{}/{}".format(url, patient_id)
                response_patient = requests.get(url_patient_id, auth=(self.login, self.password))
                if response_patient.status_code == 200:
                    patient_data = response_patient.json()
                    patient_i = patient_data.get("MainDicomTags", {}).get("PatientID")
                    if patient_i == target_patient_i:
                       return patient_data
            return None
        else:
            return None

    def find_patient_by_studies(self, target_patient_studies):
        url = "{}/studies/{}".format(self.server_address, target_patient_studies)
        response = requests.get(url, auth=(self.login, self.password))
        if response.status_code == 200:
            patient_data = response.json()
            patient_date = patient_data.get("MainDicomTags", {}).get("StudyDate")
            patient_seri = patient_data.get("Series")
            return patient_date, patient_seri
        else:
            return None

    def find_path_images_old(self, patient_seri):
        series_url = "{}/series/{}".format(self.server_address, patient_seri[0])
        print (series_url)
        series_response = requests.get(series_url, auth=(self.login, self.password))
        series_data = series_response.json()
        image_paths  = []
        for instance in series_data['Instances']:
            instances_url = "{}/instances/{}/preview".format(self.server_address, instance)
            print (instances_url)
            image_response = requests.get(instances_url, auth=(self.login, self.password))
            image_paths.append(image_response)
            print image_paths
        return image_paths

    def find_path_images(self, patient_seri):
        series_url = "{}/series/{}".format(self.server_address, patient_seri[0])
        print(series_url)
        series_response = requests.get(series_url, auth=(self.login, self.password))
        series_data = series_response.json()
        image_paths = []
        for instance in series_data['Instances']:
            instances_url = "{}/instances/{}/preview".format(self.server_address, instance)
            print(instances_url)
            image_response = requests.get(instances_url, auth=(self.login, self.password))
            if image_response.status_code == 200:
                image_data = image_response.content
                # Создание объекта "файлоподобного" объекта из данных изображения
                image_file = io.BytesIO(image_data)
                # Открытие изображения с помощью Pillow
                image = Image.open(image_file)
                # Применение обработки изображения, если необходимо
                processed_image = self.process_jpeg_image(image)
                # Сохранение изображения в формате PNG в память вместо диска
                image_bytes = io.BytesIO()
                processed_image.save(image_bytes, format='PNG')
                image_bytes.seek(0)
                # Добавление изображения в self.image_paths
                image_paths.append(image_bytes)
            print (image_paths)
        return image_paths

    def process_jpeg_image(self, image_data):
        pixel_data = np.array(image_data)
        pixel_data_normalized = (pixel_data - np.min(pixel_data)) * (255.0 / (np.max(pixel_data) - np.min(pixel_data)))
        pixel_data_normalized = pixel_data_normalized.astype(np.uint8)
        min_value = np.percentile(pixel_data_normalized, 5)
        max_value = np.percentile(pixel_data_normalized, 95)
        denominator = max_value - min_value
        if denominator == 0:
            denominator = 1  # Защита от деления на ноль
        pixel_data_stretched = np.clip((pixel_data_normalized - min_value) * (255 / denominator), 0, 255)
        pixel_data_stretched = pixel_data_stretched.astype(np.uint8)

        # Создание объекта изображения с использованием нормализованного массива пикселей
        processed_image = Image.fromarray(pixel_data_stretched)

        return processed_image