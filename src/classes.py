import os.path

import requests

from src.abs_classes import BaseClass, Parser, VacansyLoadAbs


class HH(Parser):
    """
    Класс для работы с API HeadHunter
    """

    def __init__(self, file_worker):
        self.url = 'https://api.hh.ru/vacancies'
        self.headers = {'User-Agent': 'HH-User-Agent'}
        self.params = {'text': '', 'page': 0, 'per_page': 100}
        self.vacancies = []
        #super().__init__(file_worker)


    def load_vacancies(self, keyword):
        self.params['text'] = keyword
        while self.params.get('page') != 20:
            response = requests.get(self.url, headers=self.headers, params=self.params)
            vacancies = response.json()['items']
            self.vacancies.extend(vacancies)
            self.params['page'] += 1
            return vacancies


class Vacansy(BaseClass, HH):
    """
        Класс для работы с вакансиями
        """

    name: str
    link: str
    salary: int
    description: str
    def __init__(self, name, link, salary, description):
        self.name = name
        self._link = link
        self.__salary = salary
        self.description = description



    def salary(self):
        if self.__salary:
            return self.__salary
        else:
            return self.__salary == 0


    def comparison(self, other):
        if self.__salary > other.__salary:
            return self.salary
        elif self.__salary == other.__salary:
            return 'Зарплаты равны'
        else:
            return other.__salary


class VacansyLoadJson(VacansyLoadAbs, HH):
    """Выводит информацию в файл """
    vacansies:list
    def __init__(self,vacansies):
        self.vacansies = vacansies
        super().__init__()


    def json_load(self, info: list):
        with open(os.path.abspath('json_file'),'a', encoding='utf-8') as file:
            file.write(f'{info}')
