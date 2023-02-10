from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

class AritcleSpider(CrawlSpider):
    name = 'articles'
    allowed_domains = ['wikipedia.org']
    start_urls = [
        'https://en.wikipedia.org/wiki/'
        'Benevolent_dictator_for_life'
    ]
    rules = [Rule(LinkExtractor(allow=r'.*'), callback='parse_items', follow=True)]
    
    def parse_items(self, response):
        url = response.url
        title = response.css('h1::text').extract_first()
        text = response.xpath('//div[@id="mw-content-text"]//text()').extract()
        last_updated = response.css('li#footer-info-lastmod::text').extract_first()
        last_updated = last_updated.replace('This page was last edited on ', '')
        print(f'URL is: {url}')
        print(f'title is: {title}')
        print(f'text is: {text}')
        print(f'Last updated: {last_updated}')