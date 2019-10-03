# -*- coding: utf-8 -*-
import scrapy


class TestspiderSpider(scrapy.Spider):
    name = 'testspider'
    allowed_domains = ['iscast.com']
    start_urls = ['http://iscast.com/']

    def parse(self, response):
        a = print("hello")
