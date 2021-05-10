from splinter import Browser
from bs4 import BeautifulSoup
import time
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd


def scrape_info():
    #Featured News
    # Set up splinter for news section
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)
    url = 'https://redplanetscience.com/'
    browser.visit(url)

    #scrape webpage for container
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    results = soup.find('div', class_='list_text')
    news_title = results.find('div', class_='content_title').text
    news_subtitle = results.find('div', class_='article_teaser_body').text

    # Featured Image
    # Set up Splinter for featured image section
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)
    url = 'https://spaceimages-mars.com/'
    browser.visit(url)

    # scrape webpage for full img link
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    browser.links.find_by_partial_text('FULL IMAGE').click()
    results = soup.find('a', class_='showimg fancybox-thumbs')["href"]
    featured_image_url = url + results

    # Mars Fact Table
    # Webpage url                                                                                                               
    data_url = 'https://galaxyfacts-mars.com/'

    # Extract tables
    dfs = pd.read_html(data_url)
    mars_df = dfs[0]
    mars_df = mars_df.rename(columns={0:"",1:"Mars",2:"Earth"})
    mars_df = mars_df.set_index("")
    
    #turn df into html
    mars_table_html = mars_df.to_html()
    mars_table_html = mars_table_html.replace('\n', '')

    # Mars Hemisphere Section
    # Set up splinter for hemisphere section
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)
    url = 'https://marshemispheres.com/'
    browser.visit(url)

    # scrape webpage for full img link and hemisphere name
    hemisphere_image_urls = []
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    results = soup.find_all('div', class_='item')
    for result in results:
        #find title with first url
        title = result.find('h3').text
    
        #click the title link to find full res image
        browser.click_link_by_partial_text(title)
    
        #save the new url to get full res image url
        new_html = browser.html
        new_soup = BeautifulSoup(new_html, 'html.parser')
        partial_url = new_soup.find('img', class_="wide-image")['src']
        img_url = url + partial_url
    
        #go back to previous page for next title and image
        browser.back()
    
        # Dictionary to be inserted into list
        post = {
            'title': title,
            'img_url': img_url,
        }
        hemisphere_image_urls.append(post)

    #store data in dictionary
    mars_data = {
        "news_title" : news_title,
        "news_subtitle" : news_subtitle,
        "featured_image_url" : featured_image_url,
        "mars_table_html" : mars_table_html,
        "hemisphere_image_urls" : hemisphere_image_urls
    }

    # Close the browser after scraping
    browser.quit()

    # Return results
    return mars_data