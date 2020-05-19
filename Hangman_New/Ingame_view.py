import sys
import pygame
from pygame.locals import QUIT, Rect,\
    MOUSEBUTTONDOWN, MOUSEBUTTONUP

pygame.init()
SURFACE = pygame.display.set_mode((900, 600))
FPSCLOCK = pygame.time.Clock()

def main():
    mouseposx : int = 0
    mouseposy : int = 0
    sysfont = pygame.font.SysFont(None, 46)
    message = [[0]*4 for i in range(7)]
    message_rect = [[0]*4 for i in range(7)]
    answermessage = []

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

        if (55 <= mouseposx <= 110) and (155 <= mouseposy <= 210):
            answermessage.append('A')
        elif (155 <= mouseposx <= 210) and (155 <= mouseposy <= 210):
            answermessage.append('B')

        for i in range(0, len(answermessage)):
            answermessaged = sysfont.render(answermessage[i], True, (0,0,255))
            answermessaged_rect = answermessaged.get_rect()
            answermessaged_rect.center = (40, 60)
            SURFACE.blit(answermessaged, answermessaged_rect)

        pygame.display.update()
        FPSCLOCK.tick(1)

if __name__ == '__main__':
    main()