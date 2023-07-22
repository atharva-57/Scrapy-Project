import scrapy
from scrapy.selector import Selector
from scrapy_selenium import SeleniumRequest
from selenium.webdriver.common.keys import Keys


class ExampleSpider(scrapy.Spider):
    name = 'example'
   
    def start_requests(self):
        yield SeleniumRequest(
            url='https://duckduckgo.com',
            wait_time=7,
            screenshot=True,
            callback=self.parse
        )
            
    def parse(self, response):
        # img = response.meta['screenshot']

        # with open('screenshot.png', 'wb') as f:
        #     f.write(img)

        driver = response.meta['driver']
        search_input = driver.find_element_by_xpath("//input[@class='js-search-input search__input--adv']")
        search_input.send_keys('Hello World')

        search_input.send_keys(Keys.ENTER)

        html = driver.page_source
        response_obj = Selector(text=html)

        links = response_obj.xpath("//div[@class='mwuQiMOjmFJ5vmN6Vcqw NvMwcsUp56q4W2Z_b8E7 hAeZQDlu0XXeGwL7U722 SgSTKoqQXa0tEszD2zWF LQVY1Jpkk8nyJ6HBWKAk']")
        for link in links:
            yield {
                'URL': link.xpath(".//@href").get()
            }


      







       
