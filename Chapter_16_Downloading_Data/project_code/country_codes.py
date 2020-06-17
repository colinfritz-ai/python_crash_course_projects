from pygal.maps.world import COUNTRIES

def get_country_code(country_name):

	for country_code, name in COUNTRIES.items():
		if country_name == name:
			return country_code


	return None

