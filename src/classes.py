import os.path

import requests

from src.abs_classes import BaseClass, Parser, VacansyLoadAbs


class HH(Parser):
    """
    Класс для работы с API HeadHunter
    """

    def __init__(self, file_worker):
        self.__url = 'https://api.hh.ru/vacancies'
        self.__headers = {'User-Agent': 'HH-User-Agent'}
        self.__params = {'text': '', 'page': 0, 'per_page': 100}
        self.vacancies = []
        super().__init__(file_worker)


    def _load_vacancies(self, keyword):
        self.__params['text'] = keyword
        try:
            while self.params.get('page') != 20:
                response = requests.get(self.__url, headers=self.__headers, params=self.__params)
                vacancies = response.json()['items']
                self.vacancies.extend(vacancies)
                self.__params['page'] += 1
                return vacancies
        except Exception as err:
            return f'Произошла ошибка при подключении, текст ошибки:{err}'




class Vacansy(BaseClass):
    """
        Класс для работы с вакансиями
        """
    __slots__ = ('_name', '_link', '__salary', '_description')

    name: str
    link: str
    salary: int
    description: str

    def __init__(self, name, link, salary, description):
        self._name = name
        self._link = link
        self.__salary = salary
        self._description = description
        super().__init__()

    @property
    def name(self):
        return self._name


    @property
    def link(self):
        return self._link


    @property
    def description(self):
        return self._description


    def salary(self):
        if self.__salary:
            return self.__salary
        else:
            return self.__salary == 0


    def __eq__(self, other):
        if self.__salary > other.__salary:
            return self.salary
        elif self.__salary == other.__salary:
            return 'Зарплаты равны'
        else:
            return other.__salary


    def __le__(self,other):
        if self.__salary < other.__salary:
            return other.salary
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


    def json_load(self, information: list):
        with open(os.path.abspath('json_file'),'a+', encoding='utf-8') as file:
            for info in information:
                file.write(f'{info}\n')


    def file_delete(self, filename: str):
        os.remove(os.path.abspath(filename))


    def file_read(self, filename):
        with open(os.path.abspath(filename), 'r+', encoding='utf-8') as file:
            print(file.read())
            file.close()


    def information_delete(self, filename):
        with open(os.path.abspath(filename), 'r+', encoding='utf-8') as file:
            file.truncate(0)