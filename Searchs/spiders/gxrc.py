# -*- coding: utf-8 -*-
import scrapy


class GxrcSpider(scrapy.Spider):
    name = 'gxrc'
    allowed_domains = ['www.gxrc.com']
    start_urls = []
    for i in range(1, 10):
        i = str(i)
        url_list = "http://s.gxrc.com/sJob?schType=3&page= %s" % (i)
        start_urls.append(url_list)

    def parse(self, response):
        print(response.url)
        pass
