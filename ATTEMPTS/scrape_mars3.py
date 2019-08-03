# STEP 2 - MongoDB and Flask Application
from bs4 import BeautifulSoup as bs
import requests
from splinter import Browser
import pandas as pd
import numpy as np
import time

def init_browser():
    executable_path = {"executable_path": "chromedriver.exe"}
    return Browser("chrome", **executable_path, headless=False)


def scrape():
    mars = {}
    browser = init_browser()

    #Scrape NEWS
    url= 'https://mars.nasa.gov/news/'
    response= requests.get(url)
    soup= bs(response.text, 'html.parser')

    #Title and paragraph
    news_title= soup.find("div", class_="content_title").text
    news_p= soup.find("div", class_="rollover_description_inner").text

  
    # IMAGES
    #url = 'https://ww.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    #browser = Browser('chrome', headless=False)
    #browser.visit(url)

    #html = browser.html
    #soup = BeautifulSoup(html, 'html.parser')
    #featured_image_url = soup.find_all('img')[0]['src']
    
    #TWITTER - weather
    #url = 'https://twitter.com/marswxreport?lang=en'
    #browser.visit(url)
    #html = browser.html
    #soup = BeautifulSoup(html, 'html.parser')
    #mars_weather = soup.find_all('p', class_='TweetTextSize TweetTextSize--normal js-tweet-text tweet-text')[0].text.strip()
  
    # MARS FACTS
    #url = 'https://space-facts.com/mars/'
    #browser.visit(url)
    #mars_profile = pd.read_html(url)
    #mars_profile = pd.DataFrame(mars_profile[0])
    #mars_profile = mars_profile.to_html(header = False, index = False)
    #mars_profile

    # MARS Hemispheres
    #url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    #browser.visit(url)
    #html = browser.html
    #soup = BeautifulSoup(html, 'html.parser')
    #items = soup.find_all ('div', class_='item')
    #hemisphere_image_urls = []

    #hemisphere_main_url = 'https://astrogeology.usgs.gov'

        
    #hemisphere_image_urls=[
#        {'title': 'Cerberus Hemisphere Enhanced',
#  'img_url': 'https://astrogeology.usgs.gov/cache/images/cfa62af2557222a02478f1fcd781d445_cerberus_enhanced.tif_full.jpg'},
# {'title': 'Schiaparelli Hemisphere Enhanced',
#  'img_url': 'https://astrogeology.usgs.gov/cache/images/3cdd1cbf5e0813bba925c9030d13b62e_schiaparelli_enhanced.tif_full.jpg'},
# {'title': 'Syrtis Major Hemisphere Enhanced',
#  'img_url': 'https://astrogeology.usgs.gov/cache/images/ae209b4e408bb6c3e67b6af38168cf28_syrtis_major_enhanced.tif_full.jpg'},
# {'title': 'Valles Marineris Hemisphere Enhanced',
#  'img_url': 'https://astrogeology.usgs.gov/cache/images/7cf2da4bf549ed01c17f206327be4db7_valles_marineris_enhanced.tif_full.jpg'}
#  ]

    mars = {
        "News_Title": news_title,
        "News_Paragraph": news_p,
    #    "Image": featured_image_url,
    #    "Weather": mars_weather,
    #    "Attibutes": mars_profile,
    #    "Hemispheres": items,
    #    "Main Hemisphere": hemisphere_main_url,
    #    "Cerberus":hemisphere_image_urls[0]['img_url'],
    #    "Schiaparelli":hemisphere_image_urls[1]['img_url'],
    #    "Syrtis Major":hemisphere_image_urls[2]['img_url'],
    #    "Valles Marineris":hemisphere_image_urls[3]['img_url']
    }

    browser.quit()
    return mars