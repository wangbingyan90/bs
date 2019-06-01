# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql

class RedisscrapyPipeline(object):

    def __init__(self):
        self.db = pymysql.connect(host="127.0.0.1",user="root",password="root",db="bs",port=3306,charset="utf8")
        self.cursor = self.db.cursor()
    def process_item(self, item, spider):
        print("=============================")
        print(item.get("id"))
        sql="insert into new  values(%s,%s,%s,%s,%s,%s)"%(item.get('id'),item.get('title'),item.get('summary'),item.get('content'),item.get('userid'),item.get('username'))
        print(sql)
        self.cursor.execute(sql)
        self.db.commit()
        return item
