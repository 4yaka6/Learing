# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

import json
class TutorialPipeline:
    def __init__(self):
        self.file = open('itcast.json','w')

    def process_item(self, item, spider):
        #将item强制转化为字典，因为dump只能将字典序列化
        item = dict(item)
        json_data = json.dumps(item, ensure_ascii=False) + ',\n'
        self.file.write(json_data)

        return item
    def __del__(self):
        self.file.close()
