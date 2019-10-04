# -*- coding: utf-8 -*-
import scrapy
from myscrapy.items import MyscrapyItem


class TestspiderSpider(scrapy.Spider):
    name = 'testspider'
    allowed_domains = ['huxiu.com']
    start_urls = ['http://huxiu.com/index.php']

    def parse(self, response):
        for sel in response.xpath('//div[@class="mod-info-flow"]/div/div[@class="mob-ctt"]'):
            item = MyscrapyItem()
            item['title'] = sel.xpath('h3/a/text()')[0].extract()
            print(item['title'])
