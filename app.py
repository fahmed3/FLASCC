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

    #check if address is valid
    #info from apis for nearest restaurants using address and search
    #info sent to results.html
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
	
	
	return render_template("info.html", restaurant=restaurant)

#I don't think we need users or sessions for this project
#I'll comment it out for now
'''
    if 'user' not in session or 'address' not in session or validAddress():
        return render_template('login.html', title="Login")

    else:
        return redirect( url_for('search') )
'''
    
@app.route('/search')
def search():
    if 'user' not in session or 'address' not in session or validAddress():
        return redirect( url_for('/') )
    else:
        return render_template('search.html', title = "Search")

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

