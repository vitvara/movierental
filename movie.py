from enum import Enum
class PriceCode(Enum):
	# The types of movies (price_code). 
	NEW_RELEASE = {"price": lambda days: 3*days, "frp": lambda days: days}
	REGULAR = {"price": lambda days: 2 + 1.5*(days-2) if days > 2 else 2, "frp": lambda days: 2}
	CHILDRENS = { "price": lambda days: 2 + 1.5*(days-2) if days > 2 else 2, "frp": lambda days: 1}

	def price(self, days):
		"Return the rental price for a given number of days"""
		pricing = self.value["price"]    # the enum member's price formula
		return pricing(days)

	def freq(self, days):
		"""Return the frequency"""
		freqency = self.value["frp"]
		return freqency(days)



class Movie:
	"""
	A movie available for rent.
	"""
	
	def __init__(self, title, price_code):
		# Initialize a new movie. 
		self.title = title
		self.price_code = price_code

	def get_price_code(self):
		# get the price code
		return self.price_code
	
	def get_title(self):
		return self.title

	def __str__(self):
		return self.title
