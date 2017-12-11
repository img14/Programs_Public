"""
Search for the shortest path between two cities on a railroad
"""

import math
from math import pi, acos, sin, cos
import pickle
from pickle import dump, load
import heapq
from heapq import heappush, heappop

def calc_dist(place1, place2):
	if place1 == place2:
		return 0
	else:
		x1, y1 = positions[place1]
		x2, y2 = positions[place2]
		dist = calcd(x1,y1,x2,y2)
		return dist

def calcd(y1,x1, y2,x2):
	R = 3958.76 # miles = 6371 km
	y1 *= pi/180.0
	x1 *= pi/180.0
	y2 *= pi/180.0
	x2 *= pi/180.0
	return acos( sin(y1)*sin(y2) + cos(y1)*cos(y2)*cos(x2-x1) ) * R

#Create Graph
graph = {}
positions = {}


edgefile = open("rrEdges.txt")

with open("rrNodes.txt") as nodefile:
	for line in nodefile:
		i, lat, lon = line.split(' ')
		x = float(lat.rstrip())
		y = float(lon.rstrip())
		positions[i] = (x,y)

with open("rrEdges.txt") as edgefile:
	for line in edgefile:
		p1, p2 = line.split(' ')
		p1 = p1.rstrip()
		p2 = p2.rstrip()
		dist = calc_dist(p1, p2)
		if p1 in graph:
			graph[p1][p2] = dist
		else:
			graph[p1] = {p2:dist}
		if p2 in graph:
			graph[p2][p1] = dist
		else:
			graph[p2] = {p1:dist}

nameswithids = {}
with open("rrNodeCity.txt") as cityfile:
	for line in cityfile:
		city = ""
		cid = ""
		new_word = False
		for c in line:
			if new_word == False and c == ' ':
				new_word = True
			elif new_word == False:
				cid = cid + c
			else:
				city = city + c
		city = city.strip()
		cid = cid.strip()
		nameswithids[city] = cid


class Node:
    def __init__(self, value="", parent=None, cost = 0.0):
        self.value = value
        self.parent = parent
        self.cost = cost

#Search
f = open("solutions.txt", 'w')

with open("test.txt") as testfile:
	for line in testfile:
		s, t = line.split(',')
		s = s.strip()
		t = t.strip()

		start = nameswithids[s]
		target = nameswithids[t]

		startNode = Node(value = start, cost = 0)

		closed = []
		fringe = []
		heappush(fringe, (0, startNode))
		found = False
		targetNode = None

		found = False
		while not found:
			if not fringe:
				print("cannot find path")
				found = True
			else:
				p, x = heappop(fringe)
				if x.value == target:
					print("found")
					found = True
					targetNode = x
				else:
					if not x.value in closed:
						closed.append(x.value)
						#expand
						for n in graph[x.value]:
							h = calc_dist(n, target)
							nnode = Node(value = n, cost = x.cost+graph[x.value][n], parent = x)
							heappush(fringe, (nnode.cost+h, nnode))
		cost = targetNode.cost
		f.write("%s to %s: %s\n"%(s, t, cost))



