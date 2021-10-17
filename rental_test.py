import unittest
from customer import Customer
from rental import Rental
from movie import Movie, PriceCode


class RentalTest(unittest.TestCase):
	
	def setUp(self):
		self.new_movie = Movie("Mulan", PriceCode.NEW_RELEASE)
		self.regular_movie = Movie("CitizenFour", PriceCode.REGULAR)
		self.childrens_movie = Movie("Frozen", PriceCode.CHILDRENS)

	def test_movie_attributes(self):
		"""trivial test to catch refactoring errors or change in API of Movie"""
		m = Movie("CitizenFour", PriceCode.REGULAR)
		self.assertEqual("CitizenFour", m.get_title())
		self.assertEqual(PriceCode.REGULAR, m.get_price_code())

	def test_rental_price(self):
		rental = Rental(self.new_movie, 1)
		self.assertEqual(rental.get_price(), 3.0)
		rental = Rental(self.new_movie, 5)
		self.assertEqual(rental.get_price(), 15.0)
		rental = Rental(self.regular_movie, 5)
		self.assertEqual(rental.get_price(), 6.5)
		rental = Rental(self.childrens_movie, 8)
		self.assertEqual(rental.get_price(), 11.0)

	def test_rental_points(self):
		rental = Rental(self.new_movie, 1)
		self.assertEqual(rental.get_freq(), 1)
		rental = Rental(self.new_movie, 5)
		self.assertEqual(rental.get_freq(), 5)
		rental = Rental(self.regular_movie, 5)
		self.assertEqual(rental.get_freq(), 2)
		rental = Rental(self.childrens_movie, 8)
		self.assertEqual(rental.get_freq(), 1)