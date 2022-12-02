# Кузнецов Денис ИУ7-23Б
# Лабораторная работа номер 5

import pygame, sys
from pygame.locals import *

# Константы

FPS = 30
WINDOWWIDTH = 400 
WINDOWHEIGHT = 300
LINETHICKNESS = 10
PADDLESIZE = 50
PADDLEOFFSET = 20
WHITE = (255,255,255)

# Зарисовка поля игры

def drawArena():
    DISPLAYSURF.fill((0,0,0))
    pygame.draw.rect(DISPLAYSURF, WHITE, ((0,0),(WINDOWWIDTH,WINDOWHEIGHT)), LINETHICKNESS*2)
    pygame.draw.line(DISPLAYSURF, WHITE, ((WINDOWWIDTH // 2),0),((WINDOWWIDTH // 2),WINDOWHEIGHT), (LINETHICKNESS // 4))

# Зарисовка прямоугольников

def drawPaddle(paddle):
    if paddle.bottom > WINDOWHEIGHT - LINETHICKNESS:
        paddle.bottom = WINDOWHEIGHT - LINETHICKNESS
    elif paddle.top < LINETHICKNESS:
        paddle.top = LINETHICKNESS
    pygame.draw.rect(DISPLAYSURF, WHITE, paddle)

# Вычисление новых координат мячика

def moveBall(ball, ballDirX, ballDirY):
    ball.x += ballDirX
    ball.y += ballDirY
    return ball

# Столкновение с краем поля

def checkEdgeCollision(ball, ballDirX, ballDirY):
    if ball.top == (LINETHICKNESS) or ball.bottom == (WINDOWHEIGHT - LINETHICKNESS):
        ballDirY = ballDirY * -1
    elif ball.left == (LINETHICKNESS) or ball.right == (WINDOWWIDTH - LINETHICKNESS):
        ballDirX = ballDirX * -1
    return ballDirX, ballDirY

# Проверка на то, что мячик был отбит

def checkHitBall(ball, paddle1, paddle2, ballDirX):
    if ballDirX == -5 and paddle1.right == ball.left and paddle1.top < ball.top and paddle1.bottom > ball.bottom:
        return -1
    elif ballDirX == 5 and paddle2.left == ball.right  and paddle2.top < ball.top and paddle2.bottom > ball.bottom:
        return -1
    else: return 1

# Подсчет очков

def checkPointScored(paddle1, ball, score, ballDirX):
    if ball.left == LINETHICKNESS: 
        return 0
    elif ballDirX == -5 and paddle1.right == ball.left and paddle1.top < ball.top and paddle1.bottom > ball.bottom:
        score += 1
        return score
    elif ball.right == WINDOWWIDTH - LINETHICKNESS:
        score += 5
        return score
    return score


# Бот, который отбивает мячик

def artificialIntelligence(ball, ballDirX, paddle2):
    if ballDirX == -5:
        if paddle2.centery < (WINDOWHEIGHT / 2):
            paddle2.y += 5
        elif paddle2.centery > (WINDOWHEIGHT / 2):
            paddle2.y -= 5
    elif ballDirX == 5:
        if paddle2.centery < ball.centery:
            paddle2.y += 5
        else:
            paddle2.y -=5
    return paddle2

# Вывод счета

def displayScore(score):
    resultSurf = BASICFONT.render('Score = %s' %(score), True, WHITE)
    resultRect = resultSurf.get_rect()
    resultRect.topleft = (WINDOWWIDTH - 150,25 )
    DISPLAYSURF.blit(resultSurf, resultRect)

pygame.init()
BASICFONTSIZE = 20
BASICFONT = pygame.font.Font('freesansbold.ttf', BASICFONTSIZE)

FPSCLOCK = pygame.time.Clock()
DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH,WINDOWHEIGHT)) 
pygame.display.set_caption('Pinpong')

ballX = WINDOWWIDTH / 2 - LINETHICKNESS / 2
ballY = WINDOWHEIGHT / 2 - LINETHICKNESS / 2
playerOnePosition = (WINDOWHEIGHT - PADDLESIZE) / 2
playerTwoPosition = (WINDOWHEIGHT - PADDLESIZE) / 2
score = 0

ballDirX = -5
ballDirY = -5

paddle1 = pygame.Rect(PADDLEOFFSET,playerOnePosition, LINETHICKNESS,PADDLESIZE)
paddle2 = pygame.Rect(WINDOWWIDTH - PADDLEOFFSET - LINETHICKNESS, playerTwoPosition, LINETHICKNESS,PADDLESIZE)
ball_surf = pygame.image.load("icon.jpg").convert()
ball_surf.set_colorkey((255, 255, 255))
ball_rect = ball_surf.get_rect(center=(200, 150))

drawArena()
drawPaddle(paddle1)
drawPaddle(paddle2)

pygame.mouse.set_visible(0)
x = -3

# Запуск игры

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
                
        elif event.type == MOUSEMOTION:
            mousex, mousey = event.pos
            paddle1.y = mousey

    drawArena()
    drawPaddle(paddle1)
    drawPaddle(paddle2)

    ball_rect = moveBall(ball_rect, ballDirX, ballDirY)
    DISPLAYSURF.blit(pygame.transform.rotate(ball_surf, x), ball_rect)
    x -=3
    ballDirX, ballDirY = checkEdgeCollision(ball_rect, ballDirX, ballDirY)
    score = checkPointScored(paddle1, ball_rect, score, ballDirX)
    ballDirX = ballDirX * checkHitBall(ball_rect, paddle1, paddle2, ballDirX)
    paddle2 = artificialIntelligence (ball_rect, ballDirX, paddle2)

    displayScore(score)

    pygame.display.update()
    FPSCLOCK.tick(FPS)
