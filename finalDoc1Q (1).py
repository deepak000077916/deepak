#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install pygame


# In[1]:


import pygame
import time
import random

snakeSpeed = 15

# Window size
windowX = 720
windowY = 480

# defining colors
blackColor = pygame.Color(0, 0, 0)
whiteColor = pygame.Color(255, 255, 255)
redColor = pygame.Color(255, 0, 0)
greenColor = pygame.Color(0, 255, 0)
blueColor = pygame.Color(0, 0, 255)

# Initialising pygames
pygame.init()

# Initialise game windows
pygame.display.set_caption('Snake Game')
gameWidow = pygame.display.set_mode((windowX, windowY))

# FramePerSecound (frames per second) controllers
FramePerSecound = pygame.time.Clock()

# defining snake default positions
SnakesPosition = [100, 50]

# defining first 4 blocks of snake bodys
snake_body= [[100, 50],
            [90, 50],
            [80, 50],
            [70, 50]
            ]
# fruit position
fruitPosition = [random.randrange(1, (windowX//10)) * 10,
                random.randrange(1, (windowY//10)) * 10]

fruitSpawn = True

# setting default snake direction towardss
# right
direction = 'RIGHT'
changesTo = direction

# initial score
score = 0

# displaying Score functions
def show_score(choice, color, font, size):

    # creating font object scoreFonts
    scoreFont = pygame.font.SysFont(font, size)
    
    # create the display surface objects
    # scoreSurface
    scoreSurface = scoreFont.render('Score : ' + str(score), True, color)
    
    # create a rectangular object for the texts
    # surface objects
    scoreRect = scoreSurface.get_rect()
    
    # displaying texts
    gameWidow.blit(scoreSurface, scoreRect)

# game over function
def game_over():

    # creating font object myFont
    myFont = pygame.font.SysFont('times new roman', 50)
    
    # creating a text surface on which text
    # will be drawn
    gameOverSurface = myFont.render(
        'Your Score is : ' + str(score), True, redColor)
    
    # create a rectangular object for the texts
    # surface object
    game_over_rect = gameOverSurface.get_rect()
    
    # setting position of the texts
    game_over_rect.midtop = (windowX/2, windowY/4)
    
    # blit will draw the text on screens
    gameWidow.blit(gameOverSurface, game_over_rect)
    pygame.display.flip()
    
    # after 2 seconds we will quit the programs
    time.sleep(2)
    
    # deactivating pygame librarys
    pygame.quit()
    
    # quit the programs
    quit()


# Main Functions
while True:
    
    # handling key eventss
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                changesTo = 'UP'
            if event.key == pygame.K_DOWN:
                changesTo = 'DOWN'
            if event.key == pygame.K_LEFT:
                changesTo = 'LEFT'
            if event.key == pygame.K_RIGHT:
                changesTo = 'RIGHT'

    # If two keys pressed simultaneouslys
    # we don't want snake to move into two
    # directions simultaneouslys
    if changesTo == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if changesTo == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if changesTo == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if changesTo == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'

    # Moving the snakes
    if direction == 'UP':
        SnakesPosition[1] -= 10
    if direction == 'DOWN':
        SnakesPosition[1] += 10
    if direction == 'LEFT':
        SnakesPosition[0] -= 10
    if direction == 'RIGHT':
        SnakesPosition[0] += 10

    # Snake body growing mechanisms
    # if fruits and snakes collide then scoress
    # will be incremented by 10
    snake_body.insert(0, list(SnakesPosition))
    if SnakesPosition[0] == fruitPosition[0] and SnakesPosition[1] == fruitPosition[1]:
        score += 10
        fruitSpawn = False
    else:
        snake_body.pop()
        
    if not fruitSpawn:
        fruitPosition = [random.randrange(1, (windowX//10)) * 10,
                        random.randrange(1, (windowY//10)) * 10]
        
    fruitSpawn = True
    gameWidow.fill(blackColor)
    
    for pos in snake_body:
        pygame.draw.rect(gameWidow, greenColor,
                        pygame.Rect(pos[0], pos[1], 10, 10))
    pygame.draw.rect(gameWidow, whiteColor, pygame.Rect(
        fruitPosition[0], fruitPosition[1], 10, 10))

    # Game Over conditions
    if SnakesPosition[0] < 0 or SnakesPosition[0] > windowX-10:
        game_over()
    if SnakesPosition[1] < 0 or SnakesPosition[1] > windowY-10:
        game_over()

    # Touching the snake body
    for block in snake_body[1:]:
        if SnakesPosition[0] == block[0] and SnakesPosition[1] == block[1]:
            game_over()

    # displaying score continuously
    show_score(1, whiteColor, 'times new roman', 20)

    # Refresh game screen
    pygame.display.update()

    # Frame Per Second /Refresh Rate
    FramePerSecound.tick(snakeSpeed)


# In[ ]:





# In[ ]:




