# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import time
import csv

class PacPipeline(object):
    def open_spider(self, spider):
        Path = spider.settings.get('FILE_PATH')
        curTime = time.strftime("%Y_%m_%d",time.localtime(time.time()))
        self.fileNameOfData = Path + "/DATA_{}.csv".format(curTime)
        self.csvFile = open(self.fileNameOfData, 'w', encoding='GBK', newline='')
        self.csvFileWriter = csv.writer(self.csvFile, dialect="excel")
        self.csvFileWriter.writerow(['Name', 'Type', 'Price', 'Area',
                                     'Place_X', 'Place_Y', 'Place_Z'])
    def process_item(self, item, spider):
        # print(type(item['place_x']))
        self.csvFileWriter.writerow([item['name'], item['type'], item['price'], item['area'],
                                     item['place_x'][0], item['place_y'][0], item['place_z'][0]])
        return item

    def close_spider(self, spider):
        self.csvFile.close()
