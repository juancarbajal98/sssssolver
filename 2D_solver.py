from packages.grid import Grid

puzzle = [
    [0, 0, 4],[0, 0, 0],[0, 6, 0], 
    [0, 0, 0],[0, 0, 5],[0, 0, 0], 
    [0, 1, 9],[2, 0, 6],[8, 0, 0],
    [0, 6, 0],[0, 7, 8],[0, 5, 9], 
    [5, 0, 0],[0, 3, 0],[0, 0, 2], 
    [1, 3, 0],[5, 9, 0],[0, 8, 0], 
    [0, 0, 5],[7, 0, 1],[6, 4, 0], 
    [0, 0, 0],[8, 0, 0],[0, 0, 0], 
    [0, 2, 0],[0, 0, 0],[5, 0, 0]
    ]

s = Grid(puzzle)
while(s.getUnsolvedCount() > 0):
    s.trimSuspects() # mess with master copy - can trim from an array of 9 every single time rather than a suspect list

# have to reinitialize all the suspect lists before next iteration



    