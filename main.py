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
        self.x=0
        self.y=0
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

class ai:
    global inf
    inf=1000000
    global PosValue
    PosValue =\
        [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
            [0, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 0],
            [0, 1, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 1, 0],
            [0, 1, 2, 3, 4, 4, 4, 4, 4, 4, 4, 3, 2, 1, 0],
            [0, 1, 2, 3, 4, 5, 5, 5, 5, 5, 4, 3, 2, 1, 0],
            [0, 1, 2, 3, 4, 5, 6, 6, 6, 5, 4, 3, 2, 1, 0],
            [0, 1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 3, 2, 1, 0],
            [0, 1, 2, 3, 4, 5, 6, 6, 6, 5, 4, 3, 2, 1, 0],
            [0, 1, 2, 3, 4, 5, 5, 5, 5, 5, 4, 3, 2, 1, 0],
            [0, 1, 2, 3, 4, 4, 4, 4, 4, 4, 4, 3, 2, 1, 0],
            [0, 1, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 1, 0],
            [0, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 0],
            [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        ]

    def hasne(self, x, y):
        if x-3 > 0:
            i = x-3
        else:
            i = 0
        while i <= x+3 and i < 15:
            if y-3 > 0:
                j = y-3
            else:
                j = 0    
            while j <= y+3 and j < 15:
                if Board.board[i][j] != 0:
                    return True
                j += 1
            i += 1
        return False
    def scoretable(self, number, empty1):
        if number >= 5:
            return 100000
        elif number == 4:
            if empty1 == 2:
                return 10000
            elif empty1 == 1:
                return 1000
        elif number == 3:
            if empty1 == 2:
                return 1000
            elif empty1 == 1:
                return 100
        elif number == 2:
            if empty1 == 2:
                return 100
            elif empty1 == 1:
                return 10
        elif number == 1 and empty1 == 2:
            return 10
        return 0
    def countscore(self,lis, turn):
        scoretmp = 0
        length = len(lis)
        empty1 = 0
        number = 0
        if lis[0] == 0:
            empty1 += 1
        elif lis[0] == turn:
            number += 1
        for i in range(1,length):
            if lis[i] == turn:
                number += 1
            elif lis[i] == 0:
                if number == 0:
                    empty1 = 1
                else:
                    scoretmp += self.scoretable( number, empty1+1)
                    empty1 = 1
                    number = 0
            else:
                scoretmp += self.scoretable( number, empty1+1)
                empty1 = 0
                number = 0
            i += 1
        scoretmp += self.scoretable( number, empty1)
        return scoretmp
    def evaluate(self, Board, color):
        scorecomputer = 0
        scorehumber = 0
        for i in range(15):  # 1
            ll = []
            for j in range(15):
                ll.append(Board.board[i][j])
            scorecomputer += self.countscore(ll, color)
            scorehumber += self.countscore(ll, 3-color)
            ll.clear()
        for j in range(15):  # 2
            ll = []
            for i in range(15):
                ll.append(Board.board[i][j])
            scorecomputer += self.countscore(ll, color)
            scorehumber += self.countscore(ll, 3-color)
            ll.clear()
        for i in range(15):  # 3
            ll = []
            x = i
            y = 0
            while y < 15 and x < 15:
                ll.append(Board.board[y][x])
                y += 1
                x += 1
            scorecomputer += self.countscore(ll, color)
            scorehumber += self.countscore(ll, 3-color)
            ll.clear()
        for j in range(15):  # 4
            ll = []
            x = 0
            y = j
            while y < 15 and x < 15:
                ll.append(Board.board[y][x])
                x += 1
                y += 1
            scorecomputer += self.countscore(ll, color)
            scorehumber += self.countscore(ll, 3-color)
            ll.clear()
        for i in range(15):  # 5
            ll = []
            x = 0
            y = i
            while y >= 0 and x < 15:
                ll.append(Board.board[y][x])
                x += 1
                y -= 1
            scorecomputer += self.countscore(ll, color)
            scorehumber += self.countscore(ll, 3-color)
            ll.clear()
        for j in range(15):  # 6
            ll = []
            x = 14
            y = j
            while x >= 1 and y < 15:
                ll.append(Board.board[x][y])
                x -= 1
                y += 1
            scorecomputer += self.countscore(ll, color)
            scorehumber += self.countscore(ll, 3-color)
            ll.clear()
        for i in range(15):  # 7
            for j in range(15):
                if Board.board[i][j] == color:
                    scorecomputer += PosValue[i][j]
                elif Board.board[i][j] == 3-color:
                    scorehumber += PosValue[i][j]
        return scorecomputer - scorehumber
    def alphabeta(self, Board, depth, alpha, beta, player):
        if depth == 0:
            return self.evaluate(Board, player)
        for i in range(15):
            for j in range(15):
                if Board.board[i][j] == 0 and self.hasne(i, j):
                    node = []
                    node.append(i)
                    node.append(j)
                    Board.board[node[0]][node[1]]=player
                    val = -self.alphabeta(Board, depth - 1, -beta, -alpha, 3 - player)
                    Board.board[node[0]][node[1]]=0
                    if val >= beta:
                        return beta
                    if val > alpha:
                        if depth == 2:
                            Board.x = i
                            Board.y = j
                        alpha = val
        return alpha
    def serchGoodmove(self,Board,player):
        a=self.alphabeta(Board, 2,-inf,inf,player)
            
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
AI=ai()
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
            if event.type == pygame.KEYDOWN and event.key==pygame.K_b:
                begin=1
                nowplayer=1
                Board.clear()
                screen.fill((255,255,255))
                screen.blit(background,(0,0))
                mode=1
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
                    break
                nowplayer=3-nowplayer
                if (mode!=0):
                    AI.serchGoodmove(Board,nowplayer)
                    draw(getpos(Board.x,Board.y),nowplayer)
                    Board.board[Board.x][Board.y]=nowplayer
                    if (Board.checkwin(nowplayer)==1):
                        printf(win[nowplayer]+' '+ready)
                        begin=0
                        break
                    nowplayer=3-nowplayer
