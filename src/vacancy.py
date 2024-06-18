import json
import os.path


class Vacancy:
    def __init__(self, name, url, salary):
        self.salary_to = 0
        self.salary_from = 0
        self.name = name
        self.url = url
        self.salary = salary
        self.validate()

    def validate(self):
        if self.salary:
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
        return f'{self.name} с ЗП {self.salary_from} - {self.salary_to}'

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


class JSONSaver:
    def __init__(self):
        self.path = self.check_path()

    @staticmethod
    def check_path():
        path = os.path.abspath(os.path.join('data', 'vacancies.json'))
        if not os.path.exists(path):
            with open(path, 'w', encoding='utf-8') as file:
                file.write('[]')
        return path

    def read_file(self):
        with open(self.path) as file:
            return json.load(file)

    def write_file(self, data):
        with open(self.path, 'w') as file:
            json.dump(data, file, indent=4, ensure_ascii=False)

    def add_vacancy(self, vacancy: Vacancy):
        vac_info = {
            'name': vacancy.name,
            'url': vacancy.url,
            'salary_from': vacancy.salary_from,
            'salary_to': vacancy.salary_to
        }
        file_content: list[dict] = self.read_file()
        file_content.append(vac_info)
        self.write_file(file_content)

    def delete_vacancy(self, data):
        file_content: list[dict] = self.read_file()
        for vac in file_content:
            if data in vac.keys():
                del_vac = data
                file_content.remove(del_vac)

