# Import scrapy
import scrapy
# Import the CrawlerProcess: for running the spider
from scrapy.crawler import CrawlerProcess


# Create the Spider class
class MazdaSpider(scrapy.Spider):
    name = "MazdaSpider"

    # start_requests method
    def start_requests(self):
        yield scrapy.Request(url='https://listado.mercadolibre.com.mx/mazda-cx3', callback=self.parse)

    # First parsing method
    def parse(self, response):
        global prices
        prices = response.css('span.price__fraction::text').extract()
        # La expresión equivalente en XPath
        # prices = response.xpath('//span[@class="price__fraction"]/text()').extract()


process = CrawlerProcess()
process.crawl(MazdaSpider)
process.start()

print("-" * 100)
print(prices)
print(f"Cantidad de precios: {len(prices)}")
