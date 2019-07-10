# Import scrapy
import scrapy
# Import the CrawlerProcess: for running the spider
from scrapy.crawler import CrawlerProcess


# Create the Spider class
class MazdaSpider(scrapy.Spider):
    name = "MazdaSpider"
    # start_requests method

    def start_requests(self):
        # 1. Inserta el URL que se
        yield scrapy.Request(url='', callback=self.parse)
    # First parsing method

    def parse(self, response):
        global prices
        prices = response.css('').extract()


process = CrawlerProcess()
process.crawl(MazdaSpider)
process.start()

print("-" * 100)
print(prices)
print(f"Cantidad de precios: {len(prices)}")
