# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
class SprojectPipeline(object):
    def __init__(self):
        self.file = open('.\\sproject\\data\\'+ 'wochu.json','w',encoding='utf-8') # 初始化打开文件

    def process_item(self, item, spider):
        dict_data = dict(item)  # 将item转换成字典
        str_data = json.dumps(dict_data,ensure_ascii=False) + ',\n'
        self.file.write(str_data)
        return item

    def close_spider(self,spider):
        self.file.close() # 完成后关闭文件
