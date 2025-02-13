import scrapy

class ExtractUrls(scrapy.Spider):
    name = "Sujeetrahate"

    def start_requests(self):
        urls = ["https://economictimes.indiatimes.com"]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        # Extract all links from the page
        links = response.css("a::attr(href)").getall()

        # Yield each link as an item
        for link in links:
            yield {"link": link}
        