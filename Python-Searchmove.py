# 石唯妍代码部分
#-------------搜索函数------------#

xi
yi

def hasne(x, y):
    if x-3 > 1:
        i = x-3
    else:
        i = 1
    if y-3 > 1:
        j = y-3
    else:
        j = 1
    while i <= x+3 and i < 16:
        while j <= y+3 and j < 16:
            if Board.board[i][j] != 0:
                return True
            j += 1
        i += 1
    return False


def alphabeta(depth, alpha, beta, player):
    if depth == 0:
        return evaluate(player)
    creatMoves(player)
    for i in range(1, 16):
        for j in range(1, 16):
            if Board.board[i][j] == 0 and hasne(i, j):  # 如果这个点没有棋子
                node = []
                node[0] = i
                node[1] = j
                makeMove(node, player)
                val = -alphabeta(depth - 1, -beta, -alpha, 3 - player)
                unMakeMove(node, player)
                if val >= beta:
                    return beta
                if val > alpha:
                    if depth == 2:
                        xi = i
                        yi = j
                    alpha = val
    return alpha

def serchGoodmove(player):
    a=alphabeta(2,-inf,inf,player)
    #xi,yi为落子

def serchGoodmove(player):
    nn.x=xi
    nn.y=yi

#----------搜索函数-------------#
