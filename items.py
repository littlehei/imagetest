# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Field,Item

class ImagetestItem(Item):
    url = Field()
    name = Field()
    tags = Field()
    image_urls = Field()
    images = Field()
