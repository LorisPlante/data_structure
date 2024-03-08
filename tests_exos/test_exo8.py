from exos.exo8 import guess_number_game

def test_guess_correctly_first_try(mocker):
    mocker.patch('exo8.random.randint', return_value=42)
    mocker.patch('builtins.input', return_value='42')
    mock_print = mocker.patch('builtins.print')

    guess_number_game(max_attempts=3)
    mock_print.assert_any_call("Bravo! Vous avez trouvé le nombre mystère en 1 tentatives.")

def test_guess_correctly_third_try(mocker):
    mocker.patch('exo8.random.randint', return_value=42)
    mocker.patch('builtins.input', side_effect=['20', '60', '42'])
    mock_print = mocker.patch('builtins.print')

    guess_number_game(max_attempts=3)
    mock_print.assert_any_call("Bravo! Vous avez trouvé le nombre mystère en 3 tentatives.")

def test_fail_to_guess(mocker):
    mocker.patch('exo8.random.randint', return_value=42)
    mocker.patch('builtins.input', side_effect=['20', '60', '80'])
    mock_print = mocker.patch('builtins.print')

    guess_number_game(max_attempts=3)
    mock_print.assert_any_call(f"Désolé, vous avez utilisé toutes vos tentatives. Le nombre était : 42")

def test_input_value_error(mocker):
    mocker.patch('exo8.random.randint', return_value=42)
    mocker.patch('builtins.input', side_effect=['pas un nombre', '42'])
    mock_print = mocker.patch('builtins.print')

    guess_number_game(max_attempts=3)
    mock_print.assert_any_call("Veuillez entrer un nombre valide.")
    mock_print.assert_any_call("Bravo! Vous avez trouvé le nombre mystère en 2 tentatives.")
