# -*- coding: utf-8 -*-

from scrapy.spiders import CrawlSpider
import re
from scrapy.selector import Selector
from scrapy.http import Request
from scrapy.contrib.loader import ItemLoader, Identity
from imagetest.items import ImagetestItem


class ImageSpider(CrawlSpider):
    name = 'imagetest'

    start_urls = [
        #'http://www.meizitu.com/',
        'http://www.meizitu.com/a/list_1_1.html'
        # 'http://www.meizitu.com/a/5380.html'
    ]

    def parse(self, response):

        selector = Selector(response)

        if (response.url).find('list')>0:
            links = selector.xpath('//h3/a/@href').extract()
        else:
            links = selector.xpath('//h2/a/@href').extract()

        for link in links:
            yield Request(link, callback=self.parse_item)
            # pass

        ##获得分页的链接

        pages = selector.xpath('//div[@id="wp_page_numbers"]/ul/li/a/@href').extract()

        print ('pages %s' % pages)

        if len(pages) > 2:
            page_link = pages[-2]
            page_link = page_link.replace('/a/', '')
            url = 'http://www.meizitu.com/a/' + page_link
            # print url

            yield Request(url, callback=self.parse)

    def parse_item(self, response):

        l = ItemLoader(item=ImagetestItem(), response=response)
        l.add_xpath('name', '//h2/a/text()')
        l.add_xpath('tags', "//div[@id='maincontent']/div[@class='postmeta  clearfix']/div[@class='metaRight']/p")
        l.add_xpath('image_urls', "//div[@id='picture']/p/img/@src", Identity())

        l.add_value('url', response.url)

        return l.load_item()
