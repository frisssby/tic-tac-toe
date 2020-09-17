import random


class Game:
    player = 1
    filled_cells = 0
    last_move = [-1, -1]

    def __init__(self, data):
        self.field_size = data[0]
        self.field = [['.' for j in range(self.field_size)] for i in range(self.field_size)]
        self.line_needed = data[1]
        self.mode = data[2]

    def print_field(self):
        for i in range(self.field_size):
            for j in range(self.field_size):
                print(self.field[i][j], end=' ')
            print()
        print()

    def is_terminal(self):
        # запускаем обход в 4 направлеиях из клетки, в которой был сделан последний ход и пытаемся найти
        # k подряд идущих соответствующих символов
        # возвращаем 1, если такая последовательность символов найдена или все поле заполнено
        if self.filled_cells == self.field_size * self.field_size:
            self.print_field()
            return 1
        x = self.last_move[0]
        y = self.last_move[1]
        if x == -1 or y == -1:
            return 0
        max_line = 1
        sign = self.field[x][y]
        # вертикально
        cur_line = 1
        i = x
        j = y + 1
        while j < self.field_size and self.field[i][j] == sign:
            cur_line += 1
            j += 1
        j = y - 1
        while j >= 0 and self.field[i][j] == sign:
            cur_line += 1
            j -= 1
        max_line = max(max_line, cur_line)
        # горизонтально
        cur_line = 1
        i = x + 1
        j = y
        while i < self.field_size and self.field[i][j] == sign:
            cur_line += 1
            i += 1
        i = x - 1
        while i >= 0 and self.field[i][j] == sign:
            cur_line += 1
            i -= 1
        max_line = max(max_line, cur_line)
        # по диагонали параллельно главной
        cur_line = 1
        i = x + 1
        j = y + 1
        while i < self.field_size and j < self.field_size and self.field[i][j] == sign:
            cur_line += 1
            i += 1
            j += 1
        i = x - 1
        j = y - 1
        while i >= 0 and j >= 0 and self.field[i][j] == sign:
            cur_line += 1
            i -= 1
            j -= 1
        max_line = max(max_line, cur_line)
        # по диагонали параллельно побочной
        cur_line = 1
        i = x - 1
        j = y + 1
        while i >= 0 and j < self.field_size and self.field[i][j] == sign:
            cur_line += 1
            i -= 1
            j += 1
        i = x + 1
        j = y - 1
        while i < self.field_size and j >= 0 and self.field[i][j] == sign:
            cur_line += 1
            i += 1
            j -= 1
        max_line = max(max_line, cur_line)

        if max_line < self.line_needed:
            return 0
        else:
            self.print_field()
            return 1

    def rec(self, x, y, arr, used, depth):
        depth += 1
        used[x][y] = 1
        if len(arr) > 0 and depth > self.field_size // 3:
            return
        for i in range(-1, 2):
            for j in range(-1, 2):
                if x + i >= 0 and x + i < self.field_size and\
                        y + j >= 0 and y + j < self.field_size and \
                        used[x + i][y + j] == 0:
                    if self.field[x + i][y + j] == '.':
                        arr.append([x + i, y + j])
                    self.rec(x + i, y + j, arr, used, depth)

    def generate_move(self):
        # будем рекурсивно идти от последнего сделанного противником хода и добавлять в список
        # все возможные ходы, а затем с помощью random выбирем случайный из добавленных ходов
        x = self.last_move[0]
        y = self.last_move[1]
        list_of_moves = []
        depth = 0
        used = [[0 for j in range(self.field_size)] for i in range(self.field_size)]
        self.rec(x, y, list_of_moves, used, depth)
        move = random.choice(list_of_moves)
        return move

    def user_move(self):
        while True:
            print('Введи координаты клетки для хода: номер строки и номер столбца, '
                  'записанные через пробел.')
            try:
                move = list(map(lambda x: x - 1, list(map(int, input().split()))))
            except ValueError:
                print('Неверный формат')
            else:
                if len(move) != 2:
                    print('Неверный формат')
                elif move[0] < 0 or move[1] < 0 or move[1] > self.field_size - 1 \
                        or move[1] > self.field_size - 1:
                    print('Некорректные координаты')
                elif self.field[move[0]][move[1]] != '.':
                    print('Эта клетка уже занята')
                else:
                    return move

    def next_move(self):
        self.player = (self.player + 1) % 2
        if self.mode == 1:
            move = self.user_move()
        elif self.mode == 2:
            if self.player == 1:
                move = self.generate_move()
            else:
                move = self.user_move()
        else:
            move = self.generate_move()
        x = move[0]
        y = move[1]
        if self.player == 0:
            self.field[x][y] = 'x'
        else:
            self.field[x][y] = 'o'
        self.filled_cells += 1
        self.last_move = move
