# -*- coding: utf-8 -*-
import scrapy,json,re,requests,random,time
from ..items import ScrapyFrameItem
from urllib.parse import urlencode
import spider_tools as t

#生成column Field()与item对应字段
execute_sql = t.Execute_sql(host='192.168.4.201',username='root',password='mysql',db='zhijianju')
execute_sql.get_scrapy_filed('aqsiq_biaozhun_basic')


headers = t.str2dict('''
User-Agent: Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; TencentTraveler 4.0)
''')

class MyspiderSpider(scrapy.Spider,t):
    name = 'myspider'
    allowed_domains = ['']
    def start_requests(self):
        url = ""
        cookies = t.str2dict('''
        
        ''')
        data = t.str2dict('''
        
        ''')

        # yield scrapy.Request(url,headers=headers,cookies=cookies,callback=self.parse)
        # yield scrapy.FormRequest(url,headers=headers,cookies=cookies,formdata=data,callback=self.parse)

    def parse(self, response):
        pass

    def parese_url(self,response):
        pass

    def part1(self,response):
        item = ScrapyFrameItem()
        pass

    def part2(self,response):
        item = ScrapyFrameItem()
        pass

    def part3(self,response):
        item = ScrapyFrameItem()
        pass

    def part4(self,response):
        item = ScrapyFrameItem()
        pass


