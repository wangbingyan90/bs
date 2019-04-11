# -*- coding: utf-8 -*-
from scrapy import Request, Spider
import datetime
import json

class _36krSpider(Spider):
    name = '36kr'
    allowed_domains = ['36kr.com']
    main_url = 'https://36kr.com/api/search-column/mainsite?per_page=20&page={count}'
    content_url = 'https://36kr.com/api/post/{id}/next'
    def start_requests(self):
        for count in range(1, 2):
            yield Request(self.main_url.format(count=count), callback=self.parse_main)


    def parse_main(self, response):
        """
        主页查看
        :param response:Response对象
        :return:
        """
        result = json.loads(response.text)
        if result.get('data').get('items'):
            items = result.get('data').get('items')
            for item in items:
                yield Request(self.content_url.format(id=item.get('id')), callback=self.parse_content)


    def parse_content(self, response):
        result = json.loads(response.text)
        if result.get('data'):
            self.logger.debug(result.get('data').get('title'))