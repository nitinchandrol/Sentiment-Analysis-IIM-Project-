from scrapy.spider import Spider
from scrapy.item import Item, Field
from scrapy.selector import Selector

class FeatureItem(Item):
    feature = Field()
    #feature_list = Field()
    
class FeatureSpider(Spider):
    name = "feature"
    allowed_domains = ["www.flipcard.com"]
    start_urls = ["http://www.flipkart.com/samsung-galaxy-s-duos-2-s7582/p/itmdwzrbfzursyuy"]
    
    def parse(self, response):
        sel = Selector(response)
        item = FeatureItem()
        item['feature'] = sel.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "specs-key", " " ))]').extract()
        #item['feature'] = sel.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "group-head", " " ))]').extract()
        #item['feature_list'] = sel.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "specs-key", " " ))]').extract()
        return item
