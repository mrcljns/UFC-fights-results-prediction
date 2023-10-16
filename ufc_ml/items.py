# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class UfcMlItem(scrapy.Item):
    # define the fields for your item here like:
    event = scrapy.Field()
    winner = scrapy.Field()
    loser = scrapy.Field()
