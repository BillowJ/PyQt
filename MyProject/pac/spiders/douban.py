import scrapy
from ..items import DoubanItem

class DoubanSpider(scrapy.Spider):
    name = 'douban'
    allowed_domains = ['movie.douban.com']
    start_urls = ['https://movie.douban.com/top250/']

    def parse(self, response):
        # 首先抓取电影列表
        movie_list = response.xpath("//ol[@class='grid_view']/li")
        # movie_list = response.xpath("//ol[@class='grid_view']/li/div[@class='item']")
        for selector in movie_list:
            # 遍历每个电影列表，从其中精准抓取所需要的信息并保存为item对象
            item = DoubanItem()
            item['ranking'] = selector.xpath(".//em/text()").get()
            item['name'] = selector.xpath(".//span[@class='title']/text()").get()
            text = selector.xpath(".//div[@class='bd']/p[1]/text()").getall()
            intro = ""
            for s in text:  # 将简介放到一个字符串
                intro += "".join(s.split())  # 去掉空格
            item['introduce'] = intro
            item['star'] = selector.css('.rating_num::text').extract_first()
            item['comments'] = selector.xpath(".//div[@class='star']/span[4]/text()").extract_first()
            item['describe'] = selector.xpath(".//span[@class='inq']/text()").extract_first()
            # print(item)
            yield item  # 将结果item对象返回给Item管道
        # 爬取网页中的下一个页面url信息
        next_link = response.xpath("//span[@class='next']/a[1]/@href").extract_first()
        if next_link:
            next_link = "https://movie.douban.com/top250" + next_link
            print(next_link)
            # 将Request请求提交给调度器
            yield scrapy.Request(next_link, callback=self.parse)
