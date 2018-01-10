# -*- coding: utf-8 -*-
import scrapy
from toscrape_book.items import ToscrapeBookItem

class BooksSpider(scrapy.Spider):
    name = 'books'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['http://books.toscrape.com/']

    def parse(self, response):
        books = response.xpath("//div[@class='image_container']/a/@href").extract()
        for book in books:
            url = response.urljoin(book)
            yield scrapy.Request(url, callback=self.parse_book)

        # #next page
        # if response.xpath("//ul[@class='pager']/li[@class='next']"):
        #     next_link = response.xpath("//ul[@class='pager']/li[@class='next']/a/@href").extract_first()
        #     next_link = response.urljoin(next_link)
        #     yield scrapy.Request(next_link, callback=self.parse)

    def parse_book(self, response):
        item = ToscrapeBookItem()
        item['name'] = response.xpath("//div[@class='col-sm-6 product_main']/h1/text()").extract_first()
        item['price'] = response.xpath("//div[@class='col-sm-6 product_main']/p[1]/text()").extract_first()
        item['review_rating'] = response.css('p.star-rating::attr(class)').re_first('star-rating ([A-Za-z]+)')
        item['review_num'] = response.xpath("//table[@class='table table-striped']/tr[last()-1]/td").re_first('\((\d+) available\)')
        item['upc'] = response.xpath("//table[@class='table table-striped']/tr[1]/td/text()").extract_first()
        item['stock'] = response.xpath("//table[@class='table table-striped']/tr[last()]/td/text()").extract_first()

        yield item

