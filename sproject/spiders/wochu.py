# -*- coding: utf-8 -*-
import scrapy
from ..items import *
import datetime
class WochuSpider(scrapy.Spider):

    def __init__(self):
        self.base_url = 'http://www.wochu.cn/Product/CategoryGoods/?pageIndex='
        self.page_num = 1
        self.page_max = 21

    name = 'wochu'
    allowed_domains = ['wochu.cn']
    start_urls = ['http://www.wochu.cn/Product/CategoryGoods/?pageIndex=1']


    def parse(self, response):
        node_list = response.xpath('//div[@class="cgoods-item"]/ul/li')
        for node in node_list:
            item = WoChuItem() #创建数据存储实例
            item['prod_name'] = node.xpath('./div[@class="goods-name"]/text()').extract()[0]
            item['prod_link'] = 'http://www.wochu.cn' + node.xpath('./a/@href').extract()[0]
            item['prod_price'] = node.xpath('./div[@class="price-cart"]/div[@class="price"]/text()')
            item['prod_price'] = node.xpath('.//div[@class="price"]/text()').extract()[0]
            item['prod_pic_link'] = node.xpath('./a/img/@src').extract_first()
            item['update_time'] = str(datetime.datetime.now())

            yield item

        if self.page_num <= self.page_max:
            self.page_num +=1
            next_url = self.base_url + str(self.page_num)
            yield scrapy.Request(next_url,callback=self.parse)
