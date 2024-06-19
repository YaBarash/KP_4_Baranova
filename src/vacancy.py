class Vacancy:
    '''
    Класс работы с вакансиями
    '''
    def __init__(self, name, url, salary: dict):
        '''
        Конструктор вакансий
        :param name: Название
        :param url: Ссылка
        :param salary: Словарь со значениями зарплат
        '''
        self.salary_to = 0
        self.salary_from = 0
        self.name = name
        self.url = url
        self.salary = salary
        self.validate()

    def validate(self):
        '''
        Функция проверки поля зарплаты на отсеивание вакансий с незаданным полем (None)
        :return:
        '''
        if self.salary and type(self.salary) is not int:
            if self.salary['from']:
                self.salary_from = self.salary['from']
            if self.salary['to']:
                self.salary_to = self.salary['to']

    @classmethod
    def create_vacancies(cls, data):
        '''
        Функция создания вакансий. Класс-метод
        :param data: Список словарей с hh.ru
        :return: Обработанный писок вакансий с присвоенными полями name, url, salary, полученнные c hh.ru
        '''
        instance = []
        for vac_info in data:
            name = vac_info.get('name')
            url = vac_info.get('alternate_url')
            salary = vac_info.get('salary')
            instances = cls(name, url, salary)
            instance.append(instances)
        return instance

    def __lt__(self, other):
        '''
        Функция сравнения зарплат между собой по значению (зарплата от)
        :param other:
        :return: True
        '''
        if isinstance(other, Vacancy):
            return self.salary_from < other.salary_from

    def __repr__(self):
        return f'{self.name} с ЗП {self.salary_from} - {self.salary_to} ссылка {self.url}'

    @classmethod
    def filter_vacancies(cls, vacancies_list, keywords: list):
        '''
        Функция фильтрации вакансий по введеному доп слову от пользователя
        :param vacancies_list: Первоначальный список вакансий
        :param keywords:
        :return: Отфильтрованный список вакансий
        '''
        filtered_vacancies_list = []
        for word in keywords:
            word_lower = word.lower()
            for vac in vacancies_list:
                if word_lower in vac.name.lower().split():
                    filtered_vacancies_list.append(vac)
        return filtered_vacancies_list

    @classmethod
    def sort_vacancies(cls, filtered_vacancies_list):
        '''
        Функция сортировкис вакансий по большей зарплате между вакансиями
        :param filtered_vacancies_list: Отфильтрованный список
        :return: Отфильтрованный список по убыванию зп
        '''
        filtered_vacancies_list.sort(reverse=True)
        return filtered_vacancies_list

    @classmethod
    def get_top_vacancies(cls, sorted_vacancies_list, count_top: int):
        '''
        Функция по получению топ высокооплачиваемых вакансий
        :param sorted_vacancies_list: Отфильтрованный список по убыванию зп
        :param count_top: Кол-во необ-х пользователю топа вакансий для отображения
        :return:
        '''
        return sorted_vacancies_list[:count_top]

    def convert_to_dict(self):
        '''
        Функция для преобразования данных в словарь
        :return:
        '''
        convert = dict(name=self.name, url=self.url, salary_from=self.salary_from, salary_to=self.salary_to)
        return convert
