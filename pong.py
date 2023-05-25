
#Module
import pygame as game
from paddle import Paddle
from ball import Ball

#Initializing pygame
game.init()

#Konstanter
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

#Defining the display
display = game.display.set_mode([700, 500])
game.display.set_caption("Pong")

#Paddle A
paddleA = Paddle(WHITE, 10, 100)
paddleA.rect.x = 20
paddleA.rect.y = 200

#Paddle B
paddleB = Paddle(WHITE, 10, 100)
paddleB.rect.x = 670
paddleB.rect.y = 200

#Ball
ball = Ball(WHITE, 10, 10)

#All Sprites
allSprites_list = game.sprite.Group()
allSprites_list.add(paddleA)
allSprites_list.add(paddleB)
allSprites_list.add(ball)

#Player scores
scoreA = 0
scoreB = 0

clock = game.time.Clock()

running = True
while(running):
    for event in game.event.get():
        if(event.type == game.QUIT):
            running = False

    #Defining the display
    display.fill(BLACK)
    game.draw.line(display, WHITE, [349, 0], [349, 500], 5)
    
    #Moving the paddles
    keys = game.key.get_pressed()
    if(keys[game.K_w]):
        paddleA.moveUp(5)
    if(keys[game.K_s]):
        paddleA.moveDown(5)
    if(keys[game.K_UP]):
        paddleB.moveUp(5)
    if(keys[game.K_DOWN]):
        paddleB.moveDown(5)

    #Ball logic
    if(keys[game.K_SPACE]):
        #Ball
        ball.rect.x = 345
        ball.rect.y = 195
        while(True):
            if(ball.rect.x>=690):
                scoreA += 1
                break
            if(ball.rect.x<=0):
                scoreB += 1
                break
            if(ball.rect.y>490):
                ball.velocity[1] = -ball.velocity[1]
            if(ball.rect.y<0):
                ball.velocity[1] = -ball.velocity[1]
        
    #Detecting collision
    if(game.sprite.collide_mask(ball, paddleA) or game.sprite.collide_mask(ball, paddleB)):
        ball.collision()

    #Updating Sprites
    allSprites_list.update()
    allSprites_list.draw(display)

    #Updating Player Scores
    font = game.font.Font(None, 74)
    text = font.render(str(scoreA), 1, WHITE)
    display.blit(text, (250, 10)) 
    text = font.render(str(scoreB), 1, WHITE)
    display.blit(text, (420, 10)) 

    #Updating the display
    game.display.flip()

    #Frames per second (60 fps)
    clock.tick(60)

game.quit()