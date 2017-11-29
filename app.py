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
        #city needed to search for nearby resaturants
        city = form['city']
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
    
    results = []
    for item in restaurants:
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

    return render_template("results.html", results=results)

@app.route('/info')
def info():
	'''
	info page for selected restaurant
	get info from zomato

	also use directions to display directions on how to get to the restaurant
	'''
	if "restaurant_id" in request.args:
		r_id = request.args["restaurant_id"]
	else:
		return redirect(url_for("root"))

	api_keys = json.load(open(KEY_FILE))
	restaurant = {}

	zom_data = food.get_restaurant(api_keys["zomato"], r_id)

	restaurant = {}
	restaurant["name"] = zom_data["name"]
	restaurant["rating"] = zom_data["user_rating"]["aggregate_rating"]
	restaurant["address"] = zom_data["location"]["address"]
	restaurant["menu"] = zom_data["menu_url"]
	restaurant["cuisines"] = zom_data["cuisines"]

	#print session[ORIGIN_ADDRESS]

	dir_data = directions.call_api(
		api_keys["directions"],
		session[ORIGIN_ADDRESS],
		restaurant["address"])

	restaurant["distance"] = directions.get_distance(dir_data)
	restaurant["travelDuration"] = directions.get_time(dir_data)
	restaurant["directions"] = directions.get_directions(dir_data)


	return render_template("info.html", restaurant=restaurant)


if __name__ == "__main__":
	app.debug = True
	app.run()
