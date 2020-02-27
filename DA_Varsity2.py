import scrapy
class newSpider(scrapy.Spider):
    name = "new Spider"
    start_urls = ['http://brickset.com/sets/year-2019']
    def parse(self, response):
              css_sel = 'img'
              for x in response.css(css_sel):
                  xpath_sel = "@src"
                  css_sel2 = "::attr(src)"
                  yield {
                      'IMAGE link': x.xpath(xpath_sel).extract_first(),
                  }
                  nextcss_sel = '.next a::attr(href)'
                  next_page = response.css(nextcss_sel).extract_first()
                  if next_page:
                      yield scrapy.Request((response.urljoinnext_page), callback = self.parse)
