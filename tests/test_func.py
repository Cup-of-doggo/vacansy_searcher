from src.func import user_interaction

from unittest.mock import patch



@patch('main.input')
def test_user_interaction(mock_input):
    mock_input.side_effect = ['Python', 10, 'None']
    assert user_interaction() == []
