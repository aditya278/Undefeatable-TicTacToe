class Board:

    def __init__(self, rows, columns):
        self.boardArr = []
        self.rows = rows
        self.columns = columns
        self.CreateBoard()
    
    def CreateBoard(self):
        val = 1
        for i in range(self.rows):
            self.boardArr.append([(val+i+j) for j in range(self.columns)])
            val += self.columns - 1
        self.PrintBoard()

    def PrintBoard(self):
        for i in range(self.rows):
            for j in range(self.columns):
                endl = ' '
                if j < self.columns:
                    endl = ' | '
                print(self.boardArr[i][j], end=endl)
            print()
            for j in range(self.columns):
                print('- ', end = '  ')
            print()

    def Turn(self, player, position):
        val = 1
        for i in range(self.rows):
            for j in range(self.columns):
                if (val + i + j) == position:
                    indexVal = self.boardArr[i][j]
                    if indexVal != 'X' and indexVal != 'O':
                        indexVal = 'X' if player == 1 else 'O'
                        self.boardArr[i][j] = indexVal
                        break
            val += 2

        self.PrintBoard()

    def WinCheck(self):

        #Check Vertical
        for j in range(self.columns):
            valAtIndex = self.boardArr[0][j]
            if valAtIndex == 'X' or valAtIndex == 'O':
                if (self.boardArr[1][j] == self.boardArr[2][j] == valAtIndex):
                    return valAtIndex
        
        #Check Horizontal
        for i in range(self.rows):
            valAtIndex = self.boardArr[i][0]
            if valAtIndex == 'X' or valAtIndex == 'O':
                if (self.boardArr[i][1] == self.boardArr[i][2] == valAtIndex):
                    return valAtIndex
        
        # Check Diagonally
        if (self.boardArr[0][0] == self.boardArr[1][1] == self.boardArr[2][2]) or (self.boardArr[0][2] == self.boardArr[1][1] == self.boardArr[2][0]):
            return self.boardArr[1][1]


        for i in range(self.rows):
            for j in range(self.columns):
                if self.boardArr[i][j] != 'X' and self.boardArr[i][j] != 'O':
                    return None

        return 'Draw'

    def CheckEmptyCell(self, i, j):
        if self.boardArr[i][j] != 'X' and self.boardArr[i][j] != 'O':
            return True
        else:
            return False

    def GetCellValue(self, i, j):
        return self.boardArr[i][j]

    def SetCellValue(self, i, j, value):
        self.boardArr[i][j] = value
