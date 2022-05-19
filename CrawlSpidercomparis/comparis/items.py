# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader import ItemLoader
from itemloaders.processors import TakeFirst, MapCompose, Join, Compose
from w3lib.html import remove_tags

def remove_string(value):
    """
    Removes a string of html code that is always left over when extracting the data
    """
    return value.replace('.css-ykqdxu{cursor:inherit;}.css-1y5nuta{box-sizing:border-box;margin-right:0.8rem;cursor:inherit;}','').strip()

def remove_string_currency(value):
    """
    Removes a string of html code that is always left over when extracting the data
    """
    return value.replace('.css-1my9a6m{box-sizing:border-box;margin-left:0.4rem;font-size:1.4rem;font-weight:300;display:inline;}@media screen and (min-width: 46.25em){.css-1my9a6m{font-size:1.6rem;}}','').strip()

def remove_currency(value):
    """
    Removes the CHF string and and leaves only the number
    """
    return value.replace('CHF','').strip()

def remove_sqm(value):
    """
    Removes the square meter sign and leaves only the number
    """
    return value.replace('m²','').strip()

def remove_comma(value):
    """
    Removes any comma value
    """
    return value.replace(',','').strip()

def parse_equipment(equipment):
    return 'None' if equipment == None else True





class PropertyItem(scrapy.Item):
    # define the fields for your item here like:
    address = scrapy.Field(
        input_processor = MapCompose(remove_tags, remove_string, remove_comma), 
        output_processor = Join())
    
    price = scrapy.Field(
        input_processor = MapCompose(remove_tags, remove_currency, remove_string_currency, remove_comma), 
        output_processor = TakeFirst())
    
    type = scrapy.Field(
        input_processor = MapCompose(remove_tags, remove_comma), 
        output_processor = TakeFirst())
    
    rooms = scrapy.Field(
        input_processor = MapCompose(remove_tags, remove_comma), 
        output_processor = TakeFirst())
    
    floors = scrapy.Field(
        input_processor = MapCompose(remove_tags, remove_comma), 
        output_processor = TakeFirst())
    
    sq_meters = scrapy.Field(
        input_processor = MapCompose(remove_tags, remove_sqm, remove_comma), 
        output_processor = TakeFirst())
    
    contruction_year = scrapy.Field(
        input_processor = MapCompose(remove_tags, remove_comma), 
        output_processor = TakeFirst())
    
    available_from = scrapy.Field(
        input_processor = MapCompose(remove_tags, remove_comma), 
        output_processor = TakeFirst())
    
    balcony =  scrapy.Field(
        input_processor = MapCompose(remove_tags, parse_equipment),
        output_processor = TakeFirst())

    parking_ext =  scrapy.Field(
        input_processor = MapCompose(remove_tags, parse_equipment),
        output_processor = TakeFirst())

    parking_int =  scrapy.Field(
        input_processor = MapCompose(remove_tags, parse_equipment),
        output_processor = TakeFirst())

    tv = scrapy.Field(
        input_processor = MapCompose(remove_tags, parse_equipment),
        output_processor = TakeFirst())

    elevator  =  scrapy.Field(
        input_processor = MapCompose(remove_tags, parse_equipment),
        output_processor = TakeFirst())
    
    wash_m  =  scrapy.Field(
        input_processor = MapCompose(remove_tags, parse_equipment),
        output_processor = TakeFirst())
    
    dishwasher  =  scrapy.Field(
        input_processor = MapCompose(remove_tags, parse_equipment),
        output_processor = TakeFirst())
    
    dryer  =  scrapy.Field(
        input_processor = MapCompose(remove_tags, parse_equipment),
        output_processor = TakeFirst())
    


    # Maybe add a second itemloader and then add the response to the parse_item?
    


        # p class="css-cyiock ehesakb2
        # //P[@class="css-cyiock ehesakb2"]