import sys
# Get all 50 puzzles
fileName = ('Py1/Project_Euler/p096_sudoku.txt')
file = open(fileName,'r')
line = file.read()
file.close()
lines = line.split("Grid")
lines.remove(lines[0])
# Format one puzzle
totalPuzzles = [[[None for i in range(9)] for j in range(9)] for k in range(50)]
for iter in range(50):
    myPuzzle = lines[iter][4:93]
    rows = myPuzzle.split("\n")
    myPuzzle = [[0 for k in range(9)] for j in range(9)]
    for row in range(9):
        for col in range(9):
            myPuzzle[row][col] = int(rows[row][col])
    totalPuzzles[iter] = myPuzzle


class Puzzle():

    def __init__(self, myPuzzle):
        self.current = myPuzzle.copy()
        self.nineSet = {1,2,3,4,5,6,7,8,9}
        self.missingArray = self.genMissingArray()
        self.missingIndicies = []
        for row in range (9):
            for col in range (9):
                if (self.current[row][col] == 0):
                    self.missingIndicies.append((row, col))
        #print("init with Miss = ", len(self.missingIndicies))

    def completed(self):
        #print(self.current, "\n")
        for row in range(9):
            sum = ""
            for col in range(9):
                sum += str(self.current[row][col]) + " "
            print(sum)
        #print("exit")
        #sys.exit();

    def main(self):
        return self.recurse()

    def recurse(self):
        if (self.missingIndicies == []):
            self.completed()
            return self.current.copy()

        row, col = self.getSmall()
        miss = list(self.missingArray[row][col])
        for i in range(len(miss)):
            num = miss[i]
            new = Puzzle(self.current.copy())
            new.current[row][col] = num
            #print(new.checkError(row, col))
            if(new.checkError(row, col)):
                new2 = Puzzle(new.current.copy())
                new2.main()
        

    def getSmall(self):
        j = 1
        while (j < 10):
            for row, col in self.missingIndicies:
                if ((len(self.missingArray[row][col])) < j):
                    return row, col
            j += 1
        print("small issue")
        return None

    def checkError(self, row, col): #True = continue, False = error found
        num = self.current[row][col]
        mySet = set([])
        for i in range(9):
            if(i != row):
                mySet.add(self.current[i][col])
            if(i != col):
                mySet.add(self.current[row][i]) 
        blockRow, blockCol = Puzzle.getBlock(row, col)
        for r in range(blockRow, blockRow+3):
            for c in range(blockCol, blockCol+3):
                if(r!=row or c!=col):
                    mySet.add(self.current[r][c])
        return not (num in mySet)

    def checkNine(self, array):
        return set(array) == self.nineSet and len(array) == 9

    def checkRow(self, row):
        intList = []
        for i in range(9):
            intList.append(self.current[row][i])
        return self.checkNine(intList)

    def checkCol(self, col):
        intList = []
        for i in range(9):
            intList.append(self.current[i][col])
        return self.checkNine(intList)
    
    def getBlock(row, col):
        blockRow = int(row/3) * 3
        blockCol = int(col/3) * 3
        return blockRow, blockCol
   
    def checkBlock(self, blockRow, blockCol):
        intList = []
        for row in range(blockRow, blockRow+3):
            for col in range(blockCol, blockCol+3):
                intList.append(self.current[row][col])
        return self.checkNine(intList)
    
    def checkSpot(self, row, col):
        blockTuple = Puzzle.getBlock(row,col)
        return self.checkBlock(blockTuple[0], blockTuple[1]) and self.checkCol(col) and self.checkRow(row)
    
    def getMissingNums(self, row, col):
        if(self.current[row][col] != 0):
            return None
        mySet1 = set([self.current[row][i] for i in range(9)])
        mySet2 = set([self.current[i][col] for i in range(9)])
        bT = Puzzle.getBlock(row, col)
        mySet3 = set([])
        for row in range(bT[0], bT[0]+3):
            for col in range(bT[1], bT[1]+3):
                mySet3.add(self.current[row][col])
        return self.nineSet.difference(mySet1, mySet2, mySet3)

    def genMissingArray(self):
        missingArray = [[None for i in range(9)] for j in range(9)]
        for row in range(9):
            for col in range(9):
                missingArray[row][col] = self.getMissingNums(row, col)
        return missingArray
    
    def checkAll(self):
        for row in range(9):
            for col in range(9):
                if(not self.checkSpot(row, col)):
                    return False
        return True
"""
for s in range (50):
    notSolv = Puzzle(totalPuzzles[s])
    notSolv.main()
    print(" -- ", s, " -- ")

myList = []
for s in range (50):
    notSolv = Puzzle(totalPuzzles[s])
    notSolv.main()
    myList.append(notSolv.current[0][0] * 100 + notSolv.current[0][1] * 10 + notSolv.current[0][2] * 1)
print(len(myList), myList)

#[483, 215, 265, 139, 523, 188, 743, 487, 886, 861, 696, 962, 396, 634, 797, 361, 359, 784, 743, 782, 725, 385, 348, 
# 874, 364, 587, 897, 565, 535, 298, _9_, 243, 698, 852, _53, 516, 995, 365, 144, 193, 886, 387, 779, 317, 686, 954, 999, _61, 998, 301]
"""

notSolv = Puzzle(totalPuzzles[0])
notSolv.main()

print("done")


