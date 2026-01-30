import random
import string


class WordSearchGenerator:

    def __init__(self, words, grid_size=10):
        self.words = [w.upper() for w in words]
        self.grid_size = grid_size
        self.grid = [["" for _ in range(grid_size)] for _ in range(grid_size)]

    def generate(self):
        for word in self.words:
            self.place_word(word)

        self.fill_empty()
        return self.grid

    def place_word(self, word):
        # Solo direcciones horizontal y vertical
        directions = [
            (1, 0),   # Horizontal derecha
            (0, 1),   # Vertical abajo
            (-1, 0),  # Horizontal izquierda
            (0, -1)   # Vertical arriba
        ]
        for _ in range(100):
            dx, dy = random.choice(directions)
            x = random.randint(0, self.grid_size - 1)
            y = random.randint(0, self.grid_size - 1)

            if self.can_place(word, x, y, dx, dy):
                for i, letter in enumerate(word):
                    self.grid[y + i * dy][x + i * dx] = letter
                return True
        return False

    def can_place(self, word, x, y, dx, dy):
        for i, letter in enumerate(word):
            nx = x + i * dx
            ny = y + i * dy
            if nx < 0 or ny < 0 or nx >= self.grid_size or ny >= self.grid_size:
                return False
            if self.grid[ny][nx] not in ("", letter):
                return False
        return True

    def fill_empty(self):
        for y in range(self.grid_size):
            for x in range(self.grid_size):
                if self.grid[y][x] == "":
                    self.grid[y][x] = random.choice(string.ascii_uppercase)
