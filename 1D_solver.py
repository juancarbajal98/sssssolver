#Sodoku calculator
import math
import numpy as np

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

def checksum(in_mat, op, num):
	temp_mat = []
	if(op == 0):
		temp_mat = row_grab(in_mat, num)
	elif(op == 1):
		temp_mat = col_grab(in_mat, num)
	elif(op == 2):
		temp_mat = box_grab(in_mat, num)

	sum = 0
	for i in range(len(temp_mat)):
		sum += temp_mat[i]

	if(sum == 45):
		return 1
	else:
		return 0


class Grid:
    # Node Initializer. Sets first node to carry data and sets pointer to next node
	def __init__(self, data):
		self.data = data
		self.squares = []
		self.suspectList = None

	def populate(self):
		for i in range(len(self.data)):
			s = Squares(i, self.data[i])
			if(s.value == 0):
				s.suspectList = []
			self.squares.append(s)

	def print(self):
		for i in range(len(self.data)):
			print(self.squares[i].value, end = " ")
			if((i+1)%9 == 0):
				print(' ')

	def package(self):
		out_mat = []
		for i in range(len(self.data)):
			out_mat.append(self.data[i])
		return out_mat

	def suslist(self):
		for i in range(len(self.data)):
			sus_temp = []
			if self.data[i] == 0:
				#check row, then column, then box
				#in the future, keep the row temp since we on the same one...
				sus_temp = row_grab(self.package(), int(i/9)+1)

				for j in range(len(sus_temp)):
					print(sus_temp[j], end = " ")
				print(" ")

				sus_temp = col_grab(self.package(), (i+1) % 9)
				for j in range(len(sus_temp)):
					print(sus_temp[j], end = " ")
				print(" ")


				sus_temp = box_grab(self.package(), int(i/27)*3 + (int(i/3)%3)+1)
				for j in range(len(sus_temp)):
					print(sus_temp[j], end = " ")
				print(" ")


			print(" ")



class Squares:
	def __init__(self, index, value):
		self.index = index #int
		self.value = value
		self.suspectList = []


###########TESTING############
mat = [	0, 0, 4, 0, 0, 0, 0, 6, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 1, 9, 2, 0, 6, 8, 0, 0, 0, 6, 0, 0, 7, 8, 0, 5, 9, 5, 0, 0, 0, 3, 0, 0, 0, 2, 1, 3, 0, 5, 9, 0, 0, 8, 0, 0, 0, 5, 7, 0, 1, 6, 4, 0, 0, 0, 0, 8, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 5, 0, 0]
g = Grid(mat)
#row_print(g.package(), 5)

mat_print(g.package())
g.suslist()
