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

	def fill_gas_tank(self):
		print("fill up")

class electric_car(Car):

	def __init__(self,make,model,year):
		super().__init__(make,model,year)
		self.battery=Battery()

	

	def fill_gas_tank(self):
		print("electric cars don't need gas")

class Battery():

	def __init__(self, charge=70, cell_density=10):
		self.battery_size = charge
		self.cell_density =cell_density

	def describe_battery(self):
		print("This car has a " + str(self.battery_size) + "-kWh battery.")










my_tesla = electric_car('tesla', 'model s', '2016')
my_tesla.describe_car()

my_tesla.fill_gas_tank()
my_tesla.battery.describe_battery()