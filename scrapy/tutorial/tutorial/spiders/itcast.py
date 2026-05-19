import scrapy
from tutorial.items import TutorialItem

class ItcastSpider(scrapy.Spider):
    name = "itcast"
    allowed_domains = ["itcast.cn"]
    start_urls = ["https://www.itheima.com/teacher.html#ajavaee"]

#parse是解析的意思，这里定义响应网址的相关操作
    def parse(self, response):
        #获取所需要的节点然后遍历，使用xpath方法提取。
        node_list = response.xpath('//div[@class="top"]')
        for node in node_list:
            item = TutorialItem()

            #xpath方法返回的是选择器对象列表,[0].extract()是从这个选择器中提取数据的方法,
            #extract_first()更好，如果前面提取的是空列表，也不会报错会返回none。若是你肯定返回的是一个元素的列表，那么用这个更好。
            item['name'] = node.xpath( './h3/text()').extract_first()
            item['title'] = node.xpath( './h3/span/text()')[0].extract()
            item['desc'] = node.xpath( './p/text()')[0].extract()
            item['cv'] = node.xpath('//div[@class="center"]/p/text()')[0].extract()

            #不return是为了后续这个函数还能继续运行，比如要翻页的话。返回的数据按照框架是给了引擎。
            yield item