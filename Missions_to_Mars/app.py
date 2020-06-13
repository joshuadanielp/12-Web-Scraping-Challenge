from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars_news

app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/craigslist_app"
mongo = PyMongo(app)


@app.route("/")
def index():
    # Find data
    mars_data = mongo.db.mars_data.find_one()

    # Return template and data
    return render_template("index.html", mars_data=mars_data)


# Route that will trigger scrape function
@app.route("/scrape")
def scraper():
    # Scrape functions
    mars_data = mongo.db.mars_data
    mars_data = scrape_mars_news.scrape()
    
    # Update Mongo DB
    mongo.db.mars_data.update({}, mars_data, upsert=True)
    
    # Redirect back to home
    return redirect("/", code=302)


if __name__ == "__main__":
    app.run(debug=True)
