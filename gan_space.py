import pygame

class Gan():

    def __init__(self, screen):
        " Инициализация пушки"

        self.screen = screen
        self.image = pygame.image.load('imige/gun.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
