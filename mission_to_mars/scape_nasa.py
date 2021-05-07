from splinter import Browser
from bs4 import BeautifulSoup as bs
import time
from webdriver_manager.chrome import ChromeDriverManager


def scrape_info():
    # Set up Splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    # Visit NASA Mars site
    url = 'https://redplanetscience.com/'
    browser.visit(url)

    time.sleep(1)

    mars_data = {}

    # Scrape page into Soup
    html = browser.html
    soup = bs(html, "html.parser")
    
    #get title and subtitle
    results = soup.find_all('div', class_='list_text')
    
    #get title
    title = results.find_all('div', class_='content_title')[0].text

    #get subtitle
    subtitle = results.find_all('div', class_='article_teaser_body')[0].text

    #store data in dictionary
    mars_data = {
        "title" = title
        "subtitle" = subtitle
    }

    # Close the browser after scraping
    browser.quit()

    # Return results
    return mars_data