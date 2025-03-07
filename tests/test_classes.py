from src.classes import Vacansy, VacansyLoadJson, HH

some_vacansy = Vacansy('Сварщик', 'htttp/tipo_ssilka/chto_to.ru',50000,'Варить металл')
other_vacansy = Vacansy('Грузчик','htttp/tipo_ssilka/chto_to.ru',60000,'Грузить металл')

def test_Vacansy_init():
    assert some_vacansy._name == "Сварщик"
    assert some_vacansy._link == "htttp/tipo_ssilka/chto_to.ru"
    assert some_vacansy.salary() == 50000
    assert some_vacansy._description == 'Варить металл'


def test_Vacansy_salary_comparison():
    assert some_vacansy.salary() < other_vacansy.salary() == 60000


def test_Vacansy_load_json():
    assert VacansyLoadJson(Vacansy).json_load(['test_text']) == None
    assert VacansyLoadJson(Vacansy).file_read('json_file') == None
    assert VacansyLoadJson(Vacansy).information_delete('json_file') == None
    assert VacansyLoadJson(Vacansy).file_delete('json_file') == None
