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

from scrapy.loader import ItemLoader
from Comparis_Webscraper.items import ComparisWebscraperItem
#from comparis.items import PropertyEquipment


class Comparis_Spider(scrapy.Spider):
    name = 'real-estate'
    start_urls = ['https://httpbin.org/']

    def parse(self, response):
        self.property_codes = pd.read_csv(filepath_or_buffer='/Users/gino/University-and-Education/UNIL/Advanced-Programming/Comparis_Webscraper/Comparis_Webscraper/spiders/property_codes.csv')
        #l = ItemLoader(item = ComparisWebscraperItem(), response = response)
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        
        for url in self.property_codes['url']:
            self.driver.get(url)
            sleep(2)
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            sleep(1.4)
            
            scrapy_selector = Selector(text = self.driver.page_source)


            l = ItemLoader(item = ComparisWebscraperItem(), selector = scrapy_selector)
            l.add_xpath('rooms', '(//p[@class="css-1ush3w6 ehesakb2"]/span[last()])[2]')

            yield l.load_item()

            
      #scrapy_selector = Selector(text = self.driver.page_source)


        
