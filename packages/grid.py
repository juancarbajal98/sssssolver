from .square import Square
from .helpers.T_zone import (
    getRow, getRowData, 
    getColumn, getColumnData, 
    getBox, getBoxData)
from .suspectList import SuspectList
class Grid:
    def __init__(self,squares_2D):
        # 1D array of Square objects 
        self.squares = []
        # populate squares data field with data from 2d array
        self.populate(squares_2D)
        # once we populate squares we:
        # - get a (suspectlist != none) count
        # - trim suspects 
        self.unsolvedCount = self.setUnsolvedCount(self.squares)
        print(self.unsolvedCount)
        # update squares with Tzone
        self.setTzones(self.squares)
        self.trimSuspects()
        # call method to trim the suspect lists - pass in object of t-zone data


        #print(self.suspectListCount)
        #for i in range(81):
         #   print(self.squares[i], end=" ")
          #  if ((i+1) % 9 == 0):
           #     print(' ')
    #
    def populate(self,squares_2D):
        for i in range (27):
            for j in range (3):
                if(squares_2D[i][j] != 0):
                    self.squares.append(Square([i,j],squares_2D[i][j]))
                else:
                    self.squares.append(Square([i,j],squares_2D[i][j],[1,2,3,4,5,6,7,8,9]))
    
    def getUnsolvedCount(self):
        return self.unsolvedCount
    # returns the # of unsolved squares - i.e. those with value 0 
    def setUnsolvedCount(self, squares):
        count = 0 
        for i in range(81):
            if(squares[i].value == 0):
                count += 1
            else:
                pass
        return count
    def setTzones(self,squares):
        for i in range(81):
            # will hold t_zone once t_zone gets filled 
            #t_zones = []
            t_zone= []

            # for each square with valid suspect list: 
            if(squares[i].suspectlist != None):
                # get row data
                rowData = getRowData(squares[i].index, squares)
                for j in range(9):
                    t_zone.append(rowData[0][j].value)

                # get column data
                columnData = getColumnData(squares[i].index, squares)
                for k in range(9):
                    t_zone.append(columnData[0][k].value)
                
                # get box data
                boxData = getBoxData(squares[i].index, squares)
                for l in range(9):
                    t_zone.append(boxData[0][l].value)

                # set every squares T-zone with this array of objects
                squares[i].setTzone(t_zone)

    def trimSuspects(self):
        # iterate through
        for i in range(81):
            if(self.squares[i].value == 0):
                for j in range(1,10):
                    for k in range(len(self.squares[i].stripTzone()) ):
                        if(self.squares[i].stripTzone()[k]==j):
                            self.squares[i].trimSuspect(j)
        # update # of unsolved
        self.unsolvedCount = self.setUnsolvedCount(self.squares) kldj