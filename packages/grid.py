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
        self.unsolvedCount = self.unsolvedCount(self.squares)
        self.setTzones(self.squares)
        self.trimSuspects(self.squares)
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
                    self.squares.append(Square([i,j],squares_2D[i][j],SuspectList()))
    
    # returns the # of unsolved squares - i.e. those with value 0 
    def unsolvedCount(self, squares):
        count = 0 
        for i in range(81):
            if(squares[i].value == 0):
                count += 1
            else:
                pass
        return count
        
    def setTzones(self,squares):
        t_zones = []
        for i in range(81):
            t_zone = {
                "t_row":[],
                "t_column":[],
                "t_box":[]
            }
            # temporary holders to replace above dictionary values
            t_row = []
            t_column = []
            t_box = []

            # for each square with valid suspect list: 
            if(squares[i].suspectlist != None):
                # get row data
                rowData = getRowData(squares[i].index, squares)
                for j in range(9):
                    t_row.append(rowData[0][j].value)
                t_zone["t_row"]=t_row

                # get column data
                columnData = getColumnData(squares[i].index, squares)
                for k in range(9):
                    t_column.append(columnData[0][k].value)
                t_zone["t_column"]=t_column
                
                # get box data
                boxData = getBoxData(squares[i].index, squares)
                for l in range(9):
                    t_box.append(boxData[0][l].value)
                t_zone["t_box"] =t_box
                t_zones.append(t_zone)
            squares[i].setTzone(t_zones)

    def trimSuspects(self,squares):
        t_zones = []
        for i in range(81):
            t_zone = {
                "t_row":[],
                "t_column":[],
                "t_box":[]
            }
            # temporary holders to replace above dictionary values
            t_row = []
            t_column = []
            t_box = []

            # for each square with valid suspect list: 
            if(squares[i].suspectlist != None):
                # get row data
                rowData = getRowData(squares[i].index, squares)
                for j in range(9):
                    t_row.append(rowData[0][j].value)
                t_zone["t_row"]=t_row

                # get column data
                columnData = getColumnData(squares[i].index, squares)
                for k in range(9):
                    t_column.append(columnData[0][k].value)
                t_zone["t_column"]=t_column
                
                # get box data
                boxData = getBoxData(squares[i].index, squares)
                for l in range(9):
                    t_box.append(boxData[0][l].value)
                t_zone["t_box"] =t_box
                t_zones.append(t_zone)
            
                # begin trim by removing own value from suspect list
                #squares[i].suspectlist.remove(squares[i].value)
                # right now we are trying to look for other occurences of 
                # the value but failing to consider the already existent occurence
                #for v in range(9):
                 #   for b in range(9):
                    # if any of the 9 values should be found anywhere in t zone
                    # they are removed from the suspect list
                    # - although this also looks for the squares value, it will never find it
                  #      if((t_zone["t_row"][b] == v) or (t_zone["t_col"][b] == v) or (t_zone["box"][b] == v)):
                   #         squares[i].suspectlist.remove(v)
                #print(squares[i].suspectlist)