class Square:
    def __init__(self,index,value):
        # member list: index, value, suspect list
        self.index = index # [a,b]
        self.value = value 
        self.suspectList = []
    def __str__(self):
        return str(self.value)
    


class Grid:
    def __init__(self,squares):
        self.squares = []
        self.populate(squares)
        for i in range(81):
            print(self.squares[i], end=" ")
            if ((i+1) % 9 == 0):
                print(' ')

    def populate(self,squares):
        for i in range (27):
            for j in range (3):
                self.squares.append(Square([i,j],squares[i][j]))

puzzle = [
    [0, 0, 4], [0, 0, 0], [0, 6, 0], [0, 0, 0], [0, 0, 5], [0, 0, 0], [0, 1, 9], [2, 0, 6], [8, 0, 0], [0, 6, 0], [0, 7, 8], [0, 5, 9], [5, 0, 0], [0, 3, 0], [0, 0, 2], [1, 3, 0], [5, 9, 0], [0, 8, 0], [0, 0, 5], [7, 0, 1], [6, 4, 0], [0, 0, 0], [8, 0, 0], [0, 0, 0], [0, 2, 0], [0, 0, 0], [5, 0, 0]
    ]

s = Grid(puzzle)



    