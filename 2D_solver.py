def getRow(index):
    return int(index[0] / 3)
def getColumn(index):
    if((int(index[0]) % 3) != 0):
        return ((int(index[0]) % 3)*3 + int(index[1]))
    else:
        return int(index[1])

def getBox(index):
    # first line of 3 boxes - options are box 0, 1, 2
    if(getRow(index) < 3):
        if(getColumn(index) < 3):
            return 0
        elif(getColumn(index) < 6):
            return 1
        else:
            return 2
    elif(getRow(index) < 6):
        if(getColumn(index) < 3):
            return 4
        elif(getColumn(index) < 6):
            return 5
        else:
            return 6
    else:
        if(getColumn(index) < 3):
            return 7
        elif(getColumn(index) < 6):
            return 8
        else:
            return 9
# should return 9 size array with data
# @param - index:[a,b] where a ranges 0-27 and b 0-2
# @param - data: 1d array of square objects
def getRowData(index,data):
    rowData = []
    rowNum = getRow(index)
    #print('index:'+str(index[0]) + ', ' + str(index[1]) +' row number:'+ str(rowNum))
    rowData.append(data[(rowNum*9):(rowNum*9)+9])
    return rowData

def getColumnData(index,data):
    columnData = []
    temp = []
    colNum = getColumn(index)
    #print('index:'+str(index[0]) + ', ' + str(index[1]) +' column number:'+ str(colNum))
    for l in range(9):
        temp.append(data[l*9 + colNum])
    columnData.append(temp)
    return columnData

def getBoxData(index,data):
    BoxData = []
    temp = []
    boxNum = getBox(index)
    for i in range(81):
        # check index of every square 
        # - find those with same boxNum
        # - append these
        if(getBox(data[i].index) == boxNum):
            temp.append(data[i])
    BoxData.append(temp)
    return BoxData

class SuspectList:
    # t_pose - range of data
    def __init__(self,suspectlist):
        self.suspectList = suspectlist

# look at a index - deduce no more suspects 
# delete that square instance - reproduce it as the 2 param square
# run a live update on the # of squares with a valid suspectlist
class Square:
    def __init__(self,index,value,suspectlist=None):
        # member list: index, value, suspect list
        self.index = index # [a,b]
        self.value = value 
        self.suspectlist = suspectlist

    def __str__(self):
        return str(self.value)

class Grid:
    def __init__(self,squares_2D):
        # 1D array of Square objects 
        self.squares = []
        # populate squares data field with data from 2d array
        self.populate(squares_2D)
        # once we populate squares we:
        # - get a (suspectlist != none) count
        # - trim suspects 
        self.suspectListCount = self.suspectListCount(self.squares)
        self.trimSuspects(self.squares)
        # call method to trim the suspect lists - pass in object of t-zone data


        #print(self.suspectListCount)
        #for i in range(81):
         #   print(self.squares[i], end=" ")
          #  if ((i+1) % 9 == 0):
           #     print(' ')

    def populate(self,squares_2D):
        for i in range (27):
            for j in range (3):
                if(squares_2D[i][j] != 0):
                    self.squares.append(Square([i,j],squares_2D[i][j]))
                else:
                    self.squares.append(Square([i,j],squares_2D[i][j],[1,2,3,4,5,6,7,8,9] ))
    
    def suspectListCount(self, squares):
        count = 0 
        for i in range(81):
            if(squares[i].suspectlist != None):
                count += 1
            else:
                pass
        return count

    def trimSuspects(self,squares):
        for i in range(81):
            t_zone = {
                "t_row":[],
                "t_column":[],
                "t_box":[]
            }
            t_row = []
            t_column = []
            t_box = []
            if(squares[i].suspectlist != None):
                # pass in index and 1d squares data
                # get back a 2d array with all squares inside of this values row in 0th index
                rowData = getRowData(squares[i].index, squares)
                for j in range(9):
                    t_row.append(rowData[0][j].value)
                t_zone["t_row"]=t_row

                columnData = getColumnData(squares[i].index, squares)
                for k in range(9):
                    t_column.append(columnData[0][k].value)
                t_zone["t_column"]=t_column
                

                boxData = getBoxData(squares[i].index, squares)
                for i in range(9):
                    t_box.append(boxData[0][i].value)
                t_zone["t_box"] =t_box
                print ('t_zone[t_row]:',t_zone["t_row"])
                print ('t_zone[t_cal]:',t_zone["t_column"])
                print ('t_zone[box]:',t_zone["t_box"])



puzzle = [
    [0, 0, 4], [0, 0, 0], [0, 6, 0], [0, 0, 0], [0, 0, 5], [0, 0, 0], [0, 1, 9], [2, 0, 6], [8, 0, 0], [0, 6, 0], [0, 7, 8], [0, 5, 9], [5, 0, 0], [0, 3, 0], [0, 0, 2], [1, 3, 0], [5, 9, 0], [0, 8, 0], [0, 0, 5], [7, 0, 1], [6, 4, 0], [0, 0, 0], [8, 0, 0], [0, 0, 0], [0, 2, 0], [0, 0, 0], [5, 0, 0]
    ]

s = Grid(puzzle)



    