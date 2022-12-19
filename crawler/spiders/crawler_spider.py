from time import sleep
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
        data = ["ab","ac","ad","ae","af","ag","ah","ai","aj","ak","al","am","an","ao","ap","aq","ar","as","at","au","av","aw","ax","ay","az"]
        
        for i in data:
            url = "https://fbref.com/en/players/{}/".format(i)
            yield scrapy.Request(url=url, callback=self.parse)
            sleep(10)

    def parse(self, response):
        questions = Selector(response).xpath('//div[@class="section_content"]//p')
        for x in range(len(questions)-1):
            item = CrawlerItem()
            # player info
            # item['Link'] = question.xpath('//div[@class="section_content"]//p//a//@href').extract_first()
            path = '//div[@class="section_content"]//p[' + str(x+1) + ']//a//@href'
            item['Link']= Selector(response).xpath(path).extract_first()
            yield item
