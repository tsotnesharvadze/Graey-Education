import requests
import scrapy
from scrapy import Request
from scrapy.http import Response


class CarsSpider(scrapy.Spider):
    """
    scrapy runspider fisrt_spider.py -o test.json
    """
    name = 'myManqanebi'
    start_urls = ['https://www.myauto.ge/ka/search/?vips=1']
    custom_settings = {
        'FEED_EXPORT_ENCODING': 'utf-8'
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',

    }

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
        r = requests.post("https://www.myauto.ge/ka/pr/SaveFeedback", data={
            "PrID": response.xpath("//div[@class='detail-top-item'][3]/text()").get().strip(),
            "type_id": "0"
        }, headers=self.headers)
        # print(r.text)
        yield {
            "title": response.xpath("//h1[@class='detail-h1']/text()").get().strip(),
            "phone": response.xpath("//a[@id='client_phone']/text()").get().strip(),
            "real_phone": r.json().get("phone"),
        }