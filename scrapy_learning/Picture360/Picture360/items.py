# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Picture360Item(scrapy.Item):
    name = scrapy.Field()
    image_link = scrapy.Field()

