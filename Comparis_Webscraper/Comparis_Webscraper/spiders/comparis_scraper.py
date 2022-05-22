# Scrapy
from numpy import append
from pandas import read_csv
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import Selector

from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

# Selenium
import selenium
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver

from selenium.common.exceptions import NoSuchElementException

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

# Other
import csv
import pandas as pd


# From our items.py file we import the item classes
from Comparis_Webscraper.items import ComparisWebscraperItem
#from comparis.items import PropertyEquipment
from scrapy.loader import ItemLoader

#driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))    


class Comparis_Spider(scrapy.Spider):
    name = 'real-estate'
    start_urls = ['https://httpbin.org/']

    def parse_pages(self, response):

        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))    

        property_codes = pd.read_csv(filepath_or_buffer='/Users/gino/University-and-Education/UNIL/Advanced-Programming/Comparis_Webscraper/Comparis_Webscraper/spiders/property_codes.csv')
    
        for url in property_codes['url']:
            self.driver.get(url)
            sleep(2)
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            sleep(1)

            scrapy_selector = Selector(text = self.driver.page_source)


            yield {
                'address': scrapy_selector.xpath('//h3[@class="css-yidf68 ehesakb2"]')
                
            }

            sleep(1)
            
      #scrapy_selector = Selector(text = self.driver.page_source)


        
