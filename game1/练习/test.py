# -*- coding: UTF-8 -*-
# envo1 python3.9
"""
@Author:大王
@File:test.py
@CreateTime:2022/4/30 21:50
"""
import pygame
import sys

screen = pygame.display.set_mode((1000, 1000))
pygame.display.set_caption('sky')
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    screen.fill((0, 0, 255))
    pygame.display.flip()

