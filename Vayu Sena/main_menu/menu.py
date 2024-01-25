import pygame
from pygame import mixer
pygame.init()

x_axis = 1100
y_axis = 700
both_axis = (x_axis, y_axis)
screen = pygame.display.set_mode(both_axis)

half_x = 0
half_y = 0
both_half = (half_x, half_y)

logo = pygame.image.load('logo.png')
pygame.display.set_caption('Vayu Sena: New Alliance')
pygame.display.set_icon(logo)

mixer.music.load('bgm.mp3')
mixer.music.play(-1)

menu = pygame.image.load('menu.png')
screen.blit(menu, (both_half))
pygame.display.update()

running = True
while running:
     for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                running = False
