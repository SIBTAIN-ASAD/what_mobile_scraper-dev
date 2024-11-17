'''
    This spider scrapes mobile phones data from whatmobile.com.pk
'''
import logging
import scrapy
from what_mobile_scraper.items import WhatMobileScraperItem

class WhatspiderSpider(scrapy.Spider):
    '''
        This spider scrapes mobile phones data from whatmobile.com.pk
    '''
    name = "whatspider"
    allowed_domains = ["whatmobile.com.pk"]
    start_urls = ["https://www.whatmobile.com.pk/Samsung_Mobiles_Prices", \
                    'https://www.whatmobile.com.pk/Huawei_Mobiles_Prices']
    logger = logging.getLogger(__name__)

    # def start_requests(self):
    custom_settings = {
        'FEED_FORMAT': 'json',  # Default output format
        'FEED_URI': None,  # Will be set dynamically based on command-line argument
    }

    def parse(self, response, **kwargs):
        '''
            This function parses a response from the start_urls defined above.
            @url https://www.whatmobile.com.pk/Samsung_Mobiles_Prices
            @returns items 1
            @scrapes name price image_url details_url
            @scrapes url project spider server date
        '''
        data = response.css('div.mobiles')

        if data:
            data = data.css('div.item')
            for mobile_div in data:
                item = WhatMobileScraperItem()
                item['name'] = mobile_div.css('h4 a::attr(title)').\
                    get().strip().replace('price', '').strip()
                item['price'] = mobile_div.css('span.PriceFont::text').get().strip()
                item['image_url'] = mobile_div.css('img[itemprop="image"]::attr(src)').get()
                item['details_url'] = response.urljoin(\
                        mobile_div.css('a[itemprop="url"]::attr(href)').get())
                yield scrapy.Request(item['details_url'], \
                                        callback=self.parse_details, meta={'item': item})

    def parse_details(self, response):
        '''
            This function parses a response from the details_url defined above.
            @url https://www.whatmobile.com.pk/Samsung_Galaxy-A11
            @returns items 1
        '''
        item = response.meta['item']

        # Extracting details from the provided HTML structure
        details = {}
        current_section = None

        for row in response.css('tr[class^="RowBG"]'):
            if row.css('td[class*="specs-mainHeading"]'):
                current_section = row.css('td[class*="specs-mainHeading"]::text').get().strip()
                details[current_section] = {}
            elif row.css('th::text'):
                sub_heading = row.css('th::text').get().strip()
                value = row.css('td::text').get('').strip()  # Use get('') to handle None
                if current_section is not None and sub_heading is not None:
                    details[current_section][sub_heading] = value
                else:
                    self.logger.error("\n\n\nSkipping item \
                        due to missing sub-heading: %s", response.url)
                    break
            else:
                self.logger.error("\n\n\nSkipping item due to missing\
                                  section heading %s", response.url)
                break
        # Adding details to the item
        print("Getting details for ", item['name'], " from ", item['details_url'])
        item['details_url'] = response.url
        item['details'] = details
        item['details']['name'] = {'Name': item['name']}
        yield item
        