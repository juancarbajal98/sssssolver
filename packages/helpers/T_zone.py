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