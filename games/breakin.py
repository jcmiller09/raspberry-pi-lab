import time
import pygame, sys
from pygame.locals import *

from RPLCD import CharLCD
lcd = CharLCD(cols=16, rows=2, pin_rs=37, pin_e=35, pins_data=[33, 31, 29, 23])



pygame.init()

pygame.display.set_caption('Hello World!')

class Player:
    def __init__(self, key, name, score):
        self.key = key
        self.name = name
        self.score = score
        
    def addScore(self):
        self.score += 1

font = pygame.font.Font('freesansbold.ttf', 32)
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)

def msg(text):
    return font.render(text, True, green, blue)
    
def drawScoreBox(player):
    boxText = msg(str(player.name) + ":" + str(player.score))
    boxTextRect = boxText.get_rect()
    #boxTextRect.center = (xPos, yPos)
    #return boxText, boxTextRect
    return boxText

def 
p1 = Player("q", "Frances", 0)
p2 = Player("p", "Daddy", 0)

#scoreboxes = [drawScoreBox(p1, -400, 200), drawScoreBox(p2, 400, -200)]

# image = pygame.image.load("pinkgirl.png")
  
# assigning values to X and Y variable 
X = 1600
Y = 900

display_surface = pygame.display.set_mode((X, Y)) 

text = msg("BEGIN!") 
textRect = text.get_rect()  
textRect.center = (X // 2, Y // 2) 

display_surface.fill(white)
display_surface.blit(text, textRect)
#display_surface.blits(scoreboxes)

while True: # main game loop
    #scoreboxes = [drawScoreBox(p1, -400, 200), drawScoreBox(p2, 400, -200)]
    display_surface.blit(text, textRect)    
    display_surface.blit(drawScoreBox(p1), (-400, 200))  
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                print('q')
                p1.addScore()
                text = msg("oop")
            if event.key == pygame.K_p:
                print('p')
                p2.addScore()
        elif event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.flip()

