import scrapy

class XKCDSpider(scrapy.Spider):
    name = "xkcd_spider"
    start_urls = ["https://xkcd.com/"]
    count = 0  # Counter to track number of comics scraped

    def parse(self, response):
        if self.count < 10:
            yield {
                "title": response.css("#ctitle::text").get(),
                "img_url": response.css("#comic img::attr(src)").get(),
            }
            self.count += 1
            # Find the 'prev' link on the page
            prev_page = response.css("a[rel='prev']::attr(href)").get()
            if prev_page:
                next_page = response.urljoin(prev_page)
                yield scrapy.Request(next_page, callback=self.parse)
