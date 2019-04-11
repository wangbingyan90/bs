# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field


class UserItem(Item):
    collection = 'users'
    id = Field()
    name = Field()
    avatar = Field()
    cover = Field()
    gender = Field()
    description = Field()
    fans_count = Field()
    follows_count = Field()
    weibos_count = Field()
    verified = Field()
    verified_reason = Field()
    verified_type = Field()
    follows = Field()
    fans = Field()
    crawled_at = Field()

class UserRelationItem(Item):
    collection = 'users'
    id = Field()
    follows = Field()
    fans = Field()


class WeiboItem(Item):
    collection = 'weibos'
    id = Field()
    attitudes_count = Field()
    comments_count = Field()
    reposts_count = Field()
    picture = Field()
    pictures = Field()
    source = Field()
    text = Field()
    raw_text = Field()
    thumbnail = Field()
    user = Field()
    created_at = Field()
    crawled_at = Field()

class NewsItem(Item):
    collection = 'New'
    id = Field()        #id
    title = Field()      #标题
    summary = Field()   #摘要
    published = Field()  #发布时间
    content = Field()    #正文
    news_url = Field()   #url
    crawl_date = Field() #爬从抓取的时间
    referer_web = Field()#引用的网站名
    referer_url = Field()#引用的源url
    author = Field()     #作者
    read_num = Field()   #已阅读量
    comment_num =Field() #已评论量
    pic = Field()        #新闻图片
    news_no = Field()    #所在网站新闻标号
    topic = Field()      #所在网站所属主题
    catalogue = Field()  #所在网站所属目录
    tags = Field()       #标签
    keywords = Field()   #找到对应的关键词
    source = Field()     #来源网站(网易科技)