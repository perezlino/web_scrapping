import scrapy
from scrapy import FormRequest

class QuotesLoginSpider(scrapy.Spider):
    name = 'quotes_login'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['https://quotes.toscrape.com/login']

    # Procesando el csrf_token, el username y la password
    def parse(self, response):
        csrf_token = response.xpath("//input[@name='csrf_token']/@value").get()
    # enviando FormRequest (FormRequest extiende el Request base con funcionalidad para tratar con formularios HTML)
    # FormRequest.from_response() simula el inicio de sesión de un usuario
        yield FormRequest.from_response(
            response,
            formxpath='//form',
            formdata={
                'csrf_token': csrf_token,
                'username': 'admin',
                'password': 'admin'
            },
            callback=self.after_login
        )
    # aquí definimos la función after_login que usamos en callback
    def after_login(self, response):
        # Si hay un texto "logout" en la página, imprime "Successfully logged in!"
        if response.xpath("//a[@href='/logout']/text()").get():
            print('Successfully logged in!')