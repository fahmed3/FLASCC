import requests

def get_restaurants(key, origin, keyword):
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
	headers = {'Accept': 'application/json','user-key': key}
	#print "\n\n" + restaurant_id + "\n\n"
	response = requests.get("https://developers.zomato.com/api/v2.1/restaurant?res_id=%s" % (restaurant_id), headers = headers).json()
	return response

#can't use dict because its a reserved keyword
def get_rating(d):
	return d["restaurant"]["user_rating"]["aggregate_rating"]

def get_address(d):
	return d["restaurant"]["location"]["address"]

def get_menu(d):
	return d["restaurant"]["menu_url"]

def get_cuisines(d):
	return d["restaurant"]["cuisines"]

def get_name(d):
	return d["restaurant"]["name"]

def get_num_of_reviews(d):
	return d["restaurant"]["all_reviews_count"]

def get_id(d):
	'''
	for use when passing data from results page to info page
	'''
	return d["restaurant"]["id"]
