import scrapy
from ..items import LianJiaItem
import time

class LianjiaSpider(scrapy.Spider):
    name = 'LianJia'
    Q = None
    #allowed_domains = ['lianjia.com']
    start_urls = ['https://fz.lianjia.com/zufang']
    base_urls = 'https://fz.lianjia.com'
    nextPage = 1

    '''
    def start_requests(self):
        
        self.Q.put('开始爬取')
        
        while True:
            if self.nextPage < 10:
                _url = self.base_urls + "/zufang/pg/" + str(self.nextPage)
                self.nextPage += 1
                yield scrapy.Request(_url)
            else:
                self.Q.put("爬取完成")
                print("爬取完成")
                return 1
        '''

    def parse(self, response):
        #所有房源
        details = response.xpath("//div[@class='content__list']/div[@class='content__list--item']/div[@class='content__list--item--main']")

        # time.sleep(3)
        for detail in details:
            _data = detail.xpath('./p[1]/a/text()').extract()[0].strip()
            #print(_data)
            if _data[:2] == "独栋":
                self.Q.put(_data)
                continue
            if _data[:2] == "合租" or "整租":
                self.Q.put(_data)

                item = LianJiaItem()
                # item['name'] = detail.xpath("./p[1]/a/text()").extract()[0]
                item['name'] = _data[3:]
                item['area'] = detail.xpath("./p[2]/text()[5]").extract()[0].strip()
                item['price'] = detail.xpath("./span[@class='content__list--item-price']/em/text()").extract()[0] + '元/月'
                item['type'] = detail.xpath("./p[2]/text()[7]").extract()[0].strip()
                item['place_x'] = detail.xpath("./p[2]/a[1]/text()").extract()
                item['place_y'] = detail.xpath("./p[2]/a[2]/text()").extract()
                item['place_z'] = detail.xpath("./p[2]/a[3]/text()").extract()

                # print(item)
                yield item

        #下一页
        if self.nextPage < 50:
            time.sleep(2)
            _url = self.base_urls + "/zufang/pg" + str(self.nextPage)
            self.nextPage += 1
            yield scrapy.Request(_url, callback=self.parse)
        else:
            self.Q.put('Finish')
    #下一级
    # def parse_detail(self):
    #     pass

    # def close(spider, reason):
    #     pass