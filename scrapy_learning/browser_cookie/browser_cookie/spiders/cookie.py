# -*- coding: utf-8 -*-
import scrapy
import json
from PIL import Image
import time
import os
from browser_cookie.items import BrowserCookieItem

class CookieSpider(scrapy.Spider):
    name = 'cookie'
    allowed_domains = ['www.zhihu.com']
    start_urls = ['https://www.zhihu.com/settings/profile']
    Agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'
    header = {'User-Agent': Agent}

    def start_requests(self):
        t = str(int(time.time() * 1000))
        captcha_url = 'https://www.zhihu.com/captcha.gif?r=' + t + '&type=login&lang=en'
        return [scrapy.Request(url=captcha_url, headers=self.header, callback=self.parser_captcha)]

    def parse(self, response):
        item = BrowserCookieItem()
        item['name'] = response.xpath("//div[@id='rename-section']/span/text()").extract_first()
        print(item)
        yield item

    def parser_captcha(self, response):
        with open('captcha.jpg', 'wb') as f:
            f.write(response.body)
            f.close()
        try:
            im = Image.open('captcha.jpg')
            im.show()
            im.close()
        except:
            print('path: %s' % os.path.abspath('captcha.jpn'))
        captcha = input('please input the captcha\n>')
        return scrapy.FormRequest(url='https://www.zhihu.com/#signin',headers=self.header,callback=self.login,meta={'captcha': captcha})

    def login(self,response):
        xsrf = response.xpath("//input[@name='_xsrf']/@value").extract_first()
        if xsrf is None:
            return ' '
        post_url = 'https://www.zhihu.com/login/phone_num'
        post_data = {
            "_xsrf": xsrf,
            #"email": 'sirzhangyu@gmail.com',
            'phone_num': '18583671578',
            "password": 'fengcheche1q',
            #"password": 'ZhngY1987)^!$',
            "captcha": response.meta['captcha']
        }
        return [scrapy.FormRequest(url=post_url, formdata=post_data, headers=self.header, callback=self.check_login)]

    def check_login(self, response):
        js = json.loads(response.text)
        print(js)
        if 'msg' in js and js['msg'] == '登录成功':
            for url in self.start_urls:
                yield scrapy.Request(url=url, headers=self.header, callback=self.parse)


