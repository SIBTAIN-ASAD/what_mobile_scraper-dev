'''
Define here the models for your scraped items
'''
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class WhatMobileScraperItem(scrapy.Item):
    '''
        define the fields for your item here like:
    '''
    name = scrapy.Field()
    price = scrapy.Field()
    image_url = scrapy.Field()
    details_url = scrapy.Field()
    details = scrapy.Field()


    def __repr__(self):
        """only print out attr1 after exiting the Pipeline"""
        return repr({"name": self['name'], "price": self['price'], \
                "image_url": self['image_url'], "details_url": self['details_url']})

    def __str__(self):
        """only print out attr1 after exiting the Pipeline"""
        return str({"name": self['name'], "price": self['price'], \
                "image_url": self['image_url'], "details_url": self['details_url']})
