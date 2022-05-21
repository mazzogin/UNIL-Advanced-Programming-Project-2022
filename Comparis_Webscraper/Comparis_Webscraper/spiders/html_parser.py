import scrapy
from scrapy import Request
from scrapy.loader import ItemLoader

class TestSpider(scrapy.Spider):
    name = 'htmlparser'
    start_urls = ['file:///Users/gino/University-and-Education/UNIL/Advanced-Programming/data/Comparis_Start_URL.html']
    
    def parse(self, response):
        codes = response.css('script').re_first('{\"adIds\":\[(.+?)]')
        all_codes = [code for code in codes.split(',')] if codes else []
        for code in all_codes:
            yield {
                'Property_Codes': code,
                'url': f'https://en.comparis.ch/immobilien/marktplatz/details/show/{code}',
            }