import requests

def call_api(key, src, dest):
	'''
	Calls the Google Directions API
	Note that not all requests are successful, so check the status first
	
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
	
	return response["routes"][0]["legs"][0]["duration"]["value"] / 60

def get_distance(response):
	'''
	Extracts the total distance for a trip
	
	@type response: dictionary
	@param response: The dictionary returned from call_api()
	
	@rtype: string
	@return: The total distance based on the locale of the origin
	'''
	
	return response["routes"][0]["legs"][0]["distance"]["text"]

def get_directions(response):
	'''
	Extracts the directions for a trip
	
	@type response: dictionary
	@param response: The dictionary returned from call_api()
	
	@rtype: list
	@return: A list containing html formatted directions
	'''
	
	result = []
	steps = response["routes"][0]["legs"][0]["steps"]
	
	for step in steps:
		result.append(step["html_instructions"])
	
	return result

