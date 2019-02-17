# -*- coding: utf-8 -*-
import scrapy
import datetime


class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/page/1/']

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'quotes-%s.html' % page
        filename = filename + str(datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S'))
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)
