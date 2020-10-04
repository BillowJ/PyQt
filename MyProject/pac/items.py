# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class LianJiaItem(scrapy.Item):
    name = scrapy.Field()
    price = scrapy.Field()
    area = scrapy.Field()
    place_x = scrapy.Field()
    place_y = scrapy.Field()
    place_z = scrapy.Field()
    type = scrapy.Field()
    # longitude = scrapy.Field()
    # latitude = scrapy.Field()

class DoubanItem(scrapy.Item):
  ranking = scrapy.Field()  # 排名
  name = scrapy.Field()  # 电影名
  introduce = scrapy.Field() # 简介
  star = scrapy.Field()  # 星级
  comments = scrapy.Field()  # 评论数
  describe = scrapy.Field()  # 描述

class PacItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
