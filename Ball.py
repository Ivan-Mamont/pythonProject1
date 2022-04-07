
import pygame
from pygame.draw import *
from random import randint
pygame.init()
from math import sqrt

FPS = 1
screen = pygame.display.set_mode((1200, 900))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255,  255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]
global schet1
global schet2
schet1 = 0
schet2 = 0


def new_ball():
    """Рисуем новый шарик"""
    global x, y, r
    x = randint(100, 1100)
    y = randint(100, 800)
    r = randint(10, 100)
    color = COLORS[randint(0, 5)]
    circle(screen, color, (x, y), r)

def new_balloon():
    """Рисуем новый воздушный шарик"""
    global x_b, y_b, r_b
    x_b = randint(100, 1100)
    y_b = randint(100, 800)
    r_b = randint(10, 100)
    color2 = COLORS[randint(0, 5)]
    circle(screen, color2, (x_b, y_b), r_b)


def click(event):
    global schet1
    global schet2
    a, b = event.pos
    popal = sqrt((x - a)**2 + (y - b)**2)
    if popal <= r:
        circle(screen, RED, event.pos, 10)
        schet1 += 1
    popal2 = sqrt((x_b - a)**2 + (y_b - b)**2)
    if popal2 <= r_b:
        circle(screen, YELLOW, event.pos, 20)
        schet2 += 1


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                click(event)
                pygame.display.update()


    new_ball()
    new_balloon()
    pygame.display.update()
    screen.fill(BLACK)


print("Попаданий в круг: ", schet1)
print("Попаданий в шарик: ", schet2)
pygame.quit()




