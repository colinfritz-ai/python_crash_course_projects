

def print_models(unprinted_designs, completed_models):
	""" 
	Simulate printing each design, until none are left.  
	Mve each design to completed_models after printing. 
	"""

	while unprinted_designs: 
		current_design = unprinted_designs.pop() 
		
		print("Printing model " + current_design)
		completed_models.append(current_design)


unprinted_designs= ['iphone case', 'robot pendant', 'dodecahedron']
completed_models=[]
print_models(unprinted_designs, completed_models)
print(unprinted_designs)