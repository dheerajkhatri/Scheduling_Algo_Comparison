import random
import math
import heapq as heap
import matplotlib.pyplot as plt

def round_robin(file_name):

	fo = open(file_name,"r")
	e = fo.readlines()
	fo.close()
	j = [1,1]
	num_processors = int(e[0])
	num_task = int(e[1])
	sum = 0
	miss = 0
#	sim_time = 1000 * num_processors
	########################input
	for	i in range(2,num_task+2):
		e[i] = int(e[i])
		j.append(0)
		sum = sum + e[i]
#	new_sum = 0
	sim_time = sum / num_processors

	i = 2
	########################time simulation
	for time in range(1,sim_time+1):
		i_prev = i
		x = 0
		cond = 1
		num_busy_process = 0
		while (cond == 1):
			if j[i] != e[i]:
				j[i] = j[i] + 1
				num_busy_process = num_busy_process + 1
			else:
				x = x + 1
			i = i + 1
			if i == num_task + 2:
				i = 2
			if num_busy_process == num_processors:
				cond = 0
			if i == i_prev:
				cond = 0
			if x == num_task:
				return miss
		for	k in range(2,num_task+2):
			lag = (e[k]*time)/sim_time - (j[k])
#			print lag
			if lag >= 1:
				miss = miss + math.floor(lag)
#		print time
	return miss