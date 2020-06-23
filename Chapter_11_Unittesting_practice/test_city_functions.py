from city_functions import city_population 
import unittest

class test_city_functions(unittest.TestCase):

	def test_no_pop(self):
		fact_line=city_population('tokyo', 'japan')
		self.assertEqual(fact_line, 'Tokyo, Japan')
	def test_pop(self):
		fact_line=city_population('tokyo', 'japan', '9273000')
		self.assertEqual(fact_line, 'Tokyo, Japan - 9273000')


unittest.main()

