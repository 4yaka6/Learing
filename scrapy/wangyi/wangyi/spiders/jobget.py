import scrapy
from twisted.words.protocols.jabber.xmpp_stringprep import nodeprep
from wangyi.items import WangyiItem
import json

class JobgetSpider(scrapy.Spider):
    name = "jobget"
    allowed_domains = ["163.com"]
    api_url = "https://hr.163.com/api/hr163/position/queryPage"

    def __init__(self):
        self.page = 1

    def start_requests(self):
        post_data = {
            "currentPage": self.page,
            "pageSize": 10
        }
        yield scrapy.Request(
            url=self.api_url,
            method='POST',
            body=json.dumps(post_data),
            headers={
                'Content-Type': 'application/json;charset=UTF-8',
                'Referer': 'https://hr.163.com/job-list.html'
            },
            callback=self.parse
        )

    def parse(self, response):
        data = response.json()

        # 检查返回状态
        if data.get('code') != 200:
            self.logger.error(f"API返回错误: {data.get('msg')}")
            return

        job_list = data.get('data', {}).get('list', [])

        for job in job_list:
            item = WangyiItem()
            item['name'] = job.get('name')
            item['type'] = job.get('firstPostTypeName')
            item['num'] = job.get('recruitNum')
            item['edu'] = job.get('reqEducationName')
            item['exp'] = job.get('reqWorkYearsName')
            item['department'] = job.get('firstDepName')
            item['product'] = job.get('productName')
            # 工作地点可能是列表，取第一个
            place_list = job.get('workPlaceNameList', [])
            item['place'] = place_list[0] if place_list else None
            # 工作类型：0全职、1实习等
            item['is_full_time'] = '全职' if job.get('workType') == '0' else '实习'
            # 职位描述（如果需要）
            item['description'] = job.get('description')
            item['requirement'] = job.get('requirement')

            yield item

        # 分页处理
        is_last_page = data.get('data', {}).get('lastPage', True)

        if not is_last_page:  # 如果不是最后一页，继续爬取，判断的方式各个网页不太相同
            self.page += 1
            next_post_data = {
                "currentPage": self.page,
                "pageSize": 10
            }
            yield scrapy.Request(#返回的是request这个类
                url=self.api_url,
                method='POST',
                body=json.dumps(next_post_data),
                headers={
                    'Content-Type': 'application/json;charset=UTF-8',
                    'Referer': 'https://hr.163.com/job-list.html'
                },
                callback=self.parse #解析方式，不写就是默认为parse
            )
