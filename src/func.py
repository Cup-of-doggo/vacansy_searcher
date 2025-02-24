from src.classes import HH, Vacansy, VacansyLoadJson


def user_interaction():
    """Ищет вакансии, выдает топ вакансий, отдает вакансию по слову в описании """
    top_vacansies = []
    founded_vacansies = []
    filtred_vacansies = []
    filtred_by_salary = []

    search_query = input("Введите поисковый запрос: ")
    vacansies = HH(Vacansy).load_vacancies(search_query)
    for one_vacansy in vacansies:
        if one_vacansy['salary'] is not None:
            filtred_vacansies.append(one_vacansy)
        else:
            continue
    for vaacansy in filtred_vacansies:
        if vaacansy['salary']['from'] is not None:
            filtred_by_salary.append(vaacansy)
        else:
            continue

    top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    sorted_vacansies = sorted(filtred_by_salary, key=lambda x: x['salary']['from'], reverse=True)
    for vacansy in sorted_vacansies:
        top_vacansies.append(vacansy)
        if len(top_vacansies) == top_n:
            break

    filter_words = input("Введите ключевые слова для фильтрации вакансий: ")
    for value in top_vacansies:
        if filter_words in value['name']:
            founded_vacansies.append(value)
    VacansyLoadJson(Vacansy).json_load(founded_vacansies)
    return founded_vacansies
