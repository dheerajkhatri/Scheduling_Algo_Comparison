import random
import math
import heapq as heap
import matplotlib.pyplot as plt

def preemptive_scheduling(file_name):
	fo = open(file_name,"r")
	e = fo.readlines()
	fo.close()
	fo = open(file_name,"r")
	original_e = fo.readlines()
	fo.close()
	num_processors = int(e[0])
	num_task = int(e[1])
	sum = 0
	miss = 0
	priority = []
	j = [1,1]
#	sim_time = 1000 * num_processors
	for	i in range(2,num_task+2):
		e[i] = int(e[i])
#		original_e[i] = int(original_e[i])
		sum = sum + e[i]
	sim_time = sum / num_processors
	new_sum = 0
	for	i in range(2,num_task+2):

		j.append(1)
		heap.heappush(priority , (float(sim_time)/e[i],i))

	for time in range(1,sim_time+1):
		for z in range(0,num_processors):
			x = []
			if priority.__len__() == 0:
				break
			a = heap.heappop(priority)
			prior = a[0];
			i = a[1];
			j[i] = j[i] + 1;
			if j[i] != e[i] + 1:
				b = j[i]*prior/(j[i] - 1)
				x.append((b, i))
        
		for z in range(0,x.__len__()):
			heap.heappush(priority, x[z])
			
		for	k in range(2,num_task+2):
			lag = (e[k]*time)/sim_time - (j[k] - 1)
#			print lag
			if lag >= 1:
				miss = miss + math.floor(lag)
#		print time
		if priority.__len__() == 0:
			return miss
	return miss