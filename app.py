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

@app.route('/results', methods = ['POST'])
def results():
    return render_template("results.html")

#I don't think we need users or sessions for this project
#commenting it out for now
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
	return str(data)

if __name__ == "__main__":
	app.debug = True
	app.run()

