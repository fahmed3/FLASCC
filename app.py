from flask import Flask, session, render_template, request, flash, redirect, url_for
from utils import directions, food

#pip install the missing modules
import json, urllib3, os

#the file with our api keys
KEY_FILE = "keys.json"

#for sessions
ORIGIN_ADDRESS = "origin"

app= Flask(__name__)
app.secret_key = os.urandom(256)
urllib3.disable_warnings()	#fixes ssl errors

def validAddress():
	#apicalls
	pass

@app.route('/')
def root():
    return render_template("home.html")

#helper function to check if address form was filled
def check(param, form):
    if param in form and form[param] != '':
        return True
    else:
        return False

@app.route('/results', methods = ['POST', 'GET'])
def results():
    form = request.form
    #adds address to the session if all address fields were filled in
    if check('address',form) and check('city',form) and check('state',form) and check('zip',form):
        address = "%s, %s, %s %s" % (
                form['address'],
                form['city'],
                form['state'],
                form['zip'])
        #print address
        session[ORIGIN_ADDRESS] = address
    #if all address fields weren't filled in, redirects to home page
    else:
        flash("***Please enter your address***")
        return redirect(url_for('root'))

    if 'search' in form:
        #print form["search"]
        search = form['search']

    api_keys = json.load(open(KEY_FILE))
    restaurants = food.get_restaurants(
        api_keys["zomato"],
        session[ORIGIN_ADDRESS],
        search);

    #dummy data, remove when api is done
    restaurants = json.loads('''{
  "results_found": 1,
  "results_start": 0,
  "results_shown": 1,
  "restaurants": [
    {
      "restaurant": {
        "R": {
          "res_id": 17224907
        },
        "apikey": "cf8c9ba42742080b5d9e335fa01a9fa2",
        "id": "17224907",
        "name": "Hi-So Thai",
        "url": "https://www.zomato.com/weehawken-nj/hi-so-thai-weehawken?utm_source=api_basic_user&utm_medium=api&utm_campaign=v2.1",
        "location": {
          "address": "1903 Willow Ave, Weehawken 07086",
          "locality": "Weehawken",
          "city": "Weehawken",
          "city_id": 3924,
          "latitude": "40.7601750000",
          "longitude": "-74.0275020000",
          "zipcode": "07086",
          "country_id": 216,
          "locality_verbose": "Weehawken, Weehawken"
        },
        "switch_to_order_menu": 0,
        "cuisines": "Thai",
        "average_cost_for_two": 25,
        "price_range": 2,
        "currency": "$",
        "offers": [],
        "thumb": "",
        "user_rating": {
          "aggregate_rating": "3.6",
          "rating_text": "Good",
          "rating_color": "9ACD32",
          "votes": "46"
        },
        "photos_url": "https://www.zomato.com/weehawken-nj/hi-so-thai-weehawken/photos?utm_source=api_basic_user&utm_medium=api&utm_campaign=v2.1#tabtop",
        "menu_url": "https://www.zomato.com/weehawken-nj/hi-so-thai-weehawken/menu?utm_source=api_basic_user&utm_medium=api&utm_campaign=v2.1&openSwipeBox=menu&showMinimal=1#tabtop",
        "featured_image": "",
        "has_online_delivery": 0,
        "is_delivering_now": 0,
        "deeplink": "zomato://restaurant/17224907",
        "has_table_booking": 0,
        "events_url": "https://www.zomato.com/weehawken-nj/hi-so-thai-weehawken/events#tabtop?utm_source=api_basic_user&utm_medium=api&utm_campaign=v2.1",
        "establishment_types": []
      }
    }
  ]
}''')

    results = []
    for item in restaurants["restaurants"]:
		'''
		temp = {}
		temp["id"] = food.get_id(item)
		temp["name"] = food.get_name(item)
		temp["rating"] = food.get_rating(item)
		temp["address"] = food.get_address(item)

		data = directions.call_api(api_keys["directions"],
		    session[ORIGIN_ADDRESS],
		    temp["address"])
		
		temp["distance"] = directions.get_distance(data)
		temp["travelDuration"] = directions.get_time(data)
		results.append(temp)
		'''
		#remove below and uncomment above when api is done
		temp = {}
		temp["id"] = item["restaurant"]["id"]
		temp["name"] = item["restaurant"]["name"]
		temp["rating"] = item["restaurant"]["user_rating"]["aggregate_rating"]
		temp["address"] = item["restaurant"]["location"]["address"]

		data = directions.call_api(api_keys["directions"],
		    session[ORIGIN_ADDRESS],
		    temp["address"])
		
		temp["distance"] = directions.get_distance(data)
		temp["travelDuration"] = directions.get_time(data)
		results.append(temp)
        

    return render_template("results.html", results=results)

