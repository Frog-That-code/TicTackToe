import pygame
import random

pygame.init()

black = 0, 0, 0
white = 255, 255, 255
yellow = 50, 168, 123
green = 50, 113, 168

s = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()
running = True
dt = 0

player = 1
shape = 0

rect1 = pygame.Rect(100,100, 200, 200)
rect2 = pygame.Rect(100,300, 200, 200)
rect3 = pygame.Rect(100,500, 200, 200)
rect4 = pygame.Rect(300,100, 200, 200)
rect5 = pygame.Rect(300,300, 200, 200)
rect6 = pygame.Rect(300,500, 200, 200)
rect7 = pygame.Rect(500,100, 200, 200)
rect8 = pygame.Rect(500,300, 200, 200)
rect9 = pygame.Rect(500,500, 200, 200)

rects = [0, 0, 0, 0, 0, 0, 0, 0, 0]

line1 = (100, 300)
line11 = (700, 300)
line2 = (100, 500)
line22 = (700, 500)
line3 = (300, 100)
line33 = (300, 700)
line4 = (500, 100)
line44 = (500, 700)

def init():
    s.fill("grey")
    pygame.draw.rect(s, black, rect1)
    pygame.draw.rect(s, black, rect2)
    pygame.draw.rect(s, black, rect3)
    pygame.draw.rect(s, black, rect4)
    pygame.draw.rect(s, black, rect5)    
    pygame.draw.rect(s, black, rect6)
    pygame.draw.rect(s, black, rect7)
    pygame.draw.rect(s, black, rect8)
    pygame.draw.rect(s, black, rect9)
    pygame.draw.line(s, white, line1, line11)
    pygame.draw.line(s, white, line2, line22)
    pygame.draw.line(s, white, line3, line33)
    pygame.draw.line(s, white, line4, line44)
    pygame.display.flip()

def circle(rectt):
    pygame.draw.circle(s, yellow, rectt.center, 50)

def line(rectt):
    pygame.draw.line(s, green, rectt.topleft, rectt.bottomright, 8)
    pygame.draw.line(s, green, rectt.bottomleft, rectt.topright, 8)

def draw(shape, rect):
    shape(rect)

init()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if player == 1:
                shape = circle
            if player == 2:
                shape = line
            x, y = pygame.mouse.get_pos ()
            if x >= 100 and x <= 299:
                if y in range(100, 299):
                    if rects[0] != 1:
                        draw(shape, rect1)
                        pygame.display.flip()
                        rects[0] = 1
                elif y in range(300, 499):
                    if rects[1] != 1:
                        draw(shape, rect2)
                        pygame.display.flip()
                        rects[1] = 1
                elif y in range(500, 699):
                    if rects[2] != 1:
                        draw(shape, rect3)
                        pygame.display.flip()
                        rects[2] = 1
            if x >= 300 and x <= 499:
                if y in range(100, 299):
                    if rects[3] != 1:
                        draw(shape, rect4)
                        pygame.display.flip()
                        rects[3] = 1
                elif y in range(300, 499):
                    if rects[4] != 1:
                        draw(shape, rect5)
                        pygame.display.flip()
                        rects[4] = 1
                elif y in range(500, 699):
                    if rects[5] != 1:
                        draw(shape, rect6)
                        pygame.display.flip()
                        rects[5] = 1
            if x >= 500 and x <= 700:
                if y in range(100, 299):
                    if rects[6] != 1:
                        draw(shape, rect7)
                        pygame.display.flip()
                        rects[6] = 1
                elif y in range(300, 499):
                    if rects[7] != 1:
                        draw(shape, rect8)
                        pygame.display.flip()
                        rects[7] = 1
                elif y in range(500, 699):
                    if rects[8] != 1:
                        draw(shape, rect9)
                        pygame.display.flip()
                        rects[8] = 1

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 2:
            init()
            rects = [0, 0, 0, 0, 0, 0, 0, 0, 0]

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
            if player == 2:
                player = 1
            elif player == 1:
                player = 2

    dt = clock.tick(60) / 1000

pygame.quit()
