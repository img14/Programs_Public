"""
Generate csv file for testing majority with decision tree
"""
import numpy
from numpy import *
import csv	

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

