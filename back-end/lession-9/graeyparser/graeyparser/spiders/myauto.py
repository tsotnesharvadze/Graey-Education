import requests
import scrapy
from scrapy import Request
from scrapy.http import Response

from graeyparser.loaders import MyautoItemLoader


class MyautoSpider(scrapy.Spider):
    name = 'myauto'
    allowed_domains = ['myauto.ge']
    start_urls = ['https://www.myauto.ge/search/?vips=1']
    # custom_settings = {
    #     'FEED_EXPORT_ENCODING': 'utf-8'
    # }

    def parse(self, response: Response, **kwargs):
        a_tags = response.xpath("//div[@class='search-lists-container']//div[@class='car-name-left']/h4/a")
        for a in a_tags:
            url = a.xpath('./@href').get()
            yield Request(
                url=response.urljoin(url),
                callback=self.parse_detail
            )
        next_page_link = response.xpath("(//li[@class='pagination-li pag-next']/a/@href)[1]").get()
        if next_page_link is not None:
            yield Request(
                url=response.urljoin(next_page_link),
                callback=self.parse
            )

    def parse_detail(self, response: Response):
        # print(r.text)
        item_loader = MyautoItemLoader(response=response)
        item_loader.add_xpath('title', "//h1[@class='detail-h1']/text()")
        item_loader.add_xpath('phone', "//a[@id='client_phone']/text()")
        item_loader.add_xpath('product_id', "//div[@class='detail-top-item'][3]/text()")
        item_loader.add_xpath('price', "//span[@class='car-price ']/text()")
        yield item_loader.load_item()
