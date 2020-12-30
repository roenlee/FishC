import scrapy

from tutorial.items import DmozItem

class DmozSpider(scrapy.Spider):
    name = "dmoz"
    allowed_domains = ['www.dmoztools.net']
    start_urls = ['http://www.dmoztools.net/Computers/Programming/Languages/Python/Books/']

    '''
    # setp1

    def parse(self, response):
        filename = response.url.split("/")[-2]
        with open(filename, 'wb') as f:
            f.write(response.body)
    '''
    
    # step2
    
    def parse(self, response):
        res = scrapy.selector.Selector(response)
        sites = res.xpath('//*[@id="site-list-content"]/div[@class="site-item "]/div[@class="title-and-desc"]')
        items = []
        for site in sites:
            item = DmozItem()
            item['title'] = site.xpath('a/div/text()').extract()
            item['link'] = site.xpath('a/@href').extract()
            item['desc'] = site.xpath('div/text()').extract()
            items.append(item)

        return items


'''
        ======以下可用=======
        for site in sites:
            title = site.xpath('a/div/text()').extract()
            link = site.xpath('a/@href').extract()
            desc = site.xpath('div/text()').extract()
            print(title, link, desc)
        ======昏割线，以下不可用=======    
        
        'http://www.dmoztools.net/Computers/Programming/Languages/Python/Resources/'
         //*[@id="site-list-content"]/div[@class="site-item "]/div[@class="title-and-desc"]')

'''
