# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


#  class SoimgproItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #  pass

class ImgItem(scrapy.Item):
    # 图片url
    url = scrapy.Field()
    # 图片目录
    mulu=scrapy.Field()
    #名字
    name=scrapy.Field()