import numpy as np
import pygame

from utils import *
from config import *


# Initialising the game
pygame.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
width, height = pygame.display.get_surface().get_size()
background = BLACK
screen.fill(background)

# Making font settings
font = pygame.font.Font("MochiyPopOne-Regular.ttf", font_size)

# Creating and rendering the trails
free_x_positions = np.arange(int(width / symbol_gap))
trails = []
for i in range(NUMBER_OF_TRAILS):
    trail_symbols = []
    x_position = randint(0, len(free_x_positions) - 1)
    x = free_x_positions[x_position] * symbol_gap
    free_x_positions = np.delete(free_x_positions, x_position)
    y = - randint(10, height + 10)
    speed = 8 + 8 * random()
    for j in range(randint(LENGTH_LOW, LENGTH_HIGH)):
        if j == 0:
            if random() > 0.4:
                trail_symbols.append(Symbol(0, 0, LIGHT_GREEN))
            else:
                trail_symbols.append(Symbol(0, 0, GREEN))
        else:
            trail_symbols.append(Symbol(0, 0, GREEN))
    trail = Trail(x, y, speed, trail_symbols, symbol_gap)
    trail.render(font)
    trails.append(trail)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    screen.fill(background)

    # Moving the trails downwards
    for trail in trails:
        if trail.symbols[len(trail.symbols) - 1].y >= height + 10:
            free_x_positions = trail.reset(free_x_positions)
        else:
            trail.move()
        for symbol in trail.symbols:
            if random() > 0.997:
                symbol.new_name()

    # Displaying the trails
    for trail in trails:
        trail.render(font)
        for i in range(len(trail.symbols)):
            screen.blit(trail.images[i], (trail.symbols[i].x, trail.symbols[i].y))

    pygame.display.update()