@app.route('/info')
def info():
	'''
	info page for selected restaurant
	get info from zomato

	also use directions to display directions on how to get to the restaurant
	'''
	r_id = ""
	if "restaurant_id" in request.args:
		r_id = request.args["restaurant_id"]
	else:
		return redirect(url_for("root"))
	
	api_keys = json.load(open(KEY_FILE))
	restaurant = {}
	
	zom_data = food.get_restaurant(api_keys["zomato"], r_id)
	
	zom_data = json.loads('''{
  "R": {
    "res_id": 17224907
  },
  "apikey": "cf8c9ba42742080b5d9e335fa01a9fa2",
  "id": "17224907",
  "name": "Hi-So Thai",
  "url": "https://www.zomato.com/weehawken-nj/hi-so-thai-weehawken?utm_source=api_basic_user&utm_medium=api&utm_campaign=v2.1",
  "location": {
    "address": "1903 Willow Ave, Weehawken 07086",
    "locality": "Weehawken",
    "city": "Weehawken",
    "city_id": 3924,
    "latitude": "40.7601750000",
    "longitude": "-74.0275020000",
    "zipcode": "07086",
    "country_id": 216,
    "locality_verbose": "Weehawken, Weehawken"
  },
  "switch_to_order_menu": 0,
  "cuisines": "Thai",
  "average_cost_for_two": 25,
  "price_range": 2,
  "currency": "$",
  "offers": [],
  "thumb": "",
  "user_rating": {
    "aggregate_rating": "3.6",
    "rating_text": "Good",
    "rating_color": "9ACD32",
    "votes": "46"
  },
  "photos_url": "https://www.zomato.com/weehawken-nj/hi-so-thai-weehawken/photos?utm_source=api_basic_user&utm_medium=api&utm_campaign=v2.1#tabtop",
  "menu_url": "https://www.zomato.com/weehawken-nj/hi-so-thai-weehawken/menu?utm_source=api_basic_user&utm_medium=api&utm_campaign=v2.1&openSwipeBox=menu&showMinimal=1#tabtop",
  "featured_image": "",
  "has_online_delivery": 0,
  "is_delivering_now": 0,
  "deeplink": "zomato://restaurant/17224907",
  "has_table_booking": 0,
  "events_url": "https://www.zomato.com/weehawken-nj/hi-so-thai-weehawken/events#tabtop?utm_source=api_basic_user&utm_medium=api&utm_campaign=v2.1"
}''')
    
	'''
    restaurant = {}
    restaurant["name"] = food.get_name(zom_data)
    restaurant["rating"] = food.get_rating(zom_data)
    restaurant["address"] = food.get_address(zom_data)
	restaurant["menu"] = food.get_menu(zom_data)
	restaurant["cuisines"] = food.get_cuisines(zom_data)
	restaurant["numReviews"] = food.get_num_of_reviews(zom_data)
	
	dir_data = directions.call_api(
		api_keys["directions"],
		session[ORIGIN_ADDRESS],
		restaurant["address"])

    restaurant["distance"] = directions.get_distance(dir_data)
    restaurant["travelDuration"] = directions.get_time(dir_data)
    restaurant["directions"] = directions.get_directions(dir_data)
	'''
    
	restaurant = {}
	restaurant["name"] = zom_data["name"]
	restaurant["rating"] = zom_data["user_rating"]["aggregate_rating"]
	restaurant["address"] = zom_data["location"]["address"]
	restaurant["menu"] = zom_data["menu_url"]
	restaurant["cuisines"] = zom_data["cuisines"]
	#restaurant["numReviews"] = zom_data

	dir_data = directions.call_api(
		api_keys["directions"],
		session[ORIGIN_ADDRESS],
		restaurant["address"])

	restaurant["distance"] = directions.get_distance(dir_data)
	restaurant["travelDuration"] = directions.get_time(dir_data)
	restaurant["directions"] = directions.get_directions(dir_data)
	
	
	return render_template("info.html", restaurant=restaurant)

@app.route('/test')
def test():
	'''
	Stanley: just testing my functions out
	'''
	key = json.load(open(KEY_FILE))["directions"]
	data = directions.call_api(key, "345 Chambers St New York, NY",
		"11 West 53 St New York, NY")
	#print data
	print directions.get_time(data)
	print directions.get_distance(data)
	print directions.get_directions(data)
	
	res = ""
	for d in directions.get_directions(data):
		res += d
		res += "<br>"
	
	return res

if __name__ == "__main__":
	app.debug = True
	app.run()

