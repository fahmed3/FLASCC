from flask import Flask
import requests, json, urllib3

app= Flask(__name__)

def validAddress(){
#apicalls
}

@app.route('/')
def root():
    if 'user' not in session or 'address' not in session or validAddress():
        return render_template('login.html', title="Login")

    else:
        return redirect( url_for('search') )

@app.route('/search')
def search():
    if if 'user' not in session or 'address' not in session or validAddress():
        return redirect( url_for('/') )
    else:
        return render_template('search.html', title = "Search")
