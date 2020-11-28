# class structure - super being grid, sub being square
import tkinter as Tk

#import sys
#sys.path.append('./packages')
#from puzzle import Puzzle as p

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

#  0,0 0,1 0,2  1,0, 1,1 1,2  2,0 2,1 2,2
#  3,0 3,1 3,2  4,0


#import numpy as np
class Grid(object):
    def __init__(self,root,n):
        cubeSize = 50 # store size of each cube
        game_board = [] # list composed of 2-element lists as its elements
        # i.e. [[1,2],[3,4]]
        self.cubes = []
        self.current = (0,0)
        global puzzle
        for i in range(n+1):
            for j in range(n+1):
                game_board.append([i,j])
        #self.color_s_list = [[0]*(n+1)]*(n+1) # 2d list to store square positions
        # Canvas object where grid will be printed on
        self.w = Tk.Canvas(root, width = n*cubeSize, height = n*cubeSize)
        self.w.pack()
        # create lines
        for i in range(n-1):
            d = (i+1)*cubeSize
            self.w.create_line(d,0,d,n*100,)
            self.w.create_line(0,d,n*100,d)
        # create rectangles that overlap on canvas object and append to 1D cubes array
        for i in range(n):
            for j in range(n):
                self.cubes.append(self.w.create_rectangle(cubeSize*game_board[j][1],cubeSize*game_board[i][1],cubeSize*game_board[j][1]+cubeSize,cubeSize*game_board[i][1]+cubeSize))
        # fill in numbers
        #for i in range(27):
          #  for j in range(3):
                #print(puzzle[i][j])
                #self.w.create_text((cubeSize*i, cubeSize*i+100), text = str(puzzle[i][j]))
        self.w.pack()

def knights_tour(n):
    root = Tk.Tk() # root
    game = Grid(root,n)
    root.mainloop()
if __name__=='__main__':
    knights_tour(9)
