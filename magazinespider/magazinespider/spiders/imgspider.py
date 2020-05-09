from musinsaspider.items import MusinsaspiderItem
import scrapy
import time

class ImgSpider(scrapy.Spider):
    name="musinsa-img-spider"
    start_urls = ["https://www.musinsa.com/index.php?m=magazine&cat=COORDINATION","https://www.musinsa.com/index.php?m=magazine&cat=COORDINATION&p=2","https://www.musinsa.com/index.php?m=magazine&cat=COORDINATION&p=3","https://www.musinsa.com/index.php?m=magazine&cat=COORDINATION&p=4","https://www.musinsa.com/index.php?m=magazine&cat=COORDINATION&p=5","https://www.musinsa.com/index.php?m=magazine&cat=COORDINATION&p=6","https://www.musinsa.com/index.php?m=magazine&cat=COORDINATION&p=7","https://www.musinsa.com/index.php?m=magazine&cat=COORDINATION&p=8","https://www.musinsa.com/index.php?m=magazine&cat=COORDINATION&p=9","https://www.musinsa.com/index.php?m=magazine&cat=COORDINATION&p=10","https://www.musinsa.com/index.php?m=magazine&cat=COORDINATION&p=11","https://www.musinsa.com/index.php?m=magazine&cat=COORDINATION&p=12","https://www.musinsa.com/index.php?m=magazine&cat=COORDINATION&p=12","https://www.musinsa.com/index.php?m=magazine&cat=COORDINATION&p=13","https://www.musinsa.com/index.php?m=magazine&cat=COORDINATION&p=14","https://www.musinsa.com/index.php?m=magazine&cat=COORDINATION&p=15"]

    def parse(self,response):
        for li in response.css("ul.magazine-article-list.article-list.list li.listItem div.articleImg a"):
            yield scrapy.Request(response.urljoin(li.xpath("@href").extract_first()), self.parse_page)
            
    
    def parse_page(self,response):
        for img_url in response.css("li.listItem div img").xpath("@src").extract():
            yield MusinsaspiderItem(image_urls=["http:"+img_url])

