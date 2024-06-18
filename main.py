from src.api import HHApi
from src.vacancy import Vacancy, JSONSaver


# # Создание экземпляра класса для работы с API сайтов с вакансиями
# hh_api = HHApi()
#
# # Получение вакансий с hh.ru в формате JSON
# hh_vacancies = hh_api.get_vacancies('Python')
#
# # Преобразование набора данных из JSON в список объектов
# vacancies_list = Vacancy.create_vacancies(hh_vacancies)
#
# # Пример работы контструктора класса с одной вакансией
# # vacancy = Vacancy("Python Developer", "http://1234", "100 000", "150 000")
#
# # Сохранение информации о вакансиях в файл
# json_saver = JSONSaver()
# json_saver.write_file(vacancies_list)
# print(json_saver.read_file())
# # json_saver.delete_vacancy(vacancies_list)


# Функция для взаимодействия с пользователем
def user_interaction():
    search_query = input("Введите название вакансии: ")
    top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    filter_words = input("Введите ключевые слова для фильтрации вакансий: ").split()

    hh_api = HHApi()

    all_vacancies = hh_api.get_vacancies(search_query)
    print(all_vacancies)
    vacancies_list = Vacancy.create_vacancies(all_vacancies)
    # print(vacancies_list)
    vacancies_list.sort(reverse=True)
    # print(vacancies_list)

    filtered_vacancies = Vacancy.filter_vacancies(vacancies_list, filter_words)
    print(filtered_vacancies)

    ranged_vacancies = get_vacancies_by_salary(filtered_vacancies, salary_range)
    #
    # sorted_vacancies = sort_vacancies(ranged_vacancies)
    # top_vacancies = get_top_vacancies(sorted_vacancies, top_n)
    # print_vacancies(top_vacancies)


if __name__ == "__main__":
    user_interaction()
