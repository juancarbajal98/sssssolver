# should return 9 size array with data
def getRowData(index,data):
    rowData = []
    rowNum = int(index[0] / 3)
    rowData.append(data[(rowNum*9):(rowNum*9)+8])
    #print (rowNum)
    #if(rowNum == 1):
     #   rowData.append(data[0:8])
    #if(rowNum == 2):
     #   rowData.append(data[9:17])
    print(rowData)
    return rowData

def getColumnData(index,data):
    ColumnData = []
    print(index)
    return ColumnData

def getBoxData(index,data):
    BoxData = []
    print(index)
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
            t_zone = []
            if(squares[i].suspectlist != None):
                getRowData(squares[i].index, squares)
                #getColumnData(squares[i].index)
                #getBoxData(squares[i].index)
            print()




puzzle = [
    [0, 0, 4], [0, 0, 0], [0, 6, 0], [0, 0, 0], [0, 0, 5], [0, 0, 0], [0, 1, 9], [2, 0, 6], [8, 0, 0], [0, 6, 0], [0, 7, 8], [0, 5, 9], [5, 0, 0], [0, 3, 0], [0, 0, 2], [1, 3, 0], [5, 9, 0], [0, 8, 0], [0, 0, 5], [7, 0, 1], [6, 4, 0], [0, 0, 0], [8, 0, 0], [0, 0, 0], [0, 2, 0], [0, 0, 0], [5, 0, 0]
    ]

s = Grid(puzzle)



    