# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MyautoItem(scrapy.Item):
    title = scrapy.Field()
    phone = scrapy.Field()
    real_phone = scrapy.Field()
    product_id = scrapy.Field()
    engine = scrapy.Field()
    location = scrapy.Field()
    price = scrapy.Field()




