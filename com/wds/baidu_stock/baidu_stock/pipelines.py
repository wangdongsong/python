# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class BaiduStockPipeline(object):
    def process_item(self, item, spider):
        return item

class BaiduStocksInfoPipeline(object):

    def open_spider(self, spider):
        self.f = open("BaiduStockInfo.txt", "a", encoding="utf-8")

    def close_spider(self, spider):
        self.f.close()

    def process_item(self, item, spider):
        try:
            line = str(dict(item)) + "\n"
            #print(line)
            self.f.write(line)
        except:
            #print("Error---------------------")
            pass
        return item