import requests

def get_restaurants(key, origin, keyword):
	#in case origin  or keyword are multiple words long
	origin = "%20".join(origin.split(", "))
	origin = "%22" + ("%20".join(origin.split(" "))) + "%22"
	keyword = "+".join(keyword.split(" ")) + ""
	print "https://developers.zomato.com"\
	"/api/v2.1/search?"\
	"entity_id=%s"\
	"&q=%s"\
	"&sort=real_distance"%(origin, keyword)

	url = "https://developers.zomato.com"\
	"/api/v2.1/search?"\
	"entity_id=%s"\
	"&q=%s&sort=real_distance"%(origin,keyword)

	headers = {'Accept': 'application/json','user-key': key}
	response = requests.get(url, headers=headers)

	# print "\n\n"
	# for x in response:
    # 	print x
    # for y in response[x]:
    #     print (y,':',response[x][y])
	print response
	print response.json()
	return response

def get_restaurant(key, restaurant_id):
	pass

#can't use dict because its a reserved keyword
def get_rating(d):
	return d["restaurants"]["user_rating"]["aggregate_rating"]

def get_address(d):
	return d["restaurants"]["location"]["address"]

def get_menu(d):
	return d["restaurants"]["menu_url"]

def get_cuisines(d):
	return d["restaurants"]["cuisines"]

def get_name(d):
	return d["restaurants"]["name"]

def get_num_of_reviews(d):
	return d["restaurants"]["all_reviews_count"]

def get_id(d):
	'''
	for use when passing data from results page to info page
	'''
	print d + "\n"
	return d[0]
