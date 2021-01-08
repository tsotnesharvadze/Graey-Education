from scrapy.loader import ItemLoader

from graeyparser.items import MyautoItem
from itemloaders.processors import MapCompose, TakeFirst
from graeyparser.processors import RemoveComma


class MyautoItemLoader(ItemLoader):
    default_item_class = MyautoItem
    default_input_processor = MapCompose(str.strip, str.upper)
    default_output_processor = TakeFirst()

    price_in = RemoveComma()
