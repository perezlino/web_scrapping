import scrapy


class WorldometersSpider(scrapy.Spider):
    name = 'worldometers'
    allowed_domains = ['www.worldometers.info']
    start_urls = ['https://www.worldometers.info/world-population/population-by-country/']

    def parse(self, response):
        # Extracción de los elementos "a" de cada país
        countries = response.xpath('//td/a')

        # Recorrer la lista de países
        for country in countries:
            country_name = country.xpath(".//text()").get()
            link = country.xpath(".//@href").get()

            yield response.follow(url=link, callback=self.parse_country, meta={'country':country_name})

    # Getting data inside the "link" website
    def parse_country(self, response):
        # Obtener los nombres de los países y cada elemento "fila" dentro de la tabla de población
        country = response.request.meta['country']
        # También podemos utilizar todo el valor de la clase --> 
        # response.xpath('(//table[@class="table table-striped table-bordered table-hover table-condensed table-list"])[1]/tbody/tr')
        rows = response.xpath("(//table[contains(@class,'table')])[1]/tbody/tr")  
        # Recorriendo la lista de filas
        for row in rows:
            year = row.xpath(".//td[1]/text()").get()
            population = row.xpath(".//td[2]/strong/text()").get()

            # Devuelve los datos extraídos
            yield {
                'country':country,
                'year': year,
                'population':population,
            }