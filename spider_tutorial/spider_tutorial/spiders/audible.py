import scrapy


class AudibleSpider(scrapy.Spider):
    name = 'audible'
    allowed_domains = ['www.audible.com']
    start_urls = ['https://www.audible.com/search/']

    def start_requests(self):
        # Editar los headers por defecto (user-agent)
        yield scrapy.Request(url='https://www.audible.com/search/', callback=self.parse,
                       headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'})

    def parse(self, response):
        # Obtener la caja que contiene toda la información que queremos (título, autor, longitud)
        product_container = response.xpath('//li[contains(@class , "productListItem")]')

        # Recorrer en bucle cada uno de los productos enumerados en la caja product_container
        for product in product_container:
            book_title = product.xpath('.//h3[contains(@class , "bc-heading")]/a/text()').get()
            book_author = product.xpath('.//li[contains(@class , "authorLabel")]/span/a/text()').getall()
            book_length = product.xpath('.//li[contains(@class , "runtimeLabel")]/span/text()').get()

            # Devuelve los datos extraídos y también el user agent definido anteriormente
            yield {
                'title':book_title,
                'author':book_author,
                'length':book_length,
                # Retornamos el user-agent solo para comprobar que esta correcto el que agregamos
                'User-Agent':response.request.headers['User-Agent'], 
            }

        # Obtener la barra de paginación (pagination) y luego el enlace dentro del botón de página siguiente (next_page_url)
        pagination = response.xpath('//ul[contains(@class , "pagingElements")]')
        next_page_url = pagination.xpath('.//span[contains(@class , "nextButton")]/a/@href').get()

        # Ir al enlace "next_page_url" usando el user agent definido antes
        if next_page_url:
            yield response.follow(url=next_page_url, callback=self.parse,
                                  headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'})
