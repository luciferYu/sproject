# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SprojectItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class WoChuItem(scrapy.Item):
    prod_name = scrapy.Field()  # 产品名称
    prod_link = scrapy.Field()  # 产品链接
    prod_price = scrapy.Field()  # 产品价格
    prod_pic_link = scrapy.Field()  #产品图片链接
    update_time = scrapy.Field() # 更新时间
