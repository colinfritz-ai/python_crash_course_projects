import matplotlib.pyplot as plt 
import Random_Walk as RW 

while True:

	rw = RW.RandomWalk() # making an instance of the Random_Walk class which will have default 50000 data points in the walk 
	rw.fill_walk() # updates the contents of the class instance data attributes 
	point_numbers=list(range(rw.num_points))
	plt.scatter(rw.x_values , rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolor='none', s=15)
	# emphasizing the first and last points 
	plt.scatter(0,0,c='green', edgecolors='none', s=100 ) 
	plt.scatter(rw.x_values[-1], rw.y_values[-1], c = 'red', edgecolor= 'none', s = 100) 

	# Remove the axes 
	plt.axes().get_xaxis().set_visible(False)
	plt.axes().get_yaxis().set_visible(False)

	plt.show()

	keep_running = input("Make another walk? (y/n): ")
	if keep_running == 'n':
		break 








