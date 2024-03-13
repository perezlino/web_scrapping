import scrapy
import json

class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['https://quotes.toscrape.com/api/quotes?page=1']

    def parse(self, response):
        # Almacenar la respuesta en json y obtener quotes
        json_response = json.loads(response.body)
        quotes = json_response.get('quotes')

        # Recorrer los elementos de quotes
        for quote in quotes:
            # Devuelve los datos extraídos
            yield {
                'author': quote.get('author').get('name'),
                'tags': quote.get('tags'),
                'quotes': quote.get('text'),
            }

        # Escoger el elemento "has_next"
        has_next = json_response.get('has_next')

        # Si has_next==True (hay página siguiente), ejecuta el siguiente código
        if has_next:
            next_page_number = json_response.get('page')+1
            yield scrapy.Request(
                url=f'https://quotes.toscrape.com/api/quotes?page={next_page_number}',
                callback=self.parse
            )