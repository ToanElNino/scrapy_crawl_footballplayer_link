from scrapy import Spider
from scrapy.selector import Selector
from crawler.items import CrawlerItem
import scrapy
import re


class CrawlerSpider(Spider):
    name = "crawler"
    allowed_domains = ["fbref.com"]
    # # start_urls = [
    # #     "https://fbref.com/en/players/aa/",
    # # ]

    def start_requests(self):
        urls = [
            'https://fbref.com/en/players/aa/'
            # 'https://fbref.com/en/players/dea698d9/Cristiano-Ronaldo',
            # 'https://fbref.com/en/players/1f44ac21/Erling-Haaland',
            # 'https://fbref.com/en/players/d70ce98e/Lionel-Messi',
            # 'https://fbref.com/en/players/99127249/Antony',
            # 'https://fbref.com/en/players/e46012d4/Kevin-De-Bruyne',
            # 'https://fbref.com/en/players/9c60f681/Ahmad-Aadi',
            # 'https://fbref.com/en/players/ad713dff/Jamal-Aabbou',
            # 'https://fbref.com/en/players/c2e5d028/Zakariya-Aabbou',
            # 'https://fbref.com/en/players/c48b5529/Kim-Aabech',
            # 'https://fbref.com/en/players/d7ed844d/Kamilla-Aabel',
            # 'https://fbref.com/en/players/bb124176/Mohamed-Abd-El-Aal-Ali',
            # 'https://fbref.com/en/players/53ae3842/Nabil-Aankour',
            # 'https://fbref.com/en/players/e4b8c9c4/Edward-Aaron',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        questions = Selector(response).xpath('//div[@class="section_content"]//p')
        for x in range(len(questions)-1):
            item = CrawlerItem()
            # player info
            # item['Link'] = question.xpath('//div[@class="section_content"]//p//a//@href').extract_first()
            path = '//div[@class="section_content"]//p[' + str(x+1) + ']//a//@href'
            item['Link']= Selector(response).xpath(path).extract_first()
            yield item
