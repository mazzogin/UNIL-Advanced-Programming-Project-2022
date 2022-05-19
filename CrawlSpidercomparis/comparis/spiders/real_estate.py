from gc import callbacks
import re
from urllib import response
import scrapy
from scrapy import Request
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
import json

from comparis.items import PropertyItem
#from comparis.items import PropertyEquipment
from scrapy.loader import ItemLoader

# https://fr.comparis.ch/immobilien/result/list?requestobject=%7B%22DealType%22%3A20%2C%22SiteId%22%3A0%2C%22RootPropertyTypes%22%3A%5B%5D%2C%22PropertyTypes%22%3A%5B%5D%2C%22RoomsFrom%22%3Anull%2C%22RoomsTo%22%3Anull%2C%22FloorSearchType%22%3A0%2C%22LivingSpaceFrom%22%3Anull%2C%22LivingSpaceTo%22%3Anull%2C%22PriceFrom%22%3Anull%2C%22PriceTo%22%3Anull%2C%22ComparisPointsMin%22%3A0%2C%22AdAgeMax%22%3A0%2C%22AdAgeInHoursMax%22%3Anull%2C%22Keyword%22%3A%22%22%2C%22WithImagesOnly%22%3Anull%2C%22WithPointsOnly%22%3Anull%2C%22Radius%22%3A%2210%22%2C%22MinAvailableDate%22%3A%221753-01-01T00%3A00%3A00%22%2C%22MinChangeDate%22%3A%221753-01-01T00%3A00%3A00%22%2C%22LocationSearchString%22%3A%22Lausanne%22%2C%22Sort%22%3A3%2C%22HasBalcony%22%3Afalse%2C%22HasTerrace%22%3Afalse%2C%22HasFireplace%22%3Afalse%2C%22HasDishwasher%22%3Afalse%2C%22HasWashingMachine%22%3Afalse%2C%22HasLift%22%3Afalse%2C%22HasParking%22%3Afalse%2C%22PetsAllowed%22%3Afalse%2C%22MinergieCertified%22%3Afalse%2C%22WheelchairAccessible%22%3Afalse%2C%22LowerLeftLatitude%22%3Anull%2C%22LowerLeftLongitude%22%3Anull%2C%22UpperRightLatitude%22%3Anull%2C%22UpperRightLongitude%22%3Anull%7D
# https://fr.comparis.ch/immobilien/marktplatz/details/show/27854674
# https://fr.comparis.ch/immobilien/marktplatz/details/show/27851872

# The one I used for my successful try
# 'https://www.comparis.ch/immobilien/marktplatz/lausanne/kaufen?sort=11'

# Xpath to every link //a[@class='css-a0dqn4 ehesakb1']

# Xpath to details on every product page //p[@class='css-1ush3w6 ehesakb2']/span[last()]

# Type  (//p[@class='css-1ush3w6 ehesakb2']/span[last()])[1]
# Rooms  (//p[@class='css-1ush3w6 ehesakb2']/span[last()])[2]
# Étage (//p[@class='css-1ush3w6 ehesakb2']/span[last()])[3]
# m2 (//p[@class='css-1ush3w6 ehesakb2']/span[last()])[4]
# Construction_Year (//p[@class='css-1ush3w6 ehesakb2']/span[last()])[5]
# Available From (//p[@class='css-1ush3w6 ehesakb2']/span[last()])[6]

# Address //h5[@class='css-15z12tn ehesakb2']
# Price //h3[@class="css-eujsoq ehesakb2"]

# json containing all the data: //script[@type="application/json"]


