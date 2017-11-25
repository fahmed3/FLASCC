# FLASCC
#### Fabiha Ahmed, Cynthia Cheng, Stanley Lin

## Eatables
Eatables takes a user's address to find restaurants near them, and allows them to search specific keywords for what they want. It returns a list of restaurants with their ratings, prices, and the times it would take to get there. The user can then select a restaurant and will be sent to a page with the restaurant's information, such as its description, its cuisine, or its menu - taken from the Zomato API. That page will also have directions to the chosen restaurant through the Google Maps API.

### How to Run
Clone the repo and, in the root of the directory, create a file named "keys.json" with the following format:
```json
{
  "directions": "<YOUR_API_KEY>",
  "zomato": "<YOUR_API_KEY>"
}
```
A Google Maps Directions API key can be obtained [here](https://developers.google.com/maps/documentation/directions/) and a Zomato API key can be obtained [here](https://developers.zomato.com/api).

Now run `python app.py` in the terminal. Go to `127.0.0.1:5000` in a browser to begin using the application.
