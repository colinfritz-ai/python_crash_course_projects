import matplotlib.pyplot as plt 
import Random_Walk as RW 

while True:

	rw = RW.RandomWalk() # making an instance of the Random_Walk class which will have default 50000 data points in the walk 
	rw.fill_walk() # updates the contents of the class instance data attributes 
	plt.scatter(rw.x_values , rw.y_values)
	plt.show()

	keep_running = input("Make another walk? (y/n): ")
	if keep_running == 'n':
		break 





