# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class crawledSteamInfo(scrapy.Item):
    game_name = scrapy.Field()
    game_id = scrapy.Field()
    developers = scrapy.Field()
    website = scrapy.Field()
    publishers = scrapy.Field()
    release_date = scrapy.Field()
    requirements = scrapy.Field()
    short_description = scrapy.Field()
    genres = scrapy.Field()
    price = scrapy.Field()
