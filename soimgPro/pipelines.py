# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.pipelines.images import ImagesPipeline
import scrapy
from soimgPro import settings
import os
# 下载图片
class SoimgproPipeline(ImagesPipeline):
    # 对图片url发起请求
    def get_media_requests(self, item, info):
        # print('开始下载')
        # 在这里需要把item传给file_path方法进行处理。不按图片分页存放的话，可以不写meta参数
        return scrapy.Request(item['url'], meta={'item': item})
    def file_path(self, request, response=None, info=None):
        # print("处理文件夹")
        item = request.meta['item']
        wenjianjia = item['mulu']
        img_source = settings.IMAGES_STORE
        # 图片存放的文件夹路径
        img_path = os.path.join(img_source, wenjianjia)
        # 判断文件夹存放的位置是否存在，不存在则新建文件夹
        if not os.path.exists(img_path):
            os.makedirs(img_path)
            # 更改图片名字

        url = request.url
        print(url)
        # print('路径')
        url = str(url.split('/')[-1])[1:5]
        print(item["name"])
        file_name = str(item["name"])+url+".jpg"
        print(file_name)
        # 图片存放路径
        image_path = os.path.join(wenjianjia, file_name)
        # 返回图片的存放路径
        return image_path

    def item_completed(self, results, item, info):
        # item = request.meta['item']
        print('下载完成')
        return item

