import scrapy
from ..items import UfcMlItem


class UfcSpider(scrapy.Spider):
    name = "ufc"
    allowed_domains = ['ufcstats.com']

    start_urls = ['http://ufcstats.com/statistics/events/completed?page=all']

    def parse(self, response):
        # Here is the setting that dictates how many events will be scraped (I scraped a hundred)
        for event in response.css("tr.b-statistics__table-row i.b-statistics__table-content a::attr('href')")[0:100]:

            url = response.urljoin(event.extract())
            
            yield scrapy.Request(url, callback=self.parse_fight)
    
    def parse_fight(self, response):

        for fight in response.xpath('.//*[@class="b-fight-details__table-col l-page_align_left"]'):
            fighters = fight.xpath('.//*[@class="b-link b-link_style_black"]/text()').getall()
            if fighters:
                item = UfcMlItem()
                item['event'] = response.css("h2.b-content__title span.b-content__title-highlight::text").get().strip()
                item['winner'] = fighters[0].strip()
                item['loser'] = fighters[1].strip() 
                yield item
                
                fighter_page = fight.css("a::attr('href')")
                for fighter in fighter_page:
                    if fighter:
                        link = response.urljoin(fighter.extract())
                        yield scrapy.Request(link, callback=self.parse_fighter)
    
    def parse_fighter(self, response):

       for i in response.xpath('.//*[@class="b-list__info-box b-list__info-box_style_small-width js-guide"]'):
            data = i.xpath('.//*[@class="b-list__box-list-item b-list__box-list-item_type_block"]/text()').getall()
            if data:
                yield {
                    'name': response.css("h2.b-content__title span.b-content__title-highlight::text").get().strip(),
                    'height': data[1].strip(),
                    'weight': data[3].strip(),
                    'reach': data[5].strip(),
                    'birth_date': data[7].strip()
                }
