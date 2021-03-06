# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ToscrapeBookItem(scrapy.Item):
    name = scrapy.Field()

    price = scrapy.Field()

    review_rating = scrapy.Field()

    review_num = scrapy.Field()

    upc = scrapy.Field()

    stock = scrapy.Field()

