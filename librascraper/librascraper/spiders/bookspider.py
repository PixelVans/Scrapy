import scrapy
from librascraper.items import BookItem  
from urllib.parse import urlencode


API_KEY = 'APIKEYFROM SCRAPEOPS.IO'
 #A METHOd TO MOUNT THE API ENDPOINTS AND AVOID MOUNTING HEADERS AND AGENTS ALL IN ONE
 #The function is to be used where we make requests Scrapy.Request
 # to avoid adding the function and api codes here, pip install scrapeops-scrapy-proxy-sdk
def get_proxy_url(url):
    payload = {'api_key': API_KEY, 'url' : url}
    proxy_url = 'the url obtaned from paid scrapeops api proxy' + urlencode(payload)
    return proxy_url


class BookspiderSpider(scrapy.Spider):
    name = 'bookspider'
    allowed_domains = ['books.toscrape.com'] #add the scrapeops in the allowed domains to allow proxy mounting
    start_urls = ['https://books.toscrape.com/']

    # custom_settings = {
    #     'FEEDS': {
    #         'booksdata.json': {'format': 'json', 'overwrite': True},
    #     }
    # }
    
    #A list of user agents to avoid being blocked
    # user_agents_list = [
    #     "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
    #     "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
    #     "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    #     "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:112.0) Gecko/20100101 Firefox/112.0",
    #     "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:113.0) Gecko/20100101 Firefox/113.0",
    #     "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:115.0) Gecko/20100101 Firefox/115.0"
    #     ]
    
    #This method mounts the start urls to the proxy API defined above.
    # def start_requests(self):
    #     yield scrapy.Request(url=get_proxy_url(self.start_urls[0]), callback=self.parse, )

    def parse(self, response):
        books = response.css('article.product_pod')
        for book in books:
            relative_url = book.css('h3 a ::attr(href)').get()

            if 'catalogue/' in relative_url:
                book_url = 'https://books.toscrape.com/' + relative_url
            else:
                book_url = 'https://books.toscrape.com/catalogue/' + relative_url
    #add the meta={"proxy:urlendpoint"} as the second arguement in the follow response, to include the premium managed proxy endpoint
    #eg   yield response.follow(book_url, callback=self.parse_book_page, meta={"proxy:enterurlendpoint here"} )
    # alternatively, this can be added in the middleware
            yield response.follow(book_url, callback=self.parse_book_page, )
            
    # Mounting   THE API ENDPOINTS AND AVOID MOUNTING HEADERS AND AGENTS ALL IN ONE      
    #        yield scrapy.Request(url=get_proxy_url(book_url), callback=self.parse_book_page, )
            

        next_page = response.css('li.next a ::attr(href)').get()
        if next_page is not None:
            if 'catalogue/' in next_page:
                next_page_url = 'https://books.toscrape.com/' + next_page
            else:
                next_page_url = 'https://books.toscrape.com/catalogue/' + next_page
    #add the meta={"proxy:urlendpoint"} as the second arguement in the follow response, to include the premium managed proxy endpoint
    # eg   yield response.follow(next_page_url, callback=self.parse, meta={"enterproxy:urlendpoint here password username"})          
            yield response.follow(next_page_url, callback=self.parse,)
            
        # Mounting   THE API ENDPOINTS AND AVOID MOUNTING HEADERS AND AGENTS ALL IN ONE      
    #        yield scrapy.Request(url=get_proxy_url(book_url), callback=self.parse, )

    def parse_book_page(self, response):

        table_rows = response.css("table tr")
        book_item = BookItem()

    
        book_item['url'] = response.url,
        book_item['title'] = response.css('.product_main h1::text').get(),
        book_item['upc'] = table_rows[0].css("td ::text").get()
        book_item['product_type' ] = table_rows[1].css("td ::text").get(),
        book_item['price_excl_tax'] = table_rows[2].css("td ::text").get(),
        book_item['price_incl_tax'] = table_rows[3].css("td ::text").get(),
        book_item['tax'] = table_rows[4].css("td ::text").get(),
        book_item['availability'] = table_rows[5].css("td ::text").get(),
        book_item['num_reviews']=  table_rows[6].css("td ::text").get(),
        book_item['stars'] = response.css("p.star-rating").attrib['class'],
        book_item['category'] = response.xpath("//ul[@class='breadcrumb']/li[@class='active']/preceding-sibling::li[1]/a/text()").get(),
        book_item['description'] = response.xpath("//div[@id='product_description']/following-sibling::p/text()").get(),
        book_item['price'] = response.css('p.price_color ::text').get(),
    
        yield book_item