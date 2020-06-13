from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017"
mongo = PyMongo(app)


@app.route("/")
def index():
    # Find data from Mongo DB
    mars_dict = mongo.db.mars_dict.find_one()

    # Return template and data
    return render_template("index.html", mars_dict=mars_dict)


# Route that will trigger scrape function
@app.route("/scrape")
def scrape():
    # Scrape functions
    mars_dict = mongo.db.mars_dict
    mars_data = scrape_mars_news.scrape()
    
    # Update Mongo DB
    mars_dict.update({}, mars_data, upsert=True)
    
    # Redirect back to home
    return redirect("/", code=302)


if __name__ == "__main__":
    app.run(debug=True)
