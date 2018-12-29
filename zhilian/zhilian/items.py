# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ZhilianItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    number = scrapy.Field()
    jobname = scrapy.Field()
    company = scrapy.Field()
    position = scrapy.Field()
    size = scrapy.Field()
    edulevel = scrapy.Field()
    salary = scrapy.Field()
    workexp = scrapy.Field()
    workcontent = scrapy.Field()
    
