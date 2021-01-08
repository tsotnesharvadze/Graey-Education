# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import requests


class GraeyparserPipeline:
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',

    }

    def process_item(self, item, spider):
        r = requests.post("https://www.myauto.ge/ka/pr/SaveFeedback", data={
            "PrID": item['product_id'],
            "type_id": "0"
        }, headers=self.headers)
        item["phone"] = r.json().get("phone")
        return item


class GraeyparserTitlePipeline:

    def process_item(self, item, spider):
        item_title: str = item['title']
        title, engine, location = item_title.split(' | ')
        item["title"] = title.replace("იყიდება ", "", 1)
        item["engine"] = engine
        item["location"] = location
        return item
