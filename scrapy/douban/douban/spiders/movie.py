import scrapy
from douban.items import DoubanItem


class MovieSpider(scrapy.Spider):
    name = "movie"
    allowed_domains = ["douban.com"]
    start_urls = ["https://movie.douban.com/top250"]

    def parse(self, response):
        node_list = response.xpath('//*[@class="item"]')  # 改为从item开始
        for node in node_list:
            item = DoubanItem()
            # 修正：name - 修正路径和标签
            item['name'] = node.xpath('.//div[@class="hd"]/a/span[@class="title"]/text()').extract_first()
            # 修正：info - 修正路径，导演和主演信息
            item['info'] = node.xpath('.//div[@class="bd"]/p[1]/text()').extract_first()
            if item['info']:
                item['info'] = item['info'].strip().replace('\n', '').replace(' ', '')
            # 修正：score - 修正路径，评分在rating_num中
            item['score'] = node.xpath('.//div[@class="bd"]/div/span[@class="rating_num"]/text()').extract_first()
            # 修正：desc - 修正路径，使用.//表示相对路径
            item['desc'] = node.xpath('.//p[@class="quote"]/span/text()').extract_first()

            yield item

        # 修正：下一页URL - 更通用的写法
        next_page = response.xpath('//span[@class="next"]/a/@href').extract_first()
        if next_page:
            url = response.urljoin(next_page)
            yield scrapy.Request(url=url)