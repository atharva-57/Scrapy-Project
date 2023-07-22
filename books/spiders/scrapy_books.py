import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class ScrapyBooksSpider(CrawlSpider):
    name = 'scrapy_books'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['https://books.toscrape.com']

    rules = (
        Rule(LinkExtractor(restrict_xpaths="//article[@class='product_pod']/div/a"), callback='parse_item', follow=True),
        Rule(LinkExtractor(restrict_xpaths="//li[@class='next']/a"))
    )

    def parse_item(self, response):
       yield{
        'title': response.xpath("//h3/a/text()").get(),
        'price': response.xpath("//div[@class='product_price']/p/text()").get()
       }
