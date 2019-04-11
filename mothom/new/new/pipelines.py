# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import sqlite3
from new.items import *

class NewPipeline(object):
    def __init__(self, Sqlite_db,Sqlite_table):
        self.dbName = Sqlite_db
        print(Sqlite_table*10)

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
                Sqlite_db=crawler.settings.get('SQLITE_DATABASE'),
                Sqlite_table=crawler.settings.get('SQLITE_TABLE')
        )

    def open_spider(self, spider):
        self.conn = sqlite3.connect(self.dbName+'.db')
        print("数据库打开成功"*10)
        print(self.dbName)
        self.c = self.conn.cursor()
        self.c.execute('''CREATE TABLE IF NOT EXISTS COMPANY
            (ID INT PRIMARY KEY     NOT NULL,
            NAME           TEXT    NOT NULL,
            AGE            INT     NOT NULL,
            ADDRESS        CHAR(50),
            SALARY         REAL);''')
        self.conn.commit()

    def close_spider(self, spider):
        self.conn.close()

    def process_item(self, item, spider):
        if isinstance(item, WeiboItem):
            print("管道数据"*10)
            pass
        # self.logger.debug("管道数据")
        # self.logger.debug(item)
        return item

class SqlitePipeline(object):
    def __init__(self, Sqlite_db):
        self.dbName = Sqlite_db;

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
                Sqlite_db=crawler.settings.get('SQLITE_DATABASE')
        )

    def open_spider(self, spider):
        self.conn = sqlite3.connect(self.dbName)
        yield "数据库打开成功"
        self.c = self.conn.cursor()


    def close_spider(self, spider):
        self.conn.close()

    def process_item(self, item, spider):
        if isinstance(item, UserItem) or isinstance(item, WeiboItem):
            self.db[item.collection].update({'id': item.get('id')}, {'$set': item}, True)
        if isinstance(item, UserRelationItem):
            self.db[item.collection].update(
                {'id': item.get('id')},
                {'$addToSet':
                    {
                        'follows': {'$each': item['follows']},
                        'fans': {'$each': item['fans']}
                    }
                }, True)
        return item