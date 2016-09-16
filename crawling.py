# -*- coding: utf-8 -*-
import scrapy

from datetime import datetime
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class CrowdworksSpider(CrawlSpider):
    name = 'crowdworks'
    allowed_domains = ['crowdworks.jp']
    start_urls = ['https://crowdworks.jp/']

    rules = ( Rule(LinkExtractor(allow=r'/public/jobs/group/development'), callback='parse_item', follow=False), )

    #def parse(self, response):
    #    for href in response.css('.item_title > a::attr(href)'):
    #        full_url = response.urljoin(href.extract)
    #        yield scrapy.Request(full_url, callback=self.parse_item)

    def parse_item(self, response):
        yield {
#	    'item_title': response.css('.item_title').extract(),
            'title': response.css('.item_title > a::text').extract(),
            'ellipsis': response.css('.ellipsis::text').extract(),
            'amount': response.xpath('string(//b[@class="amount"])').extract(),
            'entries': response.xpath('string(//div[@class="entry_data entries"])').extract(),
            'absolute_date': response.css('.absolute_date::text').extract(),
            'post_date': response.xpath('string(//div[@class="post_date meta_column"])').extract(),
            'show_detail': response.css('.show_detail > a::attr(href)').extract(),
        }

