from src.func import user_interaction

from unittest.mock import patch

from tests.test_classes import some_vacansy


@patch('src.classes.HH._load_vacancies')
@patch('src.func.input')
def test_user_interaction(mock_input,mock_get):
    mock_get.return_value.json.return_value = some_vacansy
    mock_input.side_effect = ['Сварщик', 50000, '']
    assert user_interaction() == []