class RealEstateSpider(CrawlSpider):
    name = 'real-estate'
    allowed_domains = ['comparis.ch']
    start_urls = ['https://fr.comparis.ch/immobilien/result/list?requestobject=%7B%22DealType%22%3A20%2C%22SiteId%22%3A0%2C%22RootPropertyTypes%22%3A%5B%5D%2C%22PropertyTypes%22%3A%5B%5D%2C%22RoomsFrom%22%3Anull%2C%22RoomsTo%22%3Anull%2C%22FloorSearchType%22%3A0%2C%22LivingSpaceFrom%22%3Anull%2C%22LivingSpaceTo%22%3Anull%2C%22PriceFrom%22%3Anull%2C%22PriceTo%22%3Anull%2C%22ComparisPointsMin%22%3A0%2C%22AdAgeMax%22%3A0%2C%22AdAgeInHoursMax%22%3Anull%2C%22Keyword%22%3A%22%22%2C%22WithImagesOnly%22%3Anull%2C%22WithPointsOnly%22%3Anull%2C%22Radius%22%3Anull%2C%22MinAvailableDate%22%3A%221753-01-01T00%3A00%3A00%22%2C%22MinChangeDate%22%3A%221753-01-01T00%3A00%3A00%22%2C%22LocationSearchString%22%3A%228005%22%2C%22Sort%22%3A11%2C%22HasBalcony%22%3Afalse%2C%22HasTerrace%22%3Afalse%2C%22HasFireplace%22%3Afalse%2C%22HasDishwasher%22%3Afalse%2C%22HasWashingMachine%22%3Afalse%2C%22HasLift%22%3Afalse%2C%22HasParking%22%3Afalse%2C%22PetsAllowed%22%3Afalse%2C%22MinergieCertified%22%3Afalse%2C%22WheelchairAccessible%22%3Afalse%2C%22LowerLeftLatitude%22%3Anull%2C%22LowerLeftLongitude%22%3Anull%2C%22UpperRightLatitude%22%3Anull%2C%22UpperRightLongitude%22%3Anull%7D&sort=11']

    headers = {
        # Taken from url. Go to browser and enter url, then right click on website, inspect > Network > Request Headers, then copy and paste
        # User-Agent was amended
        'authority': 'en.comparis.ch',
        'method': 'GET',
        'path': '/immobilien/result/list?requestobject=%7B%22DealType%22%3A20%2C%22SiteId%22%3A0%2C%22RootPropertyTypes%22%3A%5B%5D%2C%22PropertyTypes%22%3A%5B%5D%2C%22RoomsFrom%22%3Anull%2C%22RoomsTo%22%3Anull%2C%22FloorSearchType%22%3A0%2C%22LivingSpaceFrom%22%3Anull%2C%22LivingSpaceTo%22%3Anull%2C%22PriceFrom%22%3Anull%2C%22PriceTo%22%3Anull%2C%22ComparisPointsMin%22%3A0%2C%22AdAgeMax%22%3A0%2C%22AdAgeInHoursMax%22%3Anull%2C%22Keyword%22%3A%22%22%2C%22WithImagesOnly%22%3Anull%2C%22WithPointsOnly%22%3Anull%2C%22Radius%22%3A%2210%22%2C%22MinAvailableDate%22%3A%221753-01-01T00%3A00%3A00%22%2C%22MinChangeDate%22%3A%221753-01-01T00%3A00%3A00%22%2C%22LocationSearchString%22%3A%22Lausanne%22%2C%22Sort%22%3A11%2C%22HasBalcony%22%3Afalse%2C%22HasTerrace%22%3Afalse%2C%22HasFireplace%22%3Afalse%2C%22HasDishwasher%22%3Afalse%2C%22HasWashingMachine%22%3Afalse%2C%22HasLift%22%3Afalse%2C%22HasParking%22%3Afalse%2C%22PetsAllowed%22%3Afalse%2C%22MinergieCertified%22%3Afalse%2C%22WheelchairAccessible%22%3Afalse%2C%22LowerLeftLatitude%22%3Anull%2C%22LowerLeftLongitude%22%3Anull%2C%22UpperRightLatitude%22%3Anull%2C%22UpperRightLongitude%22%3Anull%7D',
        'scheme': 'https',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7,it;q=0.6',
        'cache-control': 'max-age=0',
        # Cookie was deleted, since they are not really used.
        # In any case, if we had to use cookies, we would need to use a separate dictionary with the cookies
        'sec-ch-ua': ' " Not A;Brand";v="99", "Chromium";v="101", "Google Chrome";v="101" ',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        # Check your headers here and change if necessary: http://myhttpheader.com/
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36'
        }

    rules = (
        Rule(LinkExtractor(allow='details', deny='show')),
        Rule(LinkExtractor(allow='show'), callback='parse_item')
    )

    def parse_item(self, response):
        l = ItemLoader(item = PropertyItem(), response = response)

        l.add_css('address', 'h5.css-15z12tn.ehesakb2')
        l.add_xpath('price', '//h3[@class="css-eujsoq ehesakb2"]')
        l.add_xpath('type', '(//p[@class="css-1ush3w6 ehesakb2"]/span[last()])[1]')
        l.add_xpath('rooms', '(//p[@class="css-1ush3w6 ehesakb2"]/span[last()])[2]')
        l.add_xpath('floors', '(//p[@class="css-1ush3w6 ehesakb2"]/span[last()])[3]')
        l.add_xpath('sq_meters', '(//p[@class="css-1ush3w6 ehesakb2"]/span[last()])[4]')
        l.add_xpath('contruction_year', '(//p[@class="css-1ush3w6 ehesakb2"]/span[last()])[5]')
        l.add_xpath('available_from', '(//p[@class="css-1ush3w6 ehesakb2"]/span[last()])[6]')
        # Binary Data (Is present = true, is not present/no information = '')
        l.add_xpath('balcony', '//div[@class="css-16pvz65 ehesakb5"]/div[contains(.,"Balcon")]')
        l.add_xpath('parking_ext', '//div[@class="css-16pvz65 ehesakb5"]/div[contains(.,"Parking extérieur")]')
        l.add_xpath('parking_int', '//div[@class="css-16pvz65 ehesakb5"]/div[contains(.,"Parking intérieur")]')
        l.add_xpath('tv', '//div[@class="css-16pvz65 ehesakb5"]/div[contains(.,"TV")]')
        l.add_xpath('elevator', '//div[@class="css-16pvz65 ehesakb5"]/div[contains(.,"Ascenseur")]')
        l.add_xpath('wash_m', '//div[@class="css-16pvz65 ehesakb5"]/div[contains(.,"Lave-linge")]')
        l.add_xpath('dishwasher', '//div[@class="css-16pvz65 ehesakb5"]/div[contains(.,"Lave-vaisselle")]')
        l.add_xpath('dryer', '//div[@class="css-16pvz65 ehesakb5"]/div[contains(.,"Sèche-linge")]')
        
        
        
        
        
        

        # XPATH for critères //div[@class="css-16pvz65 ehesakb5"]/div[contains(.,"Jardin")]
        # "Equipements containts" XPATH //div[@class="css-k3nek6 ehesakb4"]/div[contains(.,"Ascenseur")]
        
        yield l.load_item()
