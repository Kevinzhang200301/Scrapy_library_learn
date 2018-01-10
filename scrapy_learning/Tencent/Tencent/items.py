# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TencentItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #职位名称
    #//td[1]/a/text()
    positionName = scrapy.Field()
    #职位链接
    positionLink = scrapy.Field()
    #//td[1]/a/@href
    #职位类别
    positionType = scrapy.Field()
    #//td[2]/text()
    #招聘人数
    peopleNumber = scrapy.Field()
    #//td[3]/text()
    #招聘地点
    workLocation = scrapy.Field()
    #//td[4]/text()
    #发布时间
    publishTime = scrapy.Field()
    #//td[5]/text()
    pass



