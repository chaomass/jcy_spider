# -*- coding: utf-8 -*-
import scrapy
import pymongo
from scrapy.conf import settings
import re
import datetime
from jcy.items import JcyItem
from jcy.items import JcyBrefItem

class JcyspiderSpider(scrapy.Spider):
    name = "jcyspider"
    allowed_domains = ["ajxxgk.jcy.cn"]
    start_urls = ['http://www.ajxxgk.jcy.cn/html/zjxflws/']

    def __init__(self,page_max=settings['PAGE_MAX_DEFAULT'],update=settings['UPDATE_DEFAULT'],*args, **kwargs):
        self.page_max = int(page_max)
    
    def parse(self, response):
        for pageindex in range(3572):
            url = 'http://www.ajxxgk.jcy.cn/html/zjxflws/'+str(pageindex)+'.html'
            yield scrapy.Request(url, self.parse_list)
    
    def parse_list(self,response):
        try:
            cases = response.xpath('//div[@class="crow"]')
            #print "cases:",cases.extract()
            itembref = JcyBrefItem()
            for case in cases:
                url0 = case.xpath('div[@class="ctitle"]/a/@href').extract()[1]
                gid=re.findall(r'/html/(.*?).html',url0)[0]
                itembref['title'] = case.xpath('div[@class="ctitle"]/a/text()').extract()[1]
                itembref['url'] = url0
                itembref['gid'] = gid
                itembref['jcy'] = case.xpath('div[@class="ctitle"]/a/text()').extract()[0]
                itembref['uid'] = case.xpath('div[@class="ajh"]/a/text()').extract()[0]
                itembref['closedate'] =case.xpath('div[@class="sj"]/span/text()').extract()[0]
                itembref['rksj'] = str(datetime.datetime.now())
                yield itembref
                href= 'http://www.ajxxgk.jcy.cn/'+url0
                #href=ex_href.replace('#gid#',gid)
                yield scrapy.Request(href, self.parse_detail)
        except Exception,e:
            print "exception:",e

    def parse_detail(self,response):
        item = JcyItem()
        item['gid'] = re.findall(r'/html/(.*?).html', response.url)[0]
        item['urls'] = response.url
        item['uid'] = response.xpath('//div[@id="contentArea"]/div/p/text()')[3].extract()
        item['text'] = response.xpath('//div[@id="Article"]')[0].extract()
        item['html'] = response.body.decode('utf-8','ignore')
        return item
