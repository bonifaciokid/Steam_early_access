import urllib.request
import json
import bs4 as bs
import scrapy
import re
from ea_crawler.items import crawledSteamInfo


def striphtml(text):
    p = re.compile(r'<.*?>')
    return p.sub('',text)


class scrape_me(scrapy.Spider):
    name = "steam_id"


    def start_requests(self):
        urls = [
        "http://store.steampowered.com/search/tabpaginated/render/?query=&start=0&count=10&genre=70&tab=NewReleases&cc=US&l=english"
        ]

        first = "http://store.steampowered.com/search/tabpaginated/render/?query=&start="
        last = "&count=10&genre=70&tab=NewReleases&cc=US&l=english"
        x = 0
        while x < 1420:
            x += 10
            s = str(x)
            add_s = first + s + last
            urls.append(add_s)
        for url in urls:
            yield scrapy.Request(url=url, callback = self.parse)

    def parse(self, response):
        crawled_json = json.loads(response.body_as_unicode())
        data_body = crawled_json['results_html']
        soup = bs.BeautifulSoup(data_body, 'lxml')
        api_steam = "http://store.steampowered.com/api/appdetails/?appids="
        for i in soup.find_all('a'):
            scraped_id = i.get('data-ds-appid')
            api_url = api_steam + str(scraped_id)
            yield scrapy.Request(api_url + "&cc=us", meta= {'app_id': scraped_id}, callback = self.steam_api)

    def steam_api(self, response):
        item = crawledSteamInfo()
        game_id = response.meta['app_id']
        crawled_api = json.loads(response.body_as_unicode())
        steam_info = crawled_api[game_id]

        item['game_name'] = steam_info['data']['name']
        item['game_id'] = steam_info['data']['steam_appid']
        item['developers'] = steam_info['data']['developers']
        item['publishers'] = steam_info['data']['publishers']
        item['website'] = steam_info['data']['website']
        item['release_date'] = steam_info['data']['release_date']['date']
        item['requirements'] = steam_info['data']['pc_requirements']['minimum'][29:1000]
        item['short_description'] = steam_info['data']['short_description']
        item['genres'] = steam_info['data']['genres']
        item['price'] = steam_info['data']['price_overview']['final']/100

        yield item
