import random
import math
import heapq as heap
import matplotlib.pyplot as plt
from preemptive import  preemptive_scheduling
from round_robin import  round_robin


def generate_data_file(num_processors, t):
	file_name = "temp.txt"
	fo = open(file_name,"w")
	fo.write(str(num_processors))
	fo.write("\n")
	fo.write(str(t))
	fo.write("\n")
	for num in range(1,t+1):
		random_no = random.randint(200,500)
		fo.write(str(random_no))
		fo.write("\n")

	fo.close()
	return file_name

if __name__ == "__main__":
	num_processors = 1
	p = []	
	y1 = []
	z1 = []
	
	while (num_processors < 64):
		print 'Number of Processors :' , num_processors
		t = 10
		x = []
		y = []
		z = []		
		while(t <= 100):
			print 'Task being executed : ' , t 
			miss_round_robin = 0
			miss_preemptive = 0
			for num in range(1,11):
				file_name = generate_data_file(num_processors,t)
				miss_preemptive = miss_preemptive + preemptive_scheduling(file_name)
				miss_round_robin = miss_round_robin + round_robin(file_name)
			miss_preemptive = miss_preemptive / 10
			miss_round_robin = miss_round_robin / 10
			y.append(miss_preemptive)
			z.append(miss_round_robin)
			x.append(t)
			t = t + 10
		num_processors = 2 * num_processors
		p.append(num_processors)
		
		plt.plot(x,y,'b-',label='Preemptive scheduling')
		plt.plot(x,z,'g-',label='Round Robin scheduling')
		plt.xlabel('number of tasks')
		plt.ylabel('misses')
		plt.show()
		y1.append(miss_preemptive)
		z1.append(miss_round_robin)
		
	plt.plot(p,y1,'b-',label='Preemptive scheduling')
	plt.plot(p,z1,'g-',label='Round Robin scheduling')
	plt.xlabel('number of processors')
	plt.ylabel('misses')
	plt.show()
		

		