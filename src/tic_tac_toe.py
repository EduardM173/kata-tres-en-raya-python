class TicTacToe:
    def __init__(self):
        self._board = [[None for _ in range(3)] for _ in range(3)]
        self._last_player = None

    def play(self, x: int, y: int) -> str:
        """
        Coloca la pieza del jugador actual en la posición (x, y).

        x -> columna
        y -> fila
        """

        if x < 0 or x > 2:
            raise ValueError("La coordenada X está fuera del tablero")

        if y < 0 or y > 2:
            raise ValueError("La coordenada Y está fuera del tablero")

        if self._board[y][x] is not None:
            raise ValueError("La posición ya está ocupada")

        player = self.next_player()
        self._board[y][x] = player
        self._last_player = player
        return player

    def next_player(self) -> str:
        """
        Devuelve qué jugador debe jugar después.
        Primer turno: X
        Luego alterna entre X y +
        """
        if self._last_player is None:
            return "X"

        if self._last_player == "X":
            return "+"

        return "X"

    def winner(self):
        """
        Devuelve:
        - 'X' si X ganó
        - '+' si + ganó
        - None si no hay ganador
        """
        lines = []

        # Filas
        for row in self._board:
            lines.append(row)

        # Columnas
        for col in range(3):
            lines.append([self._board[row][col] for row in range(3)])

        # Diagonales
        lines.append([self._board[0][0], self._board[1][1], self._board[2][2]])
        lines.append([self._board[0][2], self._board[1][1], self._board[2][0]])

        for line in lines:
            if line[0] is not None and line[0] == line[1] == line[2]:
                return line[0]

        return None

    def board(self):
        """
        Devuelve una copia del tablero.
        """
        return [row[:] for row in self._board]