# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class WangyiItem(scrapy.Item):
    name = scrapy.Field()          # 职位名称
    type = scrapy.Field()          # 职位类别
    num = scrapy.Field()           # 招聘人数
    edu = scrapy.Field()           # 学历要求
    exp = scrapy.Field()           # 经验要求
    department = scrapy.Field()    # 部门
    product = scrapy.Field()       # 所属产品 ← 添加这个
    place = scrapy.Field()         # 工作地点
    is_full_time = scrapy.Field()  # 全职/实习
    description = scrapy.Field()   # 职位描述
    requirement = scrapy.Field()   # 职位要求
