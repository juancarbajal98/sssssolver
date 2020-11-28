puzzle = [
    [0, 0, 4], [0, 0, 0], [0, 6, 0], 
    [0, 0, 0], [0, 0, 5], [0, 0, 0], 
    [0, 1, 9], [2, 0, 6], [8, 0, 0], 
    [0, 6, 0], [0, 7, 8], [0, 5, 9], 
    [5, 0, 0], [0, 3, 0], [0, 0, 2], 
    [1, 3, 0], [5, 9, 0], [0, 8, 0], 
    [0, 0, 5], [7, 0, 1], [6, 4, 0], 
    [0, 0, 0], [8, 0, 0], [0, 0, 0], 
    [0, 2, 0], [0, 0, 0], [5, 0, 0]
    ]

def printCoords(a,b){
    print(puzzle[a][b])
}
# puzzle 
class Puzzle:
    puzzle = []

    def __init__(self):
        self.puzzle = puzzle

    def printpuzzle(self):
        print("Current Puzzle: " + self.puzzle)