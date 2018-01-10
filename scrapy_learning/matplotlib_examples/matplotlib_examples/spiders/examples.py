# -*- coding: utf-8 -*-
import scrapy
from matplotlib_examples.items import MatplotlibExamplesItem

class ExamplesSpider(scrapy.Spider):
    name = 'examples'
    allowed_domains = ['matplotlib.org']
    start_urls = ['http://matplotlib.org/examples/index.html']

    def parse(self, response):
        links_temp = response.xpath("//div[@class='toctree-wrapper compound']//li[@class='toctree-l2']/a/@href")
        links = [response.urljoin(link.extract()) for link in links_temp]
        for url in links:
            print(url)
            yield scrapy.Request(url, callback=self.parse_file)

    def parse_file(self,response):
        item = MatplotlibExamplesItem()
        item['file_urls'] = []
        example_url = response.xpath("//a[@class='reference external']/@href").extract_first()
        item['file_urls'].append(response.urljoin(example_url))
        #item['files'] =
        yield item