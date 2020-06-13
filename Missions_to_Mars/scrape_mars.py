# Dependencies
from splinter import Browser
from bs4 import BeautifulSoup
import pandas as pd
import requests

def init_browser():
    #pointing to the directory where chromedriver exists
    executable_path = {'executable_path': 'chromedriver'}
    return Browser('chrome', **executable_path, headless=False)

def scrape_mars_news():
    
    # Initialize browser
    browser = init_browser()

    ### NASA Mars News ###

    # URL of page to be scraped
    news_url = 'https://mars.nasa.gov/news/'
    browser.visit(news_url)
    
#     # HTML Object
#     html = browser.html

#     # Parse HTML with Beautiful Soup
#     news_soup = BeautifulSoup(html, "html.parser")

#     # Retrieve the latest article title/sub-title
#     article = news_soup.find("div", class_='list_text')
#     news_title = article.find("div", class_="content_title").text
#     news_p = article.find("div", class_ ="article_teaser_body").text
  
#     ### JPL Mars Space Images - Featured Image ###

#     # NASA site to be scraped
#     nasa_url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
#     browser.visit(nasa_url)

#     # HTML Object 
#     html_image = browser.html

#     # Parse HTML with BeautifulSoup
#     img_soup = BeautifulSoup(html_image, "html.parser")

#     # Retrieve background-image url from style tag 
#     image_url = img_soup.find_all('img')[3]["src"]

#     # Website URl 
#     main_url = "https://www.jpl.nasa.gov"

#     # Concatenate website url with scraped route
#     featured_image_url = main_url + image_url

#     ### Mars Weather ###

#     # Mars weather to be scraped.
#     weather_url = 'https://twitter.com/marswxreport?lang=en'
#     browser.visit(weather_url)

#     # HTML Object
#     weather_html = browser.html

#     # Parse HTML with BeautifulSoup
#     weather_soup = BeautifulSoup(weather_html, 'html.parser')

#     # Scrape latest tweet with Mars weather info
#     tweet_container = weather_soup.find_all('div', class_="js-tweet-text-container")
#     print(tweet_container)

#     # Loop through tweets and grab any that contain weather info
#     for tweet in tweet_container: 
#         mars_weather = tweet.find('span').text
#         if 'sol' in mars_weather:
#             print(mars_weather)
#             break
#         else: 
#             pass

#     ### Mars Facts ###

#     # Mars facts to be scraped
#     facts_url = 'https://space-facts.com/mars/'
#     mars_tables = pd.read_html(facts_url)

#     # Create a dataframe
#     mars_facts_df = mars_tables[2]
#     mars_facts_df.columns = ["Description", "Value"]

#     # Use Pandas to convert the data to a HTML table string
#     mars_html_table = mars_facts_df.to_html()
#     mars_facts_df.to_html('mars_facts_table.html')

#     ### Mars Hemispheres ###

#     # Mars hemisphere site to be scraped
#     usgs_url = 'https://astrogeology.usgs.gov'
#     hemispheres_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
#     browser.visit(hemispheres_url)

#     # HTML Objet
#     hemispheres_html = browser.html

#     # Parse HTML with BeautifulSoup
#     hemispheres_soup = BeautifulSoup(hemispheres_html, 'html.parser')

#     # Retreive all items that contain mars hemispheres information
#     items = hemispheres_soup.find_all('div', class_='item')

#     # Create empty list for hemisphere urls 
#     image_urls = []

#     # Loop through the items previously stored
#     for i in items: 
#         # Store title
#         title = i.find('h3').text
        
#         # Store link that leads to full image website
#         partial_img_url = i.find('a', class_='itemLink product-item')['href']
        
#         # Visit the link that contains the full image website 
#         browser.visit(usgs_url + partial_img_url)
        
#         # HTML Object of individual hemisphere information website 
#         partial_img_html = browser.html
        
#         # Parse HTML with Beautiful Soup for every individual hemisphere information website 
#         img_soup = BeautifulSoup(partial_img_html, 'html.parser')
        
#         # Retrieve full image source 
#         img_url = usgs_url + img_soup.find('img', class_='wide-image')['src']
        
#         # Append the retreived information into a list of dictionaries 
#         image_urls.append({"title" : title, "img_url" : img_url})
    
#     # Dictionary that can be imported into Mongo
#     mars_data = {
#         "news_title": news_title,
#         "news_p": news_p,
#         "featured_image_url": featured_image_url,
#         "mars_weather": mars_weather,
#         "mars_html_table": mars_html_table,
#         "image_urls": image_urls
#     }

#     # Close the browser after scraping
#     browser.quit()

#     # Return dictionary
#     return mars_data