import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class BestMoviesSpider(CrawlSpider):
    name = 'best_movies'
    allowed_domains = ['imdb.com']

    user_agent= 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'

    def start_requests(self):
        yield scrapy.Request(url='https://www.imdb.com/search/title/?genres=drama&groups=top_250&sort=user_rating,desc', headers={
            'user_agent': self.user_agent
        })


    rules = (
        Rule(LinkExtractor(restrict_xpaths="//h3[@class='lister-item-header']/a"), callback='parse_item', follow=True, process_request='set_user_agent'),
        Rule(LinkExtractor(restrict_xpaths="//a[@class='lister-page-next next-page']"), process_request='set_user_agent')
    )

    def set_user_agent(self, request, spider):
        request.headers['User-Agent'] = self.user_agent
        return request


    def parse_item(self, response):
        yield {
            'title': response.xpath("//h3[@class='lister-item-header']/a/text()").get(),
            'year': response.xpath("//span[@class='sc-8c396aa2-2 itZqyK']/text()").get(),
            'duration': response.xpath("//li[@role='presentation']/text()").get(),
            'genre': response.xpath("//span[@class='ipc-chip__text']/text()").get(),
            'rating': response.xpath("//span[@class='sc-7ab21ed2-1 jGRxWM']/text()").get(),
            'movie_url': response.url
        }
