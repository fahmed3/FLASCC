import requests

def call_api(key, src, dest):
	'''
	Calls the Google Directions API
	
	@type key: string
	@param key: The api key
	
	@type src: string
	@param src: The origin address
	
	@type dest: string
	@param dest: The desired destination address
	
	@rtype: dictionary
	@return: A dictionary version of the JSON response
	'''
	
	src = "+".join(src.split(" "))
	dest = "+".join(dest.split(" "))
	
	response = requests.get("https://maps.googleapis.com"
	"/maps/api/directions/json?"
	"origin=%s"
	"&destination=%s"
	"&key=%s"%(src, dest, key)).json()
	
	return response

def get_time(response):
	'''
	Extracts the total travel time for a trip
	
	@type response: dictionary
	@param response: The dictionary returned from call_api()
	
	@rtype: number
	@return: The total duration in minutes 
	'''
	
	
	
	pass

def distance(response):
	'''
	Extracts the total distance for a trip
	
	@type response: dictionary
	@param response: The dictionary returned from call_api()
	
	@rtype: number
	@return: The total distance in miles 
	'''
	
	
	pass

def get_directions(response):
	'''
	Extracts the directions for a trip
	
	@type response: dictionary
	@param response: The dictionary returned from call_api()
	
	@rtype: list
	@return: A list containing html formatted directions
	'''
	
	
	pass

