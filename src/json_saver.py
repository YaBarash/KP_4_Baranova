import os, json
from src.vacancy import Vacancy
from abc import ABC, abstractmethod


class JSONAbstract(ABC):
    '''
    Абстрактный класс для работы с файлами
    '''

    @abstractmethod
    def read_file(self):
        pass

    @abstractmethod
    def write_file(self, data):
        pass

    @abstractmethod
    def add_vacancy(self, vacancy: Vacancy):
        pass

    @abstractmethod
    def delete_vacancy(self, vacancy: Vacancy):
        pass


class JSONSaver(JSONAbstract):
    '''
    Класс для сохранения инфо о вакансиях в JSON-файл
    '''

    def __init__(self):
        self.path = self.check_path()

    @staticmethod
    def check_path():
        '''
        Функция, проверяющая наличие файла и папке в корне проекта
        :return:Абсолютный путь до файла
        '''
        path = os.path.abspath(os.path.join('data', 'vacancies.json'))
        if not os.path.exists(path):
            with open(path, 'w', encoding='utf-8') as file:
                file.write('[]')
        return path

    def read_file(self):
        '''
        Функция чтения файла (загрузка данных)
        :return:Список вакансий
        '''
        with open(self.path, 'r', encoding='utf-8') as file:
            return json.load(file)

    def write_file(self, data):
        '''
        Функция для записи вакансий в файл
        :param data: список вакансий
        :return:
        '''
        json_list = []
        with open(self.path, 'w', encoding='utf-8') as file:
            for i in data:
                if type(i) is not dict:
                    item = i.convert_to_dict()
                    json_list.append(item)
                else:
                    continue
            json.dump(json_list, file, indent=4, ensure_ascii=False)

    def add_vacancy(self, vacancy: Vacancy):
        '''
        Функция для добавления 1 вакансии в файл
        :param vacancy: Экземпляр класса Vacancy
        :return:
        '''
        file_content = self.read_file()
        file_content.append(vacancy)
        self.write_file(file_content)

    def delete_vacancy(self, vacancy: Vacancy):
        '''
        Функция для удаления 1 вакансии в файл
        :param vacancy: Экземпляр класса Vacancy
        :return:
        '''
        file_content = self.read_file()
        for i in file_content:
            if i['name'] == vacancy.name and i['url'] == vacancy.url:
                file_content.remove(i)
                self.write_file(file_content)
