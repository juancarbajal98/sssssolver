#Sodoku calculator
import math
import numpy as np

global mat

def mat_print(in_mat):
	for i in range(len(in_mat)):
		print(in_mat[i], end=" ")
		if ((i+1)%9) == 0:
			print(' ')
	print(' ')

def row_print(in_mat, num):
	for i in range(len(in_mat)):
		if ((num-1)*9 <= i) and (i < (num)*9):
			print(in_mat[i], end=" ")
	print(' ')
	print(' ')

#0, 9, 18, 27...
def col_print(in_mat, num):
	for i in range(len(in_mat)):
		if (i % 9) == num-1:
			print(in_mat[i])
	print(' ')

def box_print(in_mat, num):
	step = 0
	wrap = 0

	#given the boxnum, find the root number
	root = int((num - 1) / 3) * 27

	for boxnum in range(9):
		print(in_mat[root + step +  wrap + ((num - 1) % 3)*3 ], end = ' ')
		step += 1
		if(step == 3):
			print(' ')
			wrap += 9
			step = 0

	print(' ')

def row_grab(in_mat, num):
	out_mat = []
	for i in range(len(in_mat)):
		if ((num-1)*9 <= i) and (i < (num)*9):
			out_mat.append(in_mat[i])

	return out_mat

#0, 9, 18, 27...
def col_grab(in_mat, num):
	out_mat = []
	for i in range(len(in_mat)):
		if (i % 9) == num-1:
			out_mat.append(in_mat[i])
	return out_mat

def box_grab(in_mat, num):
	out_mat = []
	step = 0
	wrap = 0
	#given the boxnum, find the root number
	root = int((num - 1) / 3) * 27
	for boxnum in range(9):
		out_mat.append(in_mat[root + step +  wrap + ((num - 1) % 3)*3 ])
		step += 1
		if(step == 3):
			wrap += 9
			step = 0
	return out_mat

def checksum(in_mat):
	sum = 0
	for i in range(len(in_mat)):
		sum += in_mat[i]

	if(sum == 45):
		return 1
	else:
		return 0


class Box:

	def __init__(self, box):
		self.box = box

	def printbox(self):
		print('This box is: ', self.box)


#reference
b= Box('box1')
b.printbox()

###########TESTING############
mat = [	0, 0, 4, 0, 0, 0, 0, 6, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 1, 9, 2, 0, 6, 8, 0, 0, 0, 6, 0, 0, 7, 8, 0, 5, 9, 5, 0, 0, 0, 3, 0, 0, 0, 2, 1, 3, 0, 5, 9, 0, 0, 8, 0, 0, 0, 5, 7, 0, 1, 6, 4, 0, 0, 0, 0, 8, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 5, 0, 0]

row_print(row_grab(mat,9), 1)
