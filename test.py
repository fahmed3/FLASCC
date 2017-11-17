from flask import Flask
import requests, json, urllib3

app = Flask(__name__)
urllib3.disable_warnings()

@app.route("/")
def root():

	header = {
		"Accept": "application/json",
		"user-key": "cf8c9ba42742080b5d9e335fa01a9fa2"
	}
	f = requests.get("https://developers.zomato.com/api/v2.1/search?q=pizza",
		headers=header)
	
	#print f
	address = f.json()["restaurants"][0]["restaurant"]["location"]["address"]
	#print address
	
	final = "+".join(address.split(" "))
	#print final
	
	f = requests.get("https://maps.googleapis.com/maps/api/directions/json?origin=345+Chambers+St+New+York,+NY&destination=%s&key=AIzaSyAS7aTw_07NBhamUNuNVIO0rYUijRRUSTU"%(final) )
	
	print f.text
	
	return "f"

if __name__ == "__main__":
	app.debug = True
	app.run()
