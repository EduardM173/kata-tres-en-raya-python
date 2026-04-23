import pytest
from src.tic_tac_toe import TicTacToe


def test_primer_turno_es_x():
    game = TicTacToe()
    assert game.next_player() == "X"


def test_no_deja_jugar_fuera_del_tablero():
    game = TicTacToe()

    with pytest.raises(ValueError):
        game.play(-1, 0)

    with pytest.raises(ValueError):
        game.play(0, 3)


def test_no_deja_jugar_en_una_posicion_ocupada():
    game = TicTacToe()
    game.play(1, 1)

    with pytest.raises(ValueError):
        game.play(1, 1)


def test_cambia_turno_entre_x_y_mas():
    game = TicTacToe()

    game.play(0, 0)  
    assert game.next_player() == "+"

    game.play(1, 0)  
    assert game.next_player() == "X"


def test_no_hay_ganador_si_no_se_completa_linea():
    game = TicTacToe()
    game.play(0, 0)  
    game.play(1, 0)  
    game.play(2, 2)  

    assert game.winner() is None


def test_gana_por_fila():
    game = TicTacToe()
    game.play(0, 0)  
    game.play(0, 1)  
    game.play(1, 0)  
    game.play(1, 1)  
    game.play(2, 0)  

    assert game.winner() == "X"


def test_gana_por_columna():
    game = TicTacToe()
    game.play(0, 0)  
    game.play(1, 0)  
    game.play(0, 1)  
    game.play(1, 1)  
    game.play(0, 2)  

    assert game.winner() == "X"


def test_gana_por_diagonal():
    game = TicTacToe()
    game.play(0, 0)  
    game.play(1, 0)  
    game.play(1, 1)  
    game.play(2, 0)  
    game.play(2, 2)  

    assert game.winner() == "X"