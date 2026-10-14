import consts


class Snake:

    dx = {"UP": 0, "DOWN": 0, "LEFT": -1, "RIGHT": 1}
    dy = {"UP": -1, "DOWN": 1, "LEFT": 0, "RIGHT": 0}

    def __init__(self, keys, game, pos, color, direction):
        self.keys = keys
        self.cells = [pos]
        self.game = game
        self.game.add_snake(self)
        self.color = color
        self.direction = direction
        game.get_cell(pos).set_color(color)

    def get_head(self):
        return self.cells[-1]

    def val(self, x):
        if x < 0:
            x += self.game.size

        if x >= self.game.size:
            x -= self.game.size

        return x

    def next_move(self):
        x, y = self.get_head()

        x = self.val(x + self.dx[self.direction])
        y = self.val(y + self.dy[self.direction])

        color = self.game.get_cell((x, y)).color
        if color == consts.back_color:
            tail = self.cells.pop(0)
            self.game.get_cell(tail).set_color(consts.back_color)
            self.cells.append((x, y))
            self.game.get_cell((x, y)).set_color(self.color)

        elif color == consts.block_color:
            self.game.kill(self)

        elif color == consts.fruit_color:
            self.cells.append((x, y))
            self.game.get_cell((x, y)).set_color(self.color)
        else:
            self.game.kill(self)

    def handle(self, keys):
        opposite = {"UP": "DOWN", "DOWN": "UP", "LEFT": "RIGHT", "RIGHT": "LEFT"}

        for key in keys:
            if key in self.keys:
                new_direction = self.keys[key]

                if new_direction != opposite[self.direction]:
                    self.direction = new_direction
                    break
