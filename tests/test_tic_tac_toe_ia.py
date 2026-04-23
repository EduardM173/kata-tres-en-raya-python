import pytest
from src.tic_tac_toe import TicTacToe


def test_debe_colocar_una_pieza_en_una_posicion_valida_del_tablero():
    game = TicTacToe()

    player = game.play(0, 0)

    assert player == "X"
    assert game.board()[0][0] == "X"


def test_debe_lanzar_excepcion_cuando_x_esta_fuera_del_rango_por_debajo():
    game = TicTacToe()

    with pytest.raises(ValueError, match="La coordenada X está fuera del tablero"):
        game.play(-1, 0)


def test_debe_lanzar_excepcion_cuando_x_esta_fuera_del_rango_por_encima():
    game = TicTacToe()

    with pytest.raises(ValueError, match="La coordenada X está fuera del tablero"):
        game.play(3, 0)


def test_debe_lanzar_excepcion_cuando_y_esta_fuera_del_rango_por_debajo():
    game = TicTacToe()

    with pytest.raises(ValueError, match="La coordenada Y está fuera del tablero"):
        game.play(0, -1)


def test_debe_lanzar_excepcion_cuando_y_esta_fuera_del_rango_por_encima():
    game = TicTacToe()

    with pytest.raises(ValueError, match="La coordenada Y está fuera del tablero"):
        game.play(0, 3)


def test_debe_lanzar_excepcion_cuando_la_posicion_ya_esta_ocupada():
    game = TicTacToe()
    game.play(1, 1)

    with pytest.raises(ValueError, match="La posición ya está ocupada"):
        game.play(1, 1)


def test_el_primer_turno_debe_ser_de_x():
    game = TicTacToe()

    assert game.next_player() == "X"


def test_despues_de_que_juega_x_el_siguiente_turno_debe_ser_mas():
    game = TicTacToe()
    game.play(0, 0)

    assert game.next_player() == "+"


def test_despues_de_que_juega_mas_el_siguiente_turno_debe_ser_x():
    game = TicTacToe()
    game.play(0, 0)  # X
    game.play(1, 0)  # +

    assert game.next_player() == "X"


def test_no_debe_haber_ganador_si_no_se_cumple_una_condicion_de_victoria():
    game = TicTacToe()
    game.play(0, 0)  # X
    game.play(1, 0)  # +
    game.play(2, 2)  # X

    assert game.winner() is None


def test_x_debe_ganar_cuando_completa_una_linea_horizontal():
    game = TicTacToe()
    game.play(0, 0)  # X
    game.play(0, 1)  # +
    game.play(1, 0)  # X
    game.play(1, 1)  # +
    game.play(2, 0)  # X

    assert game.winner() == "X"


def test_x_debe_ganar_cuando_completa_una_linea_vertical():
    game = TicTacToe()
    game.play(0, 0)  # X
    game.play(1, 0)  # +
    game.play(0, 1)  # X
    game.play(1, 1)  # +
    game.play(0, 2)  # X

    assert game.winner() == "X"


def test_x_debe_ganar_cuando_completa_una_linea_diagonal_principal():
    game = TicTacToe()
    game.play(0, 0)  # X
    game.play(1, 0)  # +
    game.play(1, 1)  # X
    game.play(2, 0)  # +
    game.play(2, 2)  # X

    assert game.winner() == "X"


def test_mas_debe_ganar_cuando_completa_una_linea_diagonal_secundaria():
    game = TicTacToe()
    game.play(0, 0)  # X
    game.play(2, 0)  # +
    game.play(1, 0)  # X
    game.play(1, 1)  # +
    game.play(2, 2)  # X
    game.play(0, 2)  # +

    assert game.winner() == "+"