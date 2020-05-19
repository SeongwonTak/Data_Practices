import sys
import pygame
from pygame.locals import QUIT, Rect,\
    MOUSEBUTTONDOWN, MOUSEBUTTONUP

pygame.init()
SURFACE = pygame.display.set_mode((900, 600))
FPSCLOCK = pygame.time.Clock()
sysfont = pygame.font.SysFont(None,46)

def button(x,y,w,h,text,mousex,mousey):
    hover = False
    if mousex > x and mousex < x + w:
        if mousey > y and mousey < y + h:
            hover = True
    #usually i would have a if click but since you only getting mouse pos when click it should be fine
    txtobj = sysfont.render(text,True,(0,0,0))
    SURFACE.blit(txtobj, (x,y))
    return hover #return True if mouse clicked on button

def main():
    mouseposx : int = 0
    mouseposy : int = 0
    message = [[0]*4 for i in range(7)]
    message_rect = [[0]*4 for i in range(7)]
    answermessage = []
    alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N",\
                "O","P","Q","R","S","T","U","V","W","X","Y","Z"]

    for i in range(0, 7):
        for j in range(0, 4):
            if not ((i == 5 and j == 3) or (i == 6 and j == 3)):
                message[i][j] = sysfont.render(chr(65+7*j+i), True, (0, 255, 0))
                message_rect[i][j] = message[i][j].get_rect()
                message_rect[i][j].center = (80 + 100 * i, 180 + 100 * j)

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONDOWN:
                mouseposx = event.pos[0]
                mouseposy = event.pos[1]
            elif event.type == MOUSEBUTTONUP:
                mouseposx = 0
                mouseposy = 0

        SURFACE.fill((255, 255, 255))
        for i in range(0, 7):
            for j in range(0, 4):
                if not ((i == 5 and j == 3) or (i == 6 and j == 3)):
                    SURFACE.blit(message[i][j], message_rect[i][j])

        for i in range(0, 7):
            for j in range(0, 4):
                if not ((i == 5 and j == 3) or (i == 6 and j == 3)):
                    pygame.draw.rect(SURFACE, (0, 0, 0), (50+100*i, 150+100*j, 60, 60), 5)

        for i, letter in enumerate(alphabet):  # enumerate gets the letter and its position in the list
            letter_clicked = button(55 + (100 * i), 155, 55, 55, letter, mouseposx, mouseposy)
            if letter_clicked:
                answermessage.append(letter)

        for i in range(0, len(answermessage)):
            answermessaged = sysfont.render(answermessage[i], True, (0,0,255))
            answermessaged_rect = answermessaged.get_rect()
            answermessaged_rect.center = (40 + (i*50), 60) # 50 is a guess
            SURFACE.blit(answermessaged, answermessaged_rect)

        pygame.display.update()
        FPSCLOCK.tick(1)

if __name__ == '__main__':
    main()