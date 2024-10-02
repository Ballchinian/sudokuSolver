def sudoku(puzzle):
    def row(rowIndex,oneToNine):   
        for testRowPos in puzzle[rowIndex]:     
            if testRowPos != 0 and testRowPos in oneToNine:         
                oneToNine.remove(testRowPos)
        return oneToNine

    def column(rowPosIndex,oneToNine):
        for testRowIndex in range(9):
            if puzzle[testRowIndex][rowPosIndex] != 0 and puzzle[testRowIndex][rowPosIndex] in oneToNine:   
                oneToNine.remove(puzzle[testRowIndex][rowPosIndex])
        return oneToNine
    
    def box(rowIndex,rowPosIndex,oneToNine):
        sudokuBox = {}
        startingRowIndex = int(rowIndex)
        startingRowPosIndex = int(rowPosIndex)
        while startingRowIndex not in [0,3,6]:
            startingRowIndex -=1
        while startingRowPosIndex not in [0,3,6]:
            startingRowPosIndex -=1
        for subgridRow in range(startingRowIndex,startingRowIndex+3):
            for subgridCol in range(startingRowPosIndex,startingRowPosIndex+3):

                if puzzle[subgridRow][subgridCol] !=0 and puzzle[subgridRow][subgridCol] in oneToNine:
                    oneToNine.remove(puzzle[subgridRow][subgridCol])     
        return oneToNine

    
    sudokuDictionary = {}
    
    repeatDecider = True
    
    while repeatDecider == True:
        repeatDecider = False
        for rowIndex in range(9):
            for rowPosIndex in range(9):
                if puzzle[rowIndex][rowPosIndex]==0:
                    oneToNine = [1,2,3,4,5,6,7,8,9]
                    sudokuDictionary[(rowIndex,rowPosIndex)] = row(rowIndex,oneToNine)
                    sudokuDictionary[(rowIndex,rowPosIndex)] = column(rowPosIndex,sudokuDictionary[(rowIndex,rowPosIndex)])
                    sudokuDictionary[(rowIndex,rowPosIndex)] = box(rowIndex,rowPosIndex,sudokuDictionary[(rowIndex,rowPosIndex)])
                    if len(sudokuDictionary[(rowIndex,rowPosIndex)]) == 1:
                        repeatDecider = True
                        puzzle[rowIndex][rowPosIndex]=sudokuDictionary[rowIndex,rowPosIndex][0]
                        del sudokuDictionary[rowIndex,rowPosIndex]        
    return puzzle
