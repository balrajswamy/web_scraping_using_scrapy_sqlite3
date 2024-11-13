import scrapy
from ..items import MyScrapingItem

class MyscrapySpider(scrapy.Spider):
    name = "myscrapy"
    allowed_domains = ["www.amazon.in"]
    start_urls = ["https://www.amazon.in/s?k=Books&i=stripbooks&rh=n%3A976389031%2Cp_n_publication_date%3A2684819031&dc&crid=N91M8R9RKF84&qid=1731482394&rnid=2684818031&sprefix=%2Caps%2C4176&ref=sr_pg_1","https://www.amazon.in/s?k=Books&i=stripbooks&rh=n%3A976389031%2Cp_n_publication_date%3A2684819031&dc&page=3&crid=N91M8R9RKF84&qid=1731482466&rnid=2684818031&sprefix=%2Caps%2C4176&ref=sr_pg_3"]
    # Set a custom User-Agent to mimic a browser

    custom_settings = {
        'USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.5938.132 Safari/537.36'
    }

    def parse(self, response):
        items = MyScrapingItem()
        #book_titles = response.xpath('//span[@class="a-size-medium a-color-base a-text-normal"]/text()').getall()
        #book_titles = response.xpath('//div[@class="a-section a-spacing-small a-spacing-top-small"]//span[@class="a-size-medium a-color-base a-text-normal"]/text()').getall()

        print("\n\n+++++++++++++++++++++++++\n\n")
        #print("total books:\t", len(book_titles))
        print("\n\n+++++++++++++++++++++++++\n\n")
        for book in response.xpath('//div[@class="a-section a-spacing-small a-spacing-top-small"]'):
            book_title = book.xpath(
                './/h2[@class="a-size-mini a-spacing-none a-color-base s-line-clamp-2"]/a/span/text()').get()
            book_price = book.xpath('.//div[@data-cy="price-recipe"]//span[@class="a-offscreen"]/text()').get()

            items["book_title"] = book_title if book_title is not None else ""
            items["book_price"] = book_price if book_price is not None else 0

            yield items
            """
            if book_title is not None and book_price is not None:
                yield {
                    'book_title': book_title,
                    'book_price': book_price
                }
            """