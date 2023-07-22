import scrapy


class EbaySpider(scrapy.Spider):
    name = 'ebay'
    allowed_domains = ['www.ebay.com']
    start_urls = ['https://www.ebay.com']

    def parse(self, response):
        for product in response.xpath('.//ul[@class="b-list__items_nofooter srp-results srp-grid"]'):
            yield{
                'title': product.xpath('.//div[@class="vim x-item-title"]/h1/span/text()[2]').get(),
                'price': product.xpath('.//span[@class="notranslate"]/text()').get()

            }
        next_page = response.xpath('.//a[@_sp="p2489527.m4335.l8631"]/@href')

        if next_page:
           yield scrapy.Request(url=next_page, callback=self.parse)
