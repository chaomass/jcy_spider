# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JcyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    gid = scrapy.Field()
    court = scrapy.Field()
    html = scrapy.Field()
    urls = scrapy.Field()
    uid = scrapy.Field()
    text = scrapy.Field()

class JcyBrefItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    
    title = scrapy.Field()
    url = scrapy.Field()
    gid = scrapy.Field()
    jcy = scrapy.Field()
    uid = scrapy.Field()
    closedate = scrapy.Field()
    rksj = scrapy.Field()
