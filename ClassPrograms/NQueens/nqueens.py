#Name: Isabelle Gallagher
#Block: 4
#Email: 2017igallagh@tjhsst.edu

import time
import math
import heapq
from collections import deque
import random
import copy
import heapq
from heapq import heappush, heappop

class nQueens:
	def __init__(self, state, choices, n):
		"""Initializes a nQueens board
		state -- An int array where index is the column and value is the row
		choices -- A list of sets which store the row choices for each column
		n -- the size of the board
		"""
		self.state = state 
		self.choices = choices
		self.n = n

	def assign(self, var, value):
		"""
		Assigns a value (row) to a column
		"""
		self.state[var] = value 
		self.choices[var] = set({})
		#Removes row from all choices:
		for c in range(self.n): 
			self.choices[c].difference_update({value}) 
		#Removes diagonals from all choices:
		for c in range(self.n):
			self.choices[c].difference_update({value+(abs(var-c)), value-(abs(var-c))})

	def goal_test(self): 
		"""
		Returns true if state is the goal state (each column has a row)
		"""
		success = True
		for s in self.state: 
			if s == 0:
				success = False
		return success
	
	def get_next_unassigned_var(self): 
		"""
		Returns an unassigned column with the minimum number of choices
		Breaks the tie by returning the smallest value of the two
		"""
		for c in range(self.n):
			if self.state[c] == 0 and self.choices[c] != None:
				min_choice_index = c
				break
		for c in range(self.n):
			if self.state[c] == 0 and self.choices[c] != None:
				if len(self.choices[c]) < len(self.choices[min_choice_index]):
					min_choice_index = c
					start_state = False
				elif len(self.choices[c]) == len(self.choices[min_choice_index]):
					min_choice_index = min(min_choice_index,c)
		return min_choice_index

	def get_choices_for_var(self, var):
		return self.choices[var]

	def num_unassigned_cols(self):
		num = 0
		for c in self.state:
			if c == 0:
				num = num + 1
		return num

	def __str__(self):
		rstring = ""
		return rstring


def dfs_search(board):
	tested = 0
	created = 0
	fringe = [board] #List of nQueens objects
	found = False
	while not found:
		if not fringe: #If fringe is empty, there is no solution
			print("cannot find solution")
			found = True
		else:
			x = fringe.pop()
			tested = tested+1
			if x.goal_test(): #returns true if all queens have been assigned (nothing is 0)
				print("goals: %d"%tested)
				print("nodes: %d"%created)
				found = True
			else:
				var = x.get_next_unassigned_var() #next available column
				choice_list = list(x.get_choices_for_var(var)) #put choices in list format
				new_children = []
				for value in choice_list: 
					"""
					create a new child for every choice, put into fringe based on least constraining
					"""
					s = [copy.copy(i) for i in x.state]
					ch = [copy.copy(i) for i in x.choices]
					child = nQueens(state = s, choices = ch, n = x.n)
					child.assign(var,value)
					bad = False
					for c in child.state:
						if c == 0 and child.choices[c] == None:
							bad = True
					if not bad:
						total_choices = 0
						for c in child.choices:
							total_choices = total_choices + len(c)
						if total_choices >= child.num_unassigned_cols():
							heapq.heappush(new_children, (total_choices, child))
							created = created + 1
				for i in range(len(new_children)):
						p,x = heapq.heappop(new_children)
						fringe.append(x)

#Run through problem for n = 0 to 100
for n in range(101):
	t = time.time()
	choice_set = set({})
	all_choices = []
	for i in range(n):
		choice_set.add(i+1)
	for i in range(n):
		all_choices.append(copy.deepcopy(choice_set))
	sboard = nQueens(state = [0]*n, choices = all_choices, n = n) #choices starts as all possibilities
	dfs_search(sboard)
	print(n)
	print("time: %f"%(time.time() - t))





