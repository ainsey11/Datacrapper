import scrapy

class BrickSetSpider(scrapy.Spider):
    name = "brickset_spider"
    start_urls = ['https://pubgtracker.com/profile/pc/AnalSod0my/solo?region=agg']


