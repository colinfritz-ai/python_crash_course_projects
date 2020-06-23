class dog():

	"""A simple attempt to model a dog."""

	def __init__(self, name, age):
		self.name = name 
		self.age = age 


	def sit(self):
		print(self.name.title() + " is now sitting.")


	def roll_over(self):
		print(self.name.title() + " rolled over!")

	


class Restaurant():

	def __init__(self, restaurant_name, cuisine_type):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type


	def describe_restaurant(self):
		description = self.restaurant_name + ' ' + self.cuisine_type
		print(description)

	def restaurant_open(self):
		print(self.restaurant_name + " open for business!")



restaurant = Restaurant('chilis', 'okay')
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)
restaurant.describe_restaurant()
restaurant.restaurant_open()
restaurant1 = Restaurant('Jameson_char', 'when we go')
restaurant2 = Restaurant('Texas De Brazil', 'steak')
restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
print("")

class Car():

	def __init__(self, make, model, year):
		self.make = make 
		self.model = model 
		self.year = year 
		self.mileage = 0


	def update_odometer(self, new_miles):
		self.mileage += new_miles 

	def reassign_odometer(self, new_miles):
		self.mileage = new_miles

	def describe_car(self):
		headline = self.make + ' ' + self.model + ' ' + self.year + ' ' + str(self.mileage)
		print(headline)


def list_modifier(l):
	del l[0]
	syke = [1,2,3,5,6,7]
	return syke

	
my_first = Car('honda', 'civic', '2006')
my_first.update_odometer(200000)
my_first.describe_car()




