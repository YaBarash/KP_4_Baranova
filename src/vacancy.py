class Vacancy:
    def __init__(self, name, url, salary_from, salary_to, city, experience):
        self.name = name
        self.url = url
        self.salary_from = salary_from
        self.salary_to = salary_to
        self.city = city
        self.experience = experience
        self.validate()

    def validate(self):
        if self.salary_from is None:
            self.salary_from = 0
        if self.url is None:
            self.url = 'Ссылка не найдена'
        if self.city is None:
            self.city = 'Город не указан'
        if self.experience is None:
            self.experience = 'Нет опыта'

    @classmethod
    def create_vacancies(cls, data):
        instances = []
        for vac_info in data:
            name = vac_info.get('name')
            url = vac_info.get('alternate_url')
            salary_from = vac_info.get('salary_from')
            salary_to = vac_info.get('salary_to')
        instance = cls(name, url, salary_from, salary_to)