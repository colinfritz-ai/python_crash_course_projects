from die import Die 
import pygal
die1 = Die() 
die2 = Die(num_sides=10) 
# Make some rolls, and store results in a list 
results = []
max_result = die1.num_sides+die2.num_sides
for roll_num in range(50000):
	result1 = die1.roll()
	result2 = die2.roll()
	result = result1 + result2
	results.append(result)

# analyze results 
frequencies = []
for value in range(1,max_result+1):
	frequency = results.count(value)
	frequencies.append(frequency)



#visualize the results in svg file
hist = pygal.Bar() 
hist.title = "results of rolling a D6 and D10 die 50000 times. "
hist.x_labels = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12','13', '14', '15', '16']
hist.x_tile = "Result"
hist.y_title= "Frequency of Result"
hist.add('D6 + D6', frequencies)
hist.render_to_file('die_visual.svg')




