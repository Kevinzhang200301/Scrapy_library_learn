# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.pipelines.images import ImagesPipeline
from Picture360.settings import IMAGES_STORE as images_store
import scrapy
import os

class Picture360Pipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        image_link = item['image_link']
        yield scrapy.Request(image_link)

    # def process_item(self, item, spider):
    #     return item
    def item_completed(self, results, item, info):
        print(results)
        image_path = [x['path'] for _, x in results if _]
        print('*'*20)
        print(image_path)
        os.rename(images_store + image_path[0], images_store + item['name'] + '.jpg')
        return item