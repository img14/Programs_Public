'''
Test majority accuracy with decision tree
'''
import csv
import math
import random
import numpy
from numpy import *

def majority(lis):
	s = 0
	for i in lis:
		s += int(i)
	if s > len(lis)/2:
		return 1
	else:
		return 0

csvfile = open('data1.csv', 'w')
writer = csv.writer(csvfile)
row = ["Label", "B1", "B2", "B3", "B4", "B5", "B6", "B7", "B8", "B9", "B10", "Result"]
writer.writerow(row)
for i in range(1024):
	s = format(i, '010b')
	l = list(s)
	li = [i+1]
	for c in l:
		li.append(c)
	li.append(majority(l))
	writer.writerow(li)
csvfile.close()

'''
Classes
'''
class Node():
	def __init__(self, n="", v=None, q=None):
		self.name = n
		self.value = v
		self.question = q
		self.answers = dict()

'''
Methods
'''
def print_tree(no, level):
	print("-"*level+no.question)
	for a in no.answers:
		if no.answers[a].value != None:
			print("-"*level+">"+no.answers[a].name+" : "+no.answers[a].value)
		else:
			print("-"*level+no.answers[a].name)
			print_tree(no.answers[a], level+1)

def entropy(freqs):
	s = sum(freqs)
	en = 0.0
	for i in freqs:
		if i != 0:
			prob = float(i)/s
			en = en + (-1*prob*math.log(prob,2))
	return en

def remainder(branch, total):
	r = 0
	for i in branch: 
		s = sum(i)
		r = r + (s/total*entropy(i))
	return r

def best_col(data, results1):
	minn = 1000
	minn_factor = None
	for k in data:
		options = set(data[k])
		r = dict()
		for o in options:
			r[o] = dict()
			for ro in res_options:
				r[o][ro] = 0
		for i in range(len(data[k])):
			r[data[k][i]][results1[i]] += 1
		r_list = []
		for x in r:
			templist = []
			for y in r[x]:
				templist.append(r[x][y])
			r_list.append(templist)
		cal = remainder(r_list, len(results1))
		if cal < minn:
			minn = cal
			minn_factor = k
	return minn_factor

def extract(data, col, value, results1):
	new_data = {}
	for x in data:
		for y in range(len(data[x])):
			if x != col and data[col][y] == value:
				if x in new_data:
					new_data[x].append(data[x][y])
				else:
					new_data[x] = [data[x][y]]
	return new_data, [results1[z] for z in range(len(results1)) if data[col][z] == value]

def make_tree(data, level, results1, tree):
	nnodes = 0
	best = best_col(data, results1)
	tree.question = best
	for val in set(data[best]):
		data2, results2 = extract(data, best, val, results1)
		if len(set(results2)) == 1:
			tree.answers[val] = Node(val,results2[0])
			nnodes += 1
		else:
			tree2 = Node(val)
			tree.answers[val] = tree2
			nnodes += make_tree(data2, level+1, results2, tree2)
	return nnodes

def get_answer(data, tree):
	v = None
	while not v:
		q = tree.question
		x = data[q]
		if x != '?':
			ans = tree.answers[x]
			if ans.value != None:
				v = ans.value
			else:
				tree = ans
		else:
			return "None"
	return v

def accuracy(l1, l2):
	c = 0.0
	for i in range(len(l1)):
		if l1[i] == l2[i]:
			c += 1
	return c/len(l1)

'''
Get all row numbers for rows that are not missing data
'''
rows_without_missing = []
rowcount = 0
with open('data1.csv', 'rt') as csvfile:
	r = csv.DictReader(csvfile)
	for row in r:
		if not '?' in row.values():
			rows_without_missing.append(rowcount)
		rowcount += 1


for j in range(10, 110):
	summ = 0.0
	for i in range(100):
		'''
		Choose [start] random row numbers to test tree
		'''
		choices = []
		start = j
		rr = list(rows_without_missing)
		while(start > 0):
			x = random.choice(rr)
			rr.remove(x)
			choices.append(x)
			start -= 1

		'''
		Read in all data for the randomly chosen rows. [label] is the label for the column - the first column that doesn't need to be used.
		[res] is the name of the results column. It is also deleted from main data in [info] but stored separately in [resultss]
		'''
		label = ""
		res = ""
		info = dict()
		resultss = list()

		mastercount = 0
		with open('data1.csv', 'rt') as csvfile:
			r = csv.DictReader(csvfile)
			for row in r:
				if mastercount in choices:
					count = 0
					for k in row:
						if count != 0 and count != len(row) - 1: 
							if k in info:
								info[k].append(row[k])
							else:
								info[k] = [row[k]]
						if count == 0:
							label = k
						if count == len(row) - 1:
							res = k
							resultss.append(row[k])
						count += 1
				mastercount += 1

		'''
		Store initial result options to be used in entropy and best column calculations
		'''
		res_options = set(resultss)

		'''
		Make and print the tree
		'''
		root = Node()
		numnodes = make_tree(info, 1, resultss, root)
		#print(numnodes)
		#print_tree(root,0)

		'''
		Read in data from all rows, not just 10 randomly chosen rows. 
		First column and results column are not needed in main data, results are stored in a separate list [realresults]
		'''
		info2 = []
		realresults = []
		countagain = 0
		with open('data1.csv', 'rt') as csvfile:
			r = csv.DictReader(csvfile)
			for row in r:
				if not countagain in choices:
					del row[label]
					realresults.append(row[res])
					del row[res]
					info2.append(dict(row))
				countagain += 1
		'''
		Get tree result for each row in the full data 
		'''
		myresults = []
		for i in info2:
			myresults.append(get_answer(i, root))

		'''
		Check accuracy
		'''
		#print(accuracy(myresults, realresults))
		summ += accuracy(myresults, realresults)
		#print(numnodes)
	print(summ/100.0)