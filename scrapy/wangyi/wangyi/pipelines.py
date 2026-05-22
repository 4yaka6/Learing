# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import json
from datetime import datetime

class WangyiPipeline:
    def open_spider(self, spider):
        """爬虫启动时打开文件"""
        # 使用时间戳命名文件，避免重复
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        self.file = open(f'jobs_{timestamp}.json', 'w', encoding='utf-8')
        # 写入 JSON 数组的开头
        self.file.write('[\n')
        self.first_item = True

    def process_item(self, item, spider):
        """处理每个 item，写入文件"""
        # 如果不是第一个 item，前面加逗号
        if not self.first_item:
            self.file.write(',\n')
        self.first_item = False

        # 将 item 转换为字典并写入 JSON 格式
        line = json.dumps(dict(item), ensure_ascii=False, indent=2)
        self.file.write(line)

        return item

    def close_spider(self, spider):
        """爬虫关闭时关闭文件"""
        self.file.write('\n]')
        self.file.close()