from flask import Flask

app = Flask(__name__)
app.secret_key = os.urandom(256)

@app.route("/")
def root():
	return "hello!"

if __name__ == "__main__":
	app.debug = True
	app.run()

