# Scrapy
import scrapy
from scrapy.selector import Selector

# Selenium / Selenium related
import selenium
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from time import sleep

# Other
from numpy import append
from pandas import read_csv
from scrapy.loader import ItemLoader
from Comparis_Webscraper.items import ComparisWebscraperItem
from datetime import date
import pandas as pd

###
# Define Scrapy Spider
###

class Comparis_Spider(scrapy.Spider):
    """
    Downloads 22 different datapoints from a list of predefined comparis.ch url's
    
    The list of predefined url's can be found in the 'data' folder and is named 'property_codes_"YYYY-MM-DD"'
    This list may be changed by providing the 'id-scraper' a different URL.
    """

    # Name the spider (callable from command line)
    name = 'property-scraper'

    # Just provide a website to which scrapy can connect for sure
    start_urls = ['https://httpbin.org/']

    # Set the location and format of the output. 
    # Output is a csv, the name changes based on the current date. Output directory is 'data'
    custom_settings = {'FEEDS': {f'../../../data/property_details_{date.today()}.csv':{'format':'csv'}}}

    def parse(self, response):

        # Get list of url's
        self.property_codes = pd.read_csv(filepath_or_buffer='../../../data/property_codes.csv')

        # Define Chrome as browser
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        
        for url in self.property_codes['url']:
            # Navigate to url
            self.driver.get(url)
            sleep(0.8)

            # Scroll to end of website to activate the javascript
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            sleep(1.5)
            
            # Set the scrapy selector as in the id_scraper.py file
            scrapy_selector = Selector(text = self.driver.page_source)

            # The scraped fields get processed here.
            # Details on the input/output processing can be found in the items.py file
            l = ItemLoader(item = ComparisWebscraperItem(), selector = scrapy_selector)
            l.add_css('address', 'h5.css-15z12tn.ehesakb2')
            l.add_xpath('price', '//h3[@class="css-eujsoq ehesakb2"]')
            l.add_xpath('type', '(//p[@class="css-1ush3w6 ehesakb2"]/span[last()])[1]')
            l.add_xpath('rooms', '(//p[@class="css-1ush3w6 ehesakb2"]/span[last()])[2]')
            l.add_xpath('floors', '(//p[@class="css-1ush3w6 ehesakb2"]/span[last()])[3]')
            l.add_xpath('sq_meters', '(//p[@class="css-1ush3w6 ehesakb2"]/span[last()])[4]')
            l.add_xpath('contruction_year', '(//p[@class="css-1ush3w6 ehesakb2"]/span[last()])[5]')
            l.add_xpath('available_from', '(//p[@class="css-1ush3w6 ehesakb2"]/span[last()])[6]')
            # Binary Data (if present = true, is not present/no information = '')
            l.add_xpath('balcony', '//div[@class="css-16pvz65 ehesakb5"]/div[contains(.,"Balcon")]')
            l.add_xpath('parking_ext', '//div[@class="css-16pvz65 ehesakb5"]/div[contains(.,"Parking extérieur")]')
            l.add_xpath('parking_int', '//div[@class="css-16pvz65 ehesakb5"]/div[contains(.,"Parking intérieur")]')
            l.add_xpath('tv', '//div[@class="css-16pvz65 ehesakb5"]/div[contains(.,"TV")]')
            l.add_xpath('elevator', '//div[@class="css-16pvz65 ehesakb5"]/div[contains(.,"Ascenseur")]')
            l.add_xpath('wash_m', '//div[@class="css-16pvz65 ehesakb5"]/div[contains(.,"Lave-linge")]')
            l.add_xpath('dishwasher', '//div[@class="css-16pvz65 ehesakb5"]/div[contains(.,"Lave-vaisselle")]')
            l.add_xpath('dryer', '//div[@class="css-16pvz65 ehesakb5"]/div[contains(.,"Sèche-linge")]')
            # Critères Data
            l.add_xpath('public_transp', '//div[@class="css-84kz1r ehesakb5"]/div/div[contains(.,"Transports publics")]/div/div/following-sibling::div/p/span')
            l.add_xpath('highway', '//div[@class="css-84kz1r ehesakb5"]/div/div[contains(.,"Autoroute")]/div/div/following-sibling::div/p/span')
            l.add_xpath('kindergarten', '//div[@class="css-84kz1r ehesakb5"]/div/div[contains(.,"Jardin")]/div/div/following-sibling::div/p/span')
            l.add_xpath('prim_school', '//div[@class="css-84kz1r ehesakb5"]/div/div[contains(.,"École primaire")]/div/div/following-sibling::div/p/span')
            l.add_xpath('secon_school', '//div[@class="css-84kz1r ehesakb5"]/div/div[contains(.,"École secondaire")]/div/div/following-sibling::div/p/span')
            l.add_xpath('closest_shop', '//div[@class="css-84kz1r ehesakb5"]/div/div[contains(.,"Commerces")]/div/div/following-sibling::div/p/span')
            
            # Yield scraped data from 
            yield l.load_item()
        
        # Quit the selenium webdriver
        self.driver.quit()