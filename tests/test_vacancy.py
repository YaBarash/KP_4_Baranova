from src.vacancy import Vacancy
import pytest


@pytest.fixture()
def vacancy():
    return Vacancy('Python backend developer (Junior/ Junior+)', 'https://hh.ru/vacancy/102191917',
                   {'from': 100_000, 'to': 120_000})


def test_init(vacancy):
    assert vacancy.name == 'Python backend developer (Junior/ Junior+)'
    assert vacancy.url == 'https://hh.ru/vacancy/102191917'
    assert vacancy.salary_from == 100_000
    assert vacancy.salary_to == 120_000


@pytest.fixture()
def vacancy_list():
    return [
        {
            'name': 'Python backend developer (Junior/ Junior+)',
            'alternate_url': 'https://hh.ru/vacancy/102191917',
            'salary': None
        },
        {
            'name': 'Python Developer',
            'alternate_url': 'https://hh.ru/vacancy/100742573',
            "salary": {
                "from": 200_000,
                "to": 220_000,
                "currency": "RUR",
                "gross": False
            }
        }
    ]
    # {
    #     'name': 'Python Middle',
    #     'url': 'https://hh.ru/vacancy/100742572/',
    #     'salary_from': 300_000,
    #     'salary_to': 320_000
    # }
    # ]


def test_create_vacancies(vacancy_list):
    vacancy_first = Vacancy('Python backend developer (Junior/ Junior+)', 'https://hh.ru/vacancy/102191917', None)
    vacancy_second = Vacancy('Python Developer', 'https://hh.ru/vacancy/100742573', {'from': 200_000, 'to': 220_000})
    assert Vacancy.create_vacancies(vacancy_list) == [vacancy_first, vacancy_second]


def test_filter_vacancies(vacancy_list):
    vacancy_list_new = Vacancy.create_vacancies(vacancy_list)
    assert Vacancy.filter_vacancies(vacancy_list_new, ['developer']) == [
        Vacancy('Python backend developer (Junior/ Junior+)', 'https://hh.ru/vacancy/102191917', None),
        Vacancy('Python Developer', 'https://hh.ru/vacancy/100742573', {'from': 200_000, 'to': 220_000})
    ]
