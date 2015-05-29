#!/usr/bin/env python
# -*- coding: utf-8 -*-


import pygame
from pygame import *

WIN_WIDTH = 1280 
WIN_HEIGHT = 800 
DISPLAY = (WIN_WIDTH, WIN_HEIGHT) 
BACKGROUND_COLOR = "#004400"


def main():
    pygame.init() # Инициация PyGame, обязательная строчка 
    screen = pygame.display.set_mode(DISPLAY) # Создаем окошко
    #pygame.display.toggle_fullscreen()
    
    pygame.display.set_caption("מריאו") # Пишем в шапку
    background = Surface((WIN_WIDTH,WIN_HEIGHT)) # Создание видимой поверхности
    foreground = Surface((300,200)) # Создание видимой поверхности
                                         # будем использовать как фон
    background.fill(Color(BACKGROUND_COLOR))     # Заливаем поверхность сплошным цветом
    foreground.fill(Color('#aa0000'))     # Заливаем поверхность сплошным цветом
    background_image = pygame.image.load("stena.jpg").convert()

    while True : # Основной цикл программы
        for e in pygame.event.get(): # Обрабатываем события
            if e.type == QUIT:
                raise SystemExit, "QUIT"
        screen.blit(background_image, [0, 0])
        #screen.blit(background, (0,0))      # Каждую итерацию необходимо всё перерисовывать 
        #screen.blit(foreground, (362,200))      # Каждую итерацию необходимо всё перерисовывать 
        pygame.display.update()     # обновление и вывод всех изменений на экран
        

if __name__ == "__main__":
    main()


