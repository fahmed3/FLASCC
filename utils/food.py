import requests

def get_restaurants(key, origin, keyword):
	#in case origin  or keyword are multiple words long
	origin = "%20".join(origin.split(" "))
	keyword = "+".join(keyword.split(" "))
	print "https://developers.zomato.com"
	"/api/v2.1/search?"
	"q="
	"entity_id="
	"sort=real_distance"


	#https://developers.zomato.com/api/v2.1/search?entity_id=%22345%20chambers%20street%20new%20york%20city%2010282%22&q=thai&sort=real_distance

def get_restaurant(key, restaurant_id):
	pass

#can't use dict because its a reserved keyword
def get_rating(d):
	pass

def get_address(d):
	pass

def get_menu(d):
	pass

def get_cuisines(d):
	pass

def get_name(d):
	pass

def get_num_of_reviews(d):
	pass

def get_id(d):
	'''
	for use when passing data from results page to info page
	'''
	pass
