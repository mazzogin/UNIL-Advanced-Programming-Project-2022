from gc import callbacks
import re
from urllib import response
import scrapy
from scrapy import Request
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
import json
from random import choice

# From our items.py file we import the item classes
from comparis.items import PropertyItem
#from comparis.items import PropertyEquipment
from scrapy.loader import ItemLoader

from proxies import get_working_proxies
# possibilities:
# 1. Manually pass in the property codes found in the json file at the end of the website

# https://fr.comparis.ch/immobilien/result/list?requestobject=%7B%22DealType%22%3A20%2C%22SiteId%22%3A0%2C%22RootPropertyTypes%22%3A%5B%5D%2C%22PropertyTypes%22%3A%5B%5D%2C%22RoomsFrom%22%3Anull%2C%22RoomsTo%22%3Anull%2C%22FloorSearchType%22%3A0%2C%22LivingSpaceFrom%22%3Anull%2C%22LivingSpaceTo%22%3Anull%2C%22PriceFrom%22%3Anull%2C%22PriceTo%22%3Anull%2C%22ComparisPointsMin%22%3A0%2C%22AdAgeMax%22%3A0%2C%22AdAgeInHoursMax%22%3Anull%2C%22Keyword%22%3A%22%22%2C%22WithImagesOnly%22%3Anull%2C%22WithPointsOnly%22%3Anull%2C%22Radius%22%3A%2210%22%2C%22MinAvailableDate%22%3A%221753-01-01T00%3A00%3A00%22%2C%22MinChangeDate%22%3A%221753-01-01T00%3A00%3A00%22%2C%22LocationSearchString%22%3A%22Lausanne%22%2C%22Sort%22%3A3%2C%22HasBalcony%22%3Afalse%2C%22HasTerrace%22%3Afalse%2C%22HasFireplace%22%3Afalse%2C%22HasDishwasher%22%3Afalse%2C%22HasWashingMachine%22%3Afalse%2C%22HasLift%22%3Afalse%2C%22HasParking%22%3Afalse%2C%22PetsAllowed%22%3Afalse%2C%22MinergieCertified%22%3Afalse%2C%22WheelchairAccessible%22%3Afalse%2C%22LowerLeftLatitude%22%3Anull%2C%22LowerLeftLongitude%22%3Anull%2C%22UpperRightLatitude%22%3Anull%2C%22UpperRightLongitude%22%3Anull%7D
# https://fr.comparis.ch/immobilien/marktplatz/details/show/27854674
# https://fr.comparis.ch/immobilien/marktplatz/details/show/27851872

# The one I used for my successful try
# 'https://www.comparis.ch/immobilien/marktplatz/lausanne/kaufen?sort=11'

class RealEstateSpider(scrapy.Spider):
    def __init__(self, name='real-estate', **kwargs):
        super(RealEstateSpider, self).__init__(name, **kwargs)
        #self.proxy_pool = choice(get_working_proxies())

    name = 'real-estate'
    url = ['https://fr.comparis.ch/immobilien/result/list?requestobject=%7B%22DealType%22%3A20%2C%22SiteId%22%3A0%2C%22RootPropertyTypes%22%3A%5B%5D%2C%22PropertyTypes%22%3A%5B%5D%2C%22RoomsFrom%22%3Anull%2C%22RoomsTo%22%3Anull%2C%22FloorSearchType%22%3A0%2C%22LivingSpaceFrom%22%3Anull%2C%22LivingSpaceTo%22%3Anull%2C%22PriceFrom%22%3Anull%2C%22PriceTo%22%3Anull%2C%22ComparisPointsMin%22%3A0%2C%22AdAgeMax%22%3A0%2C%22AdAgeInHoursMax%22%3Anull%2C%22Keyword%22%3A%22%22%2C%22WithImagesOnly%22%3Anull%2C%22WithPointsOnly%22%3Anull%2C%22Radius%22%3Anull%2C%22MinAvailableDate%22%3A%221753-01-01T00%3A00%3A00%22%2C%22MinChangeDate%22%3A%221753-01-01T00%3A00%3A00%22%2C%22LocationSearchString%22%3A%228005%22%2C%22Sort%22%3A11%2C%22HasBalcony%22%3Afalse%2C%22HasTerrace%22%3Afalse%2C%22HasFireplace%22%3Afalse%2C%22HasDishwasher%22%3Afalse%2C%22HasWashingMachine%22%3Afalse%2C%22HasLift%22%3Afalse%2C%22HasParking%22%3Afalse%2C%22PetsAllowed%22%3Afalse%2C%22MinergieCertified%22%3Afalse%2C%22WheelchairAccessible%22%3Afalse%2C%22LowerLeftLatitude%22%3Anull%2C%22LowerLeftLongitude%22%3Anull%2C%22UpperRightLatitude%22%3Anull%2C%22UpperRightLongitude%22%3Anull%7D&sort=11']
    custom_settings = {
        'HTTPPROXY_ENABLED' : True
    }


    def start_requests(self):
        yield Request(self.url)

    def parse(self, response):
        codes = response.css('script').re_first('{\"adIds\":\[(.+?)]')

        # List Comprehension
        all_codes = [code for code in codes.split(',')] if codes else []
        for code in all_codes:
            yield Request(
                url=f'https://en.comparis.ch/immobilien/marktplatz/details/show/{code}',
                callback=self.parse_general_information,
                meta = {'property_code_request':all_codes},
                )

    def parse_detail_page(self, response):
        
    
    def parse_general_information(self, response):
        l = ItemLoader(item = PropertyItem(), response = response)
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
        
        yield l.load_item()