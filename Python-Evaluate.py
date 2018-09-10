# 石唯妍代码部分
#-------------估值函数----------------#


def scoretable(number, empty1):
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
        elif empty1 == 2:
            return 100
    elif number == 2:
        if empty1 == 2:
            return 100
        elif empty1 == 1:
            return 10
    elif number == 1 and empty1 == 2:
        return 10
    return 0


def countscore(lis, turn):
    scoretmp = 0
    length = len(lis)
    empty1 = 0
    number = 0
    if lis[0] == 0:
        empty1 += 1
    elif lis[0] == turn:
        number += 1
    while i < length:
        if lis[i] == turn:
            number += 1
        elif lis[i] == 0:
            if number == 0:
                empty1 = 1
            else:
                scoretmp += scoretable(number, empty1+1)
                empty1 = 1
                number = 0
        else:
            scoretmp += scoretable(number, empty1+1)
            empty1 = 1
            number = 0
        i += 1
    scoretmp += scoretable(number, empty1)
    return scoretmp


PosValue = []
PosValue =\
    [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
        [0, 0, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 0],
        [0, 0, 1, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 1, 0],
        [0, 0, 1, 2, 3, 4, 4, 4, 4, 4, 4, 4, 3, 2, 1, 0],
        [0, 0, 1, 2, 3, 4, 5, 5, 5, 5, 5, 4, 3, 2, 1, 0],
        [0, 0, 1, 2, 3, 4, 5, 6, 6, 6, 5, 4, 3, 2, 1, 0],
        [0, 0, 1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 3, 2, 1, 0],
        [0, 0, 1, 2, 3, 4, 5, 6, 6, 6, 5, 4, 3, 2, 1, 0],
        [0, 0, 1, 2, 3, 4, 5, 5, 5, 5, 5, 4, 3, 2, 1, 0],
        [0, 0, 1, 2, 3, 4, 4, 4, 4, 4, 4, 4, 3, 2, 1, 0],
        [0, 0, 1, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 1, 0],
        [0, 0, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 0],
        [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]


def evaluate(color):
    scorecomputer = 0
    scorehumber = 0
    for i in range(1, 16):  # 1
        ll = []
        for j in range(1, 16):
            ll.append(Board.board[i][j])
        scorecomputer += countscore(ll, color)
        scorehumber += countscore(ll, 3-color)
        ll.clear()
    for j in range(1, 16):  # 2
        ll = []
        for i in range(1, 16):
            ll.append(Board.board[i][j])
        scorecomputer += countscore(ll, color)
        scorehumber += countscore(ll, 3-color)
        ll.clear()
    for i in range(1, 16):  # 3
        ll = []
        x = i
        y = 1
        while y < 16 and x < 16:
            ll.append(Board.board[y][x])
            y += 1
            x += 1
        scorecomputer += countscore(ll, color)
        scorehumber += countscore(ll, 3-color)
        ll.clear()
    for j in range(1, 16):  # 4
        ll = []
        x = 1
        y = j
        while y < 16 and x < 16:
            ll.append(Board.board[y][x])
            x += 1
            y += 1
        scorecomputer += countscore(ll, color)
        scorehumber += countscore(ll, 3-color)
        ll.claer()
    for i in range(1, 16):  # 5
        ll = []
        x = 1
        y = i
        while y >= 1 and x < 16:
            ll.append(Board.board[y][x])
            x += 1
            y -= 1
        scorecomputer += countscore(ll, color)
        scorehumber += countscore(ll, 3-color)
        ll.clear()
    for j in range(1, 16):  # 6
        ll = []
        x = 15
        y = j
        while x >= 1 and y < 16:
            ll.append(Board.board[y][x])
            x -= 1
            y += 1
        scorecomputer += countscore(ll, color)
        scorehumber += countscore(ll, 3-color)
        ll.clear()
    for i in range(1, 16):  # 7
        for j in range(1, 16):
            if Board.board[i][j] == color:
                scorecomputer += PosValue[i][j]
            elif Board.board[i][j] == 3-color:
                scorehumber += PosValue[i][j]
    return scorecomputer - scorehumber
    
#--------------------------------------------#