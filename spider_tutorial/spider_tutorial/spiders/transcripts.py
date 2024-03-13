import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class TranscriptsSpider(CrawlSpider):
    name = 'transcripts'
    allowed_domains = ['subslikescript.com']
    # start_urls = ['https://subslikescript.com/movies_letter-X']

    # Establecer una variable user agent
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'

    # Editar el user agent en la request enviada
    def start_requests(self):
        yield scrapy.Request(url='https://subslikescript.com/movies_letter-X', headers={
            'user-agent':self.user_agent
        })

    # Establecer reglas para el crawler 
    rules = (
        Rule(LinkExtractor(restrict_xpaths=("//ul[@class='scripts-list']/a")), callback='parse_item', follow=True, process_request='set_user_agent'),
        Rule(LinkExtractor(restrict_xpaths=("(//a[@rel='next'])[1]")), process_request='set_user_agent'),
    )

    # Configuración del user agent
    def set_user_agent(self, request, spider):
        request.headers['User-Agent'] = self.user_agent
        return request

    def parse_item(self, response):
        # Obtener la caja del article que contiene los datos que queremos (title, plot, etc)
        article = response.xpath("//article[@class='main-article']")
        # .getall() devolverá una lista, usa .join() para convertir la lista en un string (ESTO SE AGREGÓ !!)
        transcript_list = article.xpath("./div[@class='full-script']/text()").getall()
        transcript_string = ' '.join(transcript_list)

        # Extraer los datos que queremos y luego devolverlos
        yield {
            'title':article.xpath("./h1/text()").get(),
            'plot':article.xpath("./p/text()").get(),
            'transcript':transcript_string,
            'url':response.url,
            # 'user-agent':response.request.headers['User-Agent'],
        }