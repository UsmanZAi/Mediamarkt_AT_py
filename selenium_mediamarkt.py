import scrapy

class mediamarktSpider(scrapy.Spider):
    name = "mediamarkt"
    start_urls = ["https://mediamarkt.pl/telefony-i-smartfony/smartfony/iphone?click=menu&page=1&limit=50"
    ]

    def parse(self, response):
        for products in response.css('div.offers.is-list .offer'):
            yield {
                "name": products.css('a .title::text').get(),
                "price": products.css('.pricing .tab.price .price-box .main-price.is-big .whole::text').get().replace('\n','').replace('\s',''),
                "link": products.css('.details .offer-header .info >a').attrib['href'],
            }

        next_page = response.css(".more-offers a::attr(href)").get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)


a
