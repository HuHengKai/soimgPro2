import scrapy
import time
from soimgPro.items import ImgItem
class SoimgSpider(scrapy.Spider):
    name = 'soimg'
    # allowed_domains = ['netbian.com']
    #  start_urls = ['http://https://image.so.com//']
    start_urls = ['http://www.netbian.com/meinv/']
    # http: // www.netbian.com / meinv / index_2.htm

    def parse(self, response):
        # 获取总页数
        page_num = response.xpath('//*[@id="main"]/div[4]/a[8]/text()').extract_first()
        # 获取各个页的网址，可以把5改成page_num
        for i in range(10):
            if i + 1 == 1:
                url = 'http://www.netbian.com/meinv/'
            else:
                url = 'http://www.netbian.com/meinv/index_%s.htm' % (i + 1)
            yield scrapy.Request(url=url, callback=self.parse_page)
        # 获取全部以及页面地址url
    def parse_page(self, response):
        item = ImgItem()
        li_list = response.xpath('//div[@class="list"]/ul/li')
        # 获取当前页面是第几页
        page = response.xpath('//*[@id="main"]/div[4]/b/text()').extract_first()
        item['mulu'] = '第%s页' % (page)
        # print("获取壁纸的原图地址")
        for li in li_list:
            try:
                geren_url = 'http://www.netbian.com' + li.xpath('./a/@href').extract_first()
            except:
                continue
        # 传递item
            yield scrapy.Request(url=geren_url, callback=self.parse_detail, meta={'item': item})

    def parse_detail(self, response):
        time.sleep(3)
        # print("获取图片下载地址")
        name=response.xpath('//div[@class="pic"]//a/img/@title').extract_first()
        print(name)
        item = response.meta['item']
        # 获取图片地址,获得一个下载一个
        img_url = response.xpath('//div[@class="pic"]/p/a/img/@src').extract_first()
        item['url'] = img_url
        item["name"] = name
        # print(item["name"])
        yield item
