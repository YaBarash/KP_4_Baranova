from abc import ABC, abstractmethod
import requests


class BaseAPI(ABC):
    '''
    Абстрактный класс для работы с API сервиса с вакансиями
    '''
    @abstractmethod
    def get_vacancies(self, keyword):
        pass


class HHApi(BaseAPI):
    '''
    Класс наследник абстрактного класса для работы с hh.ru
    Получает вакансии, подключаясь к API
    '''
    def __init__(self):
        self._base_url = 'https://api.hh.ru/vacancies'
        self._headers = {'User-Agent': 'HH-User-Agent'}
        self.params = {
            'per_page': 100
        }

    def get_vacancies(self, keyword):
        '''
        Функция получения вакансий через запрос пользователя по полученному слову keyword
        '''
        self.params.update({'text': keyword})
        response = requests.get(self._base_url, headers=self._headers, params=self.params)
        return response.json()['items']



