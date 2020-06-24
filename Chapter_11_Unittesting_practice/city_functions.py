
def city_population(city , country, population=0):
	if population:
		headline = city + ',' + " " + country + " " + "-" + " " + str(population)
	else:
		headline = city + ',' + " " + country


	return headline.title()

