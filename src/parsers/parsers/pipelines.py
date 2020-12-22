# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


import json

# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class ParsersPipeline:
    def process_item(self, item, spider):
        return item


class JsonPipeline:
    def open_spider(self, spider):
        self.file = open("../../data/10-25.json", "w")

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        line = json.dumps(ItemAdapter(item).asdict(), sort_keys=True, indent=2) + "\n"
        self.file.write(line)
        return item
