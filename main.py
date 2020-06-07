import Board as board
import math

def AIMove(b, player):
    bestScore = -math.inf
    finalPosition = -1
    for i in range(3):
        for j in range(3):
            if b.CheckEmptyCell(i,j):
                val = b.GetCellValue(i,j)
                b.SetCellValue(i,j,'O')
                score = MiniMax(b, 0, False)
                if score > bestScore:
                    bestScore = score
                    finalPosition = val
                b.SetCellValue(i,j,val)
    b.Turn(player, finalPosition)

scores = {
    'X' : -1,
    'O' : 1,
    'Draw' : 0
}

def MiniMax(b, depth, isMaximizing):
    result = b.WinCheck()
    if result != None:
        return scores[result]

    if isMaximizing:
        bestScore = -math.inf
        score = 0
        for i in range(3):
            for j in range(3):
                if b.CheckEmptyCell(i,j):
                    val = b.GetCellValue(i,j)
                    b.SetCellValue(i,j, 'O')
                    score = MiniMax(b, depth + 1, False)
                    b.SetCellValue(i, j, val)
                    bestScore = max(score, bestScore)
    
    else:
        bestScore = math.inf
        score = 0
        for i in range(3):
            for j in range(3):
                if b.CheckEmptyCell(i,j):
                    val = b.GetCellValue(i, j)
                    b.SetCellValue(i, j, 'X')
                    score = MiniMax(b, depth + 1, True)
                    b.SetCellValue(i, j, val)
                    bestScore = min(score, bestScore)
    
    return bestScore

if __name__ == "__main__":
    b = board.Board(3,3)
    res = None
    ans = int(input("Press 1 to Play 1st or Press 2 to Play 2nd: "))
    if ans == 1:
        player = 1
    else:
        player = -1
    while res == None:
        print()

        if player > 0:
            print("X's Turn")
            pos = int(input("Enter Position: "))
            b.Turn(player, pos)
            player *= -1
        else:
            print("O's Turn")
            AIMove(b, player)
            player *= -1
            
        res = b.WinCheck()

    print("Game Result: " + str(res))