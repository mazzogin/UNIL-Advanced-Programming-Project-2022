# Scrapy
import scrapy
from scrapy import Request
from scrapy.selector import Selector

# Selenium / Selenium related
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from time import sleep

# Other
from datetime import date

###
# Define Scrapy Spider
###

class Property_ID_spider(scrapy.Spider):
    """
    Downloads the unique ID's of every property of a predefined URL.

    As input it takes the URL of a comparis overview website.
    As output it generates a csv with two columns: code (the property ID) and the URL of every single property.
    """

    # Name the spider (callable from command line)
    name = 'id-scraper'

    # Just provide a website to which scrapy can connect for sure
    start_urls = ['https://httpbin.org/']
    
    # Set the location and format of the output. 
    # Output is a csv, the name changes based on the current date. Output directory is 'data'
    custom_settings = {'FEEDS': {f'../../../data/property_codes_{date.today()}.csv':{'format':'csv'}}}

    def parse(self, response):

        # Define Chrome as browser
        # The driver installs/updates automatically thanks to ChromeDriverManager
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        
        # Set URL
        # url is created by searching for property to buy within a radius of 10km in Lausanne
        url = 'https://fr.comparis.ch/immobilien/result/list?requestobject=%7B%22DealType%22%3A20%2C%22SiteId%22%3A0%2C%22RootPropertyTypes%22%3A%5B%5D%2C%22PropertyTypes%22%3A%5B%5D%2C%22RoomsFrom%22%3Anull%2C%22RoomsTo%22%3Anull%2C%22FloorSearchType%22%3A0%2C%22LivingSpaceFrom%22%3Anull%2C%22LivingSpaceTo%22%3Anull%2C%22PriceFrom%22%3Anull%2C%22PriceTo%22%3Anull%2C%22ComparisPointsMin%22%3A0%2C%22AdAgeMax%22%3A0%2C%22AdAgeInHoursMax%22%3Anull%2C%22Keyword%22%3A%22%22%2C%22WithImagesOnly%22%3Anull%2C%22WithPointsOnly%22%3Anull%2C%22Radius%22%3A%2210%22%2C%22MinAvailableDate%22%3A%221753-01-01T00%3A00%3A00%22%2C%22MinChangeDate%22%3A%221753-01-01T00%3A00%3A00%22%2C%22LocationSearchString%22%3A%22Lausanne%22%2C%22Sort%22%3A11%2C%22HasBalcony%22%3Afalse%2C%22HasTerrace%22%3Afalse%2C%22HasFireplace%22%3Afalse%2C%22HasDishwasher%22%3Afalse%2C%22HasWashingMachine%22%3Afalse%2C%22HasLift%22%3Afalse%2C%22HasParking%22%3Afalse%2C%22PetsAllowed%22%3Afalse%2C%22MinergieCertified%22%3Afalse%2C%22WheelchairAccessible%22%3Afalse%2C%22LowerLeftLatitude%22%3Anull%2C%22LowerLeftLongitude%22%3Anull%2C%22UpperRightLatitude%22%3Anull%2C%22UpperRightLongitude%22%3Anull%7D'
        
        # Navigate to URL
        self.driver.get(url)
        # Rest for 0.8 seconds
        sleep(0.8)
        
        # Scroll to end of website to activate the javascript
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Rest for another 1.2 seconds to ensure javascript has loaded
        sleep(1.2)

        # Set the scrapy selector.
        # In order to navigate the html (source code) with scrapy selectors 
        # (which instances of class 'Selector'), we need to define the selenium
        # page source as class Selector.
        scrapy_selector = Selector(text = self.driver.page_source)

        # The ID's of every property fitting the search request are stored at the very bottom
        # of the html. Below we select this part of the html with a (scrapy) css selector.
        codes = scrapy_selector.css('script').re_first('{\"adIds\":\[(.+?)]')

        # A brief bit of list copmrehension will split the values where the commas are
        all_codes = [code for code in codes.split(',')] if codes else []

        # yield every single code (ID) as well as the corresponding 
        # url by attaching the code at the end of an url using the f-string below.
        for code in all_codes:
            yield {
                'Property_Codes': code,
                'url': f'https://fr.comparis.ch/immobilien/marktplatz/details/show/{code}',
            }

        # Quit the selenium webdriver
        self.driver.quit()