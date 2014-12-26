from scrapy.spider import Spider
from scrapy.item import Item, Field
from scrapy.selector import Selector

class FeatureItem(Item):
    title = Field()
    link = Field()
    reviews = Field()
    rating = Field()

class FeatureSpider(Spider):
    name = "review"
    allowed_domains = ["www.amazon.com","www.amazon.com"]
    start_urls = [
			 "http://www.amazon.in/product-reviews/B00D8XYAIO?pageNumber=1",
			 "http://www.amazon.in/product-reviews/B00D8XYAIO?pageNumber=2",
			 "http://www.amazon.in/product-reviews/B00D8XYAIO?pageNumber=3",
			 "http://www.amazon.in/product-reviews/B00D8XYAIO?pageNumber=4",
			 "http://www.amazon.in/product-reviews/B00D8XYAIO?pageNumber=5",
	]

    def parse(self, response):
        sel = Selector(response)
        item = FeatureItem()
        item['title'] = sel.xpath("//title/text()").extract()
        item['link'] = response.url
        item['reviews'] = sel.xpath('//span[(((count(preceding-sibling::*) + 1) = 2) and parent::*)]//b | //*[contains(concat( " ", @class, " " ), concat( " ", "reviewText", " " ))]').extract()
        item['rating'] = sel.xpath('//span[@class="asinReviewsSummary"]/a/span').extract()
        #item['rating'] = sel.xpath('//*[(@id = "productSummary")]//*[contains(concat( " ", @class, " " ), concat( " ", "s_star_4_0", " " ))]').extract()
        #item['rating'] = sel.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "s_star_4_0", " " ))]').extract()
        #//*[contains(concat( " ", @class, " " ), concat( " ", "s_star_3_0", " " ))]
        return item

