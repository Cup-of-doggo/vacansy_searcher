from abc import ABC, abstractmethod

import requests


class BaseClass(ABC):

    __slots__ = ('name', '_link', '__salary', 'description')

    def __init__(self):
        pass



class Parser(ABC):


    def __init__(self, file_worker):
        self.url = 'https://api.hh.ru/vacancies'
        self.headers = {'User-Agent': 'HH-User-Agent'}
        self.params = {'text': '', 'page': 0, 'per_page': 100}
        self.vacancies = []
        # super().__init__(file_worker)


    @abstractmethod
    def _load_vacancies(self, keyword):
        self.params['text'] = keyword
        while self.params.get('page') != 20:
            response = requests.get(self.url, headers=self.headers, params=self.params)
            vacancies = response.json()['items']
            self.vacancies.extend(vacancies)
            self.params['page'] += 1
            return vacancies



class VacansyLoadAbs(ABC):
    def __init__(self):
        pass


    @abstractmethod
    def json_load(self, info: list):
        pass