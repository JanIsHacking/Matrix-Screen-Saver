from random import *
import numpy as np

from numpy import ndarray

from symbols_library import *


class Symbol:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.name = choice(japanese_symbols)

    def new_name(self):
        self.name = choice(japanese_symbols)


class Trail:
    def __init__(self, x: float, y: float, speed: float, symbols: list, symbol_gap: float):
        self.x = x
        self.y = y
        self.speed = speed
        self.symbols = symbols
        self.symbol_gap = symbol_gap
        self.images = []
        for i in range(len(self.symbols)):
            symbols[i].x = self.x
            symbols[i].y = self.y - i * symbol_gap

    def move(self):
        for s in self.symbols:
            s.y += self.speed

    def render(self, font):
        self.images = []
        for s in self.symbols:
            self.images.append(font.render(s.name, True, s.color))

    def reset(self, free_positions: ndarray):
        self.y = - 10
        taken_position = int(self.x / self.symbol_gap)
        free_positions = np.append(free_positions, taken_position)
        random_position = randint(0, len(free_positions) - 1)
        for i in range(len(self.symbols)):
            self.symbols[i].x = self.symbol_gap * free_positions[random_position]
            self.symbols[i].y = self.y - i * self.symbol_gap
        free_positions = np.delete(free_positions, random_position)
        return free_positions

