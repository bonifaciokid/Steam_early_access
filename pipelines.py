# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import sys
import json


class storeSteamInfo(object):


    def process_item(self, item, spider):
        data = item
        genre_list = []
        for genre in data['genres']:
            genre_list.append(genre['description'])
            for n,i in enumerate(genre_list):
                if i == 'Indie':
                    genre_list[n] = 'Independent'

        for itm in data.keys():
            if itm == 'genres':
                data[itm] = genre_list

        with open('early_access.json', 'a') as f:
            json.dump(  {
                              'game_name': item['game_name'],
                              'game_id': item['game_id'],
                              'genres': item['genres'],
                              'price': item['price'],
                              'developers': item['developers'],
                              'publishers': item['publishers'],
                              'website': item['website'],
                              'release_date': item['release_date'],
                              'requirements': item['requirements'],
                              'short_description': item['short_description']
                      }, f, indent = 4, separators = (',', ':'))






















































        #for gens in genres:
            #for g in gens['description']:
            #    if g in game_genres:
                    #final_gen = game_genres[g]
