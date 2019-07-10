# Import scrapy
import scrapy
# Import the CrawlerProcess: for running the spider
from scrapy.crawler import CrawlerProcess


# Create the Spider class
class MazdaSpider(scrapy.Spider):
    name = "MazdaSpider"
    # start_requests method

    def start_requests(self):
        global query
        yield scrapy.Request(url=f'https://listado.mercadolibre.com.mx/{query}', callback=self.parse_pagination)

    # First parsing method
    def parse_pagination(self, response):
        global prices
        prices = prices + response.css('span.price__fraction::text').extract()

        pagination_elements = response.xpath('')
        page_links = pagination_elements.xpath('./a/@href')
        next_page_link = page_links.extract()
        if next_page_link:
            yield response.follow(url=next_page_link[0], callback=self.parse_pagination)


prices = []
query = input("¿Qué producto te interesa?")
query.replace(' ', '-')
process = CrawlerProcess()
process.crawl(MazdaSpider)
process.start()

print("-" * 100)
# print(prices)
print(f"Cantidad de precios: {len(prices)}")
