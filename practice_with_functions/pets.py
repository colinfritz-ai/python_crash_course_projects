import printing_models as pm

def describe_pet(animal_type, pet_name):
	"""Display information about a pet""" 
	print("\nI have a " + animal_type + ".")
	print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet('hamster', 'perry') # output changes with positional arguments in different positions.  
describe_pet(pet_name = 'perry', animal_type='hamster') #using solely keyword args makes order irrelevant

def get_formatted_name(first_name, last_name, middle_name=""): #making an empty default value is a way to define optional arguments to a function.  
	if middle_name:
		full_name = first_name+middle_name+last_name
	else:
		full_name=first_name+last_name #in this scheme the positional arguments are needed for the function to do its defined work.  


	return full_name.title()

name = get_formatted_name('john', 'bones')
print(name)

def build_person(first_name, last_name):
	person = {'first': first_name, 'last': last_name}
	return person 

person = build_person('colin', "fritz")
print(person)

g='test print'

print ('')
print ('') 
print ('')

unprinted_designs= ['iphone case', 'robot pendant', 'dodecahedron']
completed_models=[]
g='test print'
pm.print_models(unprinted_designs, completed_models)
