# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader import ItemLoader
from itemloaders.processors import TakeFirst, MapCompose
from w3lib.html import remove_tags

def remove_string(value):
    return value.replace('.css-ykqdxu{cursor:inherit;}.css-1y5nuta{box-sizing:border-box;margin-right:0.8rem;cursor:inherit;}','').strip()

def remove_string_currency(value):
    return value.replace('.css-1my9a6m{box-sizing:border-box;margin-left:0.4rem;font-size:1.4rem;font-weight:300;display:inline;}@media screen and (min-width: 46.25em){.css-1my9a6m{font-size:1.6rem;}}','').strip()

def remove_currency(value):
    return value.replace('CHF','').strip()

def remove_sqm(value):
    return value.replace('m²','').strip()

def remove_comma(value):
    return value.replace(',','').strip()


class PropertyItem(scrapy.Item):
    # define the fields for your item here like:
    address = scrapy.Field(input_processor = MapCompose(remove_tags, remove_string, remove_comma), output_processor = TakeFirst())
    price = scrapy.Field(input_processor = MapCompose(remove_tags, remove_currency, remove_string_currency, remove_comma), output_processor = TakeFirst())
    type = scrapy.Field(input_processor = MapCompose(remove_tags, remove_comma), output_processor = TakeFirst())
    rooms = scrapy.Field(input_processor = MapCompose(remove_tags, remove_comma), output_processor = TakeFirst())
    floors = scrapy.Field(input_processor = MapCompose(remove_tags, remove_comma), output_processor = TakeFirst())
    sq_meters = scrapy.Field(input_processor = MapCompose(remove_tags, remove_sqm, remove_comma), output_processor = TakeFirst())
    contruction_year = scrapy.Field(input_processor = MapCompose(remove_tags, remove_comma), output_processor = TakeFirst())
    available_from = scrapy.Field(input_processor = MapCompose(remove_tags, remove_comma), output_processor = TakeFirst())