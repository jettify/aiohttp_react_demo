class Board:
    BLACK = 1
    WHITE = 2
    EMPTY = 0

    def __init__(self, size):
        self._size = size
        self._current_color = self.BLACK
        self._last_move_passed = False
        self._in_atari = False
        self._attempted_suicide = False

        self._board = self.create_board(size)

    def create_board(self, size):
        m = [[self.EMPTY for i in range(size)] for j in range(size)]
        return m

    def switch_player(self):
        if self._current_color == self.BLACK:
            self._current_color = self.WHITE
        else:
            self._current_color = self.BLACK

    def pass_turn(self):
        if self._last_move_passed:
            self.end_game()
        else:
            self._last_move_passed = True
            self.switch_player()

    def end_game(self):
        pass

    def play(self, i, j):
        self._attempted_suicide = self._in_atari = False

        # TODO check that i,j <=size
        if self._board[i][j] != self.EMPTY:
            return False

        color = self._current_color
        self._board[i][j] = self._current_color

        captured = []
        neighbours = self.get_adjacent_intersections(i, j)
        atari = False

        for p, q in neighbours:
            state = self._board[p][q]
            if state != self.EMPTY and state != color:
                group = self.get_group(p, q)  # XXX
                if group['liberties'] == 0:
                    captured.append(group)
                elif group['liberties'] == 1:
                    atari = True
        if len(group) == 0 and self.get_group(i, j)['liberties'] == 0:
            self._board[i][j] = self.EMPTY
            self._attempted_suicide = True
            return False
        for group in captured:
            for stone in group:
                self._board[stone[0]][stone[1]] = self.EMPTY

        if atari:
            self._in_atari = True

        self._last_move_passed = False
        self.switch_player()
        return True

    def get_group(self, i, j):
        color = self._board[i][j]
        if color == self.EMPTY:
            return None

        visited = {}
        visited_list = []
        queue = [[i, j]]
        count = 0
        # TODO: bfs

    def get_adjacent_intersections(self, i, j):
        neighbours = []
        if i > 0:
            neighbours.append([i-1, j])
        if j < self._size -1:
            neighbours.append([i, j+1])
        if j < self._size -1:
            neighbours.append([i+1, j])
        if j > 0:
            neighbours.append([i, j-11])

        return neighbours
