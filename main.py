import pygame
from pygame.locals import *
import turtle

SCREEN_WIDTH=670
SCREEN_HEIGHT=670
QZ_WH=44
QZ_ST=27
class board:
    def init(self):
        self.board=[[0 for i in range(15)]for j in range(15)]
    def clear(self):
        for i in range(15):
            for j in range(15):
                self.board[i][j]=0
    def putch(self,pos,nowplayer):
        if (self.board[pos[0]][pos[1]]!=0):
            return -1
        else:
            self.board[pos[0]][pos[1]]=nowplayer
    def checkwin(self,nowplayer):
        most=0
        for i in range(15):
            for j in range(15):
                if (self.board[i][j]==nowplayer):
                    most=most+1
                    if (most==5):
                        return 1
                else:
                    most=0
            most=0
        for i in range(15):
            for j in range(15):
                if (self.board[j][i]==nowplayer):
                    most=most+1
                    if (most==5):
                        return 1
                else:
                    most=0
            most=0
        for i in range(11):
            j=0
            k=i
            while (j<15 and k<15):
                if (self.board[j][k]==nowplayer):
                    most=most+1
                    if (most==5):
                        return 1
                else:
                    most=0
                j=j+1
                k=k+1
            most=0
        for i in range(11):
            j=i
            k=0
            while (j<15 and k<15):
                if (self.board[j][k]==nowplayer):
                    most=most+1
                    if (most==5):
                        return 1
                else:
                    most=0
                j=j+1
                k=k+1
            most=0
        for i in range(4,15):
            j=0
            k=i
            while (j<15 and k>=0):
                if (self.board[j][k]==nowplayer):
                    most=most+1
                    if (most==5):
                        return 1
                else:
                    most=0
                j=j+1
                k=k-1
            most=0
        for i in range(11):
            j=i
            k=14
            while (j<15 and k>=0):
                if (self.board[j][k]==nowplayer):
                    most=most+1
                    if (most==5):
                        return 1
                else:
                    most=0
                j=j+1
                k=k-1
            most=0
        return 0
            
def getpos(x,y):
    return (x*QZ_WH+QZ_ST,y*QZ_WH+QZ_ST)
def draw(pos,num):
    if (num==1):
        pygame.draw.circle(screen,(0,0,0),pos,16)
    else:
        pygame.draw.circle(screen,(255,255,255),pos,16)
def printf(s):
    font=pygame.font.Font('arial.ttf',32)
    text=font.render(s, True, (0,0,0))
    k=text.get_rect()
    k.center=(335,100)
    screen.blit(text,k)
    pygame.display.update()
pygame.init()   
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
pygame.display.set_caption("five")
background=pygame.image.load("board.jpg")
screen.blit(background,(0,0))
nowplayer=1
Board=board()
Board.init()
begin=0
ready="Press C to begin"
win=['','Black Win and','White Win and']
printf(ready)
while True:
    pygame.display.update()
    if begin==0:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN and event.key==pygame.K_c:
                begin=1
                nowplayer=1
                Board.clear()
                screen.fill((255,255,255))
                screen.blit(background,(0,0))
                mode=0
                break
    else:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos=event.pos
                nowid=(int(round((pos[0]-QZ_ST)/QZ_WH)),int(round((pos[1]-QZ_ST)/QZ_WH)))
                if Board.board[nowid[0]][nowid[1]]!=0:
                    continue
                draw(getpos(nowid[0],nowid[1]),nowplayer)
                Board.board[nowid[0]][nowid[1]]=nowplayer;
                if (Board.checkwin(nowplayer)==1):
                    printf(win[nowplayer]+' '+ready)
                    begin=0
                nowplayer=3-nowplayer
