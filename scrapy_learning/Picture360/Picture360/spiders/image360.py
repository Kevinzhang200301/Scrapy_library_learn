# -*- coding: utf-8 -*-
import scrapy
import json
from Picture360.items import Picture360Item

class Image360Spider(scrapy.Spider):
    name = 'image360'
    allowed_domains = ['image.so.com']
    offset = 30
    start_urls = ['http://image.so.com/zj?ch=beauty&sn=%d&listtype=new&temp=1' % offset]

    def parse(self, response):
        item  = Picture360Item()
        res = json.loads(response.body.decode('utf8'))
        image_lists = res['list']
        for image in image_lists:
            item['name'] = image['group_title']
            item['image_link'] = image['cover_imgurl']
            print(item)
            yield item

        if json.loads(response.body)['count']:
            self.offset += 30
            url = "http://image.so.com/zj?ch=beauty&sn=%d&listtype=new&temp=1" % self.offset
            yield scrapy.Request(url, callback=self.parse)
