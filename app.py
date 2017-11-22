from flask import Flask, session, render_template, request
#from utils import directions

import json, urllib3
#couldn't import requests?

#the file with our api keys
KEY_FILE = "keys.json"

app= Flask(__name__)
urllib3.disable_warnings()	#fixes ssl errors

def validAddress():
	#apicalls
	pass

@app.route('/')
def root():
    return render_template("home.html")

@app.route('/results', methods = ['POST', 'GET'])
def results():
    address = request.form['address']
    search = request.form['search']
    #check if address is valid
    #info from apis for nearest restaurants using address and search
    #info sent to results.html
    return render_template("results.html")

@app.route('/info')
def info():
    #info page for selected restaurant
    #get info from zomato
    return render_template("info.html")

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

