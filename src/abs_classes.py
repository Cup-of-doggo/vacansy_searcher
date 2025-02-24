from abc import ABC, abstractmethod


class BaseClass(ABC):
    def __init__(self):
        pass


class Parser(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def load_vacancies(self):
        pass


class VacansyLoadAbs(ABC):
    def __init__(self):
        pass


    @abstractmethod
    def json_load(self):
        pass