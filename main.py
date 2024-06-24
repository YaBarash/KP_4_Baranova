from src.api import HHApi
from src.vacancy import Vacancy
from src.json_saver import JSONSaver


def work_one_vacancy():
    '''
    Функция для работы с 1 вакансией
    :return:
    '''

    # Создание экземпляра класса для работы с API сайтов с вакансиями
    hh_api = HHApi()

    # Получение вакансий с hh.ru в формате JSON
    hh_vacancies = hh_api.get_vacancies('Python')

    # Преобразование набора данных из JSON в список объектов
    vacancies_list = Vacancy.create_vacancies(hh_vacancies)

    # Пример работы конструктора класса с одной вакансией
    vacancy = Vacancy("Python Developer", "https://hh.ru/vacancy/100742575", {'from': 1, 'to': 2})

    # Сохранение информации о вакансиях в файл
    json_saver = JSONSaver()
    json_saver.write_file(vacancies_list)
    json_saver.add_vacancy(vacancy)
    json_saver.delete_vacancy(vacancy)
    # print(json_saver.read_file())


def user_interaction():
    '''
    Функция для взаимодействия с пользователем
    :return:
    '''
    search_query = input("Введите название вакансии: ")
    top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    filter_words = input("Введите ключевые слова для фильтрации вакансий: ").split()

    hhru_api = HHApi()

    all_vacancies = hhru_api.get_vacancies(search_query)
    vacancies_list = Vacancy.create_vacancies(all_vacancies)
    filtered_vacancies = Vacancy.filter_vacancies(vacancies_list, filter_words)
    sorted_vacancies = Vacancy.sort_vacancies(filtered_vacancies)
    top_vacancies = Vacancy.get_top_vacancies(sorted_vacancies, top_n)
    print(top_vacancies)


if __name__ == "__main__":
    user_interaction()
    work_one_vacancy()
