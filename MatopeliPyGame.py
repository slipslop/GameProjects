# Learning about classes and objects

import pygame
import random
import math
import tkinter as tk
from tkinter import messagebox





def drawGrid(w, rows, surface):
    sizeBtwn = w // rows

    x = 0
    y = 0
    for l in range(rows):
        x = x + sizeBtwn
        y = y + sizeBtwn

        pygame.draw.line(surface, (255, 255, 255), (x, 0), (x, w))
        pygame.draw.line(surface, (255, 255, 255), (0, y), (w, y))

def redrawWindow(surface):
    global rows, width
    surface.fill((0,0,0))
    drawGrid(width, row, surface)
    pygame.display.update()


def main():
    global width, rows
    width = 500

    rows = 20
    win = pygame.display.set_mode((width, width)) # its square
    s = snake((255,0,0), (10, 10))
    flag = True
    clock = pygame.time.Clock()
    # main loop

    while flag:
        pygame.time.delay(50) # how fast the game is, the lower the faster
        clock.tick(10) # the lower the slower
        redrawWindow(win)