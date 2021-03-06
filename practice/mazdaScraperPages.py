# Import scrapy
import scrapy
# Import the CrawlerProcess: for running the spider
from scrapy.crawler import CrawlerProcess


# Create the Spider class
class MazdaSpider(scrapy.Spider):
    name = "MazdaSpider"
    # start_requests method

    def start_requests(self):
        urls = []
        for page_url in urls:
            yield scrapy.Request(url=page_url, callback=self.parse)
    # First parsing method

    def parse(self, response):
        global prices
        prices = prices + response.css('span.price__fraction::text').extract()


prices = []
process = CrawlerProcess()
process.crawl(MazdaSpider)
process.start()

print("-" * 100)
print(prices)
print(f"Cantidad de precios: {len(prices)}")
