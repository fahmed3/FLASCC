import requests

def get_restaurants(key, origin, keyword):
	'''
	Calls Zomato API

	@type key: string
	@param key: The api key

	@type origin: string
	@param src: The origin address

	@type keyword: string
	@param dest: keyword use to search for a restaurant ex. cafe

	@rtype: dictionary
	@return: A dictionary version of the JSON response
	'''

	headers = {'Accept': 'application/json','user-key': key}
	#print "https://developers.zomato.com/api/v2.1/locations?query=%s" %origin
	response = requests.get("https://developers.zomato.com/api/v2.1/locations?query=%s" %origin, headers = headers).json()
	locationId = response['location_suggestions'][0]['entity_id']
	#print locationId
	lat = response['location_suggestions'][0]["latitude"]
	lon = response['location_suggestions'][0]["longitude"]
	response = requests.get("https://developers.zomato.com/api/v2.1/search?lat=%f&lon=%f&q=%s" % (lat, lon, keyword), headers = headers).json()

	return response['restaurants']



def get_restaurant(key, restaurant_id):
	'''
	@type key: string
	@param key: The api key

	@type restaurant_id: string
	@param restaurant_id: id of the specified restaurant

	@rtype: dictionary
	@return: A dictionary version of the JSON response (of the restaurant specified)
	'''
	headers = {'Accept': 'application/json','user-key': key}
	#print "\n\n" + restaurant_id + "\n\n"
	response = requests.get("https://developers.zomato.com/api/v2.1/restaurant?res_id=%s" % (restaurant_id), headers = headers).json()
	return response

#can't use dict because its a reserved keyword
def get_rating(d):
	'''
	@type d: dictionary
	@param d: The dictionary returned from get_restaurants()

	@rtype: string
	@return: restaurant avg rating
	'''
	return d["restaurant"]["user_rating"]["aggregate_rating"]

def get_address(d):
	'''
	@type d: dictionary
	@param d: The dictionary returned from get_restaurants()

	@rtype: string
	@return: restaurant address
	'''
	return d["restaurant"]["location"]["address"]

def get_menu(d):
	'''
	@type d: dictionary
	@param d: The dictionary returned from get_restaurants()

	@rtype: string
	@return: url to menu
	'''
	return d["restaurant"]["menu_url"]

def get_cuisines(d):
	'''
	@type d: dictionary
	@param d: The dictionary returned from get_restaurants()

	@rtype: string
	@return: restaurant id
	'''
	return d["restaurant"]["cuisines"]

def get_name(d):
	'''
	@type d: dictionary
	@param d: The dictionary returned from get_restaurants()

	@rtype: string
	@return: restaurant name
	'''
	return d["restaurant"]["name"]

def get_num_of_reviews(d):
	'''
	@type d: dictionary
	@param d: The dictionary returned from get_restaurants()

	@rtype: string
	@return: restaurant num of reviews
	'''
	return d["restaurant"]["all_reviews_count"]

def get_id(d):
	'''
	for use when passing data from results page to info page

	@type d: dictionary
	@param d: The dictionary returned from get_restaurants()

	@rtype: string
	@return: restaurant id
	'''
	return d["restaurant"]["id"]
