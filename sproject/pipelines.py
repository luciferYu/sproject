# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
class SprojectPipeline(object):
    def __init__(self):
        self.file = open('.\\sproject\\data\\'+ 'wochu.json','w',encoding='utf-8') # 初始化打开文件
        self.csv = open('.\\sproject\\data\\'+ 'wochu.csv','w',encoding='gbk') # 初始化打开文件

    def process_item(self, item, spider):
        dict_data = dict(item)  # 将item转换成字典
        str_data = json.dumps(dict_data,ensure_ascii=False) + ',\n'
        self.file.write(str_data)

        prod_str = str(dict_data['prod_name']) + ','
        prod_str += str(dict_data['prod_link']) + ','
        prod_str += str(dict_data['prod_price']) + ','
        prod_str += str(dict_data['prod_pic_link']) + ','
        prod_str += str(dict_data['update_time']) + ',\n'
        self.csv.write(prod_str)


        return item

    def close_spider(self,spider):
        self.file.close() # 完成后关闭文件
        self.csv.close() # 完成后关闭文件
