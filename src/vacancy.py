import json
import os.path


class Vacancy:
    def __init__(self, name, url, salary: dict):
        self.salary_to = 0
        self.salary_from = 0
        self.name = name
        self.url = url
        self.salary = salary
        self.validate()

    def validate(self):
        if self.salary and type(self.salary) is not int:
            if self.salary['from']:
                self.salary_from = self.salary['from']
            if self.salary['to']:
                self.salary_to = self.salary['to']

    @classmethod
    def create_vacancies(cls, data):
        instance = []
        for vac_info in data:
            name = vac_info.get('name')
            url = vac_info.get('alternate_url')
            salary = vac_info.get('salary')
            instances = cls(name, url, salary)
            instance.append(instances)
        return instance

    def __lt__(self, other):
        if isinstance(other, Vacancy):
            return self.salary_from < other.salary_from

    def __repr__(self):
        return f'{self.name} с ЗП {self.salary_from} - {self.salary_to} ссылка {self.url}'

    @classmethod
    def filter_vacancies(cls, vacancies_list, keywords: list):
        filtered_vacancies_list = []
        for word in keywords:
            word_lower = word.lower()
            for vac in vacancies_list:
                if word_lower in vac.name.lower().split():
                    filtered_vacancies_list.append(vac)
        return filtered_vacancies_list

    @classmethod
    def sort_vacancies(cls, filtered_vacancies_list):
        filtered_vacancies_list.sort(reverse=True)
        return filtered_vacancies_list

    @classmethod
    def get_top_vacancies(cls, sorted_vacancies_list, count_top: int):
        return sorted_vacancies_list[:count_top]

    def convert_to_dict(self):
        convert = dict(name=self.name, url=self.url, salary_from=self.salary_from, salary_to=self.salary_to)
        return convert
