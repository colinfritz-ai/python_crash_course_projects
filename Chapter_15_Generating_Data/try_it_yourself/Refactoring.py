import matplotlib.pyplot as plt 
from random import choice

class RandomWalk(): 

	""" A class to generate random walks.""" 

	def __init__(self, num_points=5000):
		"""initialize attributes of a walk.""" 
		self.num_points = num_points

		# All walks start at (0,0)
		self.x_values = [0]
		self.y_values = [0] 


	def fill_walk(self):
		"""Calculate all the points in the walk.""" 

		# keep taking steps until the walk reaches the desired length. 
		while len(self.x_values) < self.num_points:
			x_step = self.get_step()
			y_step = self.get_step()
			# Reject moves that go nowhere. 
			if x_step == 0 and y_step == 0:
				continue 

			next_y = self.x_values[-1] + x_step
			next_x = self.y_values[-1] + y_step 

			self.x_values.append(next_x)
			self.y_values.append(next_y)


	def get_step(self): 
		direction = choice([1,-1])
		distance = choice([0,1,2,3,4,6,7,8])
		step = direction * distance
		return step 



while True:

	rw = RandomWalk(num_points=50000) # making an instance of the Random_Walk class which will have default 50000 data points in the walk 
	rw.fill_walk() # updates the contents of the class instance data attributes 
	point_numbers=list(range(rw.num_points))
	plt.figure(figsize=(10,6))
	plt.scatter(rw.x_values , rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolor='none', s=1)
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