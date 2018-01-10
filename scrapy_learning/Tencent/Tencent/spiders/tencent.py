# -*- coding: utf-8 -*-
import scrapy
from Tencent.items import TencentItem

class TencentSpider(scrapy.Spider):
    name = 'tencent'
    allowed_domains = ['tencent.com']
    start_urls = ['http://hr.tencent.com/position.php?keywords=&tid=0&start=0']

    def parse(self, response):
        node_list = response.xpath("//tr[@class='even'] | //tr[@class='odd']")
        item = TencentItem()
        for node in node_list:
            #import pdb; pdb.set_trace()
            item['positionName'] = node.xpath("td[1]/a/text()").extract()[0]
            item['positionLink'] = node.xpath("td[1]/a/@href").extract()[0]
            if len(node.xpath("td[2]/text()")):
                item['positionType'] = node.xpath("td[2]/text()").extract()[0]
            else:
                item['positionType'] = ""
            item['peopleNumber'] = node.xpath("td[3]/text()").extract()[0]
            item['workLocation'] = node.xpath("td[4]/text()").extract()[0]
            item['publishTime'] = node.xpath("td[5]/text()").extract()[0]

            yield item
        if len(response.xpath("//a[@id='next' and @class='noactive']")) == 0:
            url = response.xpath("//a[@id='next']/@href").extract()[0]
            print("The next url: {}".format(url))
            yield scrapy.Request("http://hr.tencent.com/"+url, callback=self.parse)



