# Import scrapy
import scrapy
# Import the CrawlerProcess: for running the spider
from scrapy.crawler import CrawlerProcess


# Create the Spider class
class MazdaSpider(scrapy.Spider):
    name = "MazdaSpider"
    # start_requests method

    def start_requests(self):
        yield scrapy.Request(url='https://listado.mercadolibre.com.mx/mazda-cx3', callback=self.parse_pagination)

    # First parsing method
    def parse_pagination(self, response):
        global prices
        prices = prices + response.css('span.price__fraction::text').extract()

        pagination_elements = response.css('li.andes-pagination__button')
        page_links = pagination_elements.xpath('./a/@href')
        links_to_follow = page_links.extract()

        for url in links_to_follow:
            yield response.follow(url=url, callback=self.parse_pages)

    # First parsing method
    def parse_pages(self, response):
        global prices
        prices = prices + response.css('span.price__fraction::text').extract()


prices = []
process = CrawlerProcess()
process.crawl(MazdaSpider)
process.start()

print("-" * 100)
print(prices)
print(f"Cantidad de precios: {len(prices)}")
