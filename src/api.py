from abc import ABC, abstractmethod
import requests


class BaseAPI(ABC):
    @abstractmethod
    def get_vacancies(self, keyword):
        pass


class HHApi(BaseAPI):
    def __init__(self):
        self.base_url = 'https://api.hh.ru/vacancies'
        self.headers = {'User-Agent': 'HH-User-Agent'}
        self.params = {
            'per_page': 100
        }

    def get_vacancies(self, keyword):
        self.params.update({'text': keyword})
        response = requests.get(self.base_url, headers=self.headers, params=self.params)
        # print(response.json()['items'])
        return response.json()['items']



