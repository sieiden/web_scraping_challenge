# web_scraping_challenge
NW Bootcamp Web Scraping HW

**Web Scraping in Jupyter Notebook**

The Jupyter Notebook in this repository contains the exploratory code to scrape various websites for facts, images, and news about Mars using Splinter including:

1. The most recent NASA news from https://redplanetscience.com/

2. Featured image URL from https://redplanetscience.com/

3. Image URLs for Mars' 4 hemispheres from https://marshemispheres.com/

4. Mars facts table from https://galaxyfacts-mars.com/

The exploratory analysis was then transfered into a Flask app using VSCode to run the python app.

**Flask App**

The Flask app was designed as an app.py file that was deployed using VS Code and my local server.

The "/" route loads the initial webpage. After clicking the button "Scrape" on the website, the "/scrape" route calls an external python module (scrape_nasa.py) which scrapes each of the above websites for its designated information. The information is then saved in a MongoDB collection which is loaded to the webpage using jinja.

![mongo_db_post_scrape](https://user-images.githubusercontent.com/68086211/117593575-d0bc0a00-b101-11eb-9f22-188b04042482.png)


**Web Design/Jinja**

1. The landing page loads before scraping and includes a button to the scrape route

![app_pre_scrape](https://user-images.githubusercontent.com/68086211/117593506-8f2b5f00-b101-11eb-8aff-8e9992a84b90.png)

2. Data is loaded to the variable by the flask app (*Note the final three hemisphere images rendered below the cut off for the screen shot)

![app_post_scrape](https://user-images.githubusercontent.com/68086211/117593559-c3068480-b101-11eb-80c2-8e17694eb519.png)

3. Facts table renders correctly

![mars_table](https://user-images.githubusercontent.com/68086211/117593640-ffd27b80-b101-11eb-995b-bcb1aa737e09.png)
