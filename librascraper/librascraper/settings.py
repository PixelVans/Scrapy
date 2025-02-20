# Scrapy settings for librascraper project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = "librascraper"

SPIDER_MODULES = ["librascraper.spiders"]
NEWSPIDER_MODULE = "librascraper.spiders"

#obtaining free Agents headers from scrapeops.io
SCRAPEOPS_API_KEY = 'bb10ccbd-8ea0-4f28-b7be-bae72dc31ce1' # from https://scrapeops.io
SCRAPEOPS_FAKE_USER_AGENT_ENDPOINT = 'https://headers.scrapeops.io/v1/user-agents'
SCRAPEOPS_FAKE_USER_AGENT_ENABLED = True
SCRAPEOPS_NUM_RESULTS = 5


#Free proxies obtained from geonode (https://geonode.com/free-proxy-list)
ROTATING_PROXY_LIST = [
  '181.66.37.210:4153',
  '114.141.61.2:4145',
  '67.43.236.18:20067',
 ]

# Proxy settings for premium proxies with IP adress rotation eg from smartnet
PROXY_USER = "your_proxy_username"
PROXY_PASSWORD = "your_proxy_password"
PROXY_SERVER = "your.proxy.server"  # Example: "proxy.example.com"
PROXY_PORT = "8080"  # Example: 8080



#USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36'

# specifies where to save the data when crawl command is run
# FEEDS = {
#     'cleanedbooksdata.json': {'format': 'json'},
# }

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = "librascraper (+http://www.yourdomain.com)"

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
#    "Accept-Language": "en",
#}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    "librascraper.middlewares.LibrascraperSpiderMiddleware": 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
  # "librascraper.middlewares.LibrascraperDownloaderMiddleware": 543,
  "librascraper.middlewares.ScrapeOpsFakeBrowserHeaderAgentMiddleware": 400,
   
  # FOR THE POROXY MIDDLEWARE CLASS TO BE ADDED eg from smartproxy
  #  "librascraper.middlewares.MyProxyMiddleware": 300,
   
  # THE ROTATING PROXIES ARE TO BE USED WHEN FREE PROXIES ARE WORKING
  #  "rotating_proxies.middlewares.RotatingProxyMiddleware": 610,
  #  "rotating_proxies.middlewares.BanDetectionMiddleware": 620,
}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    "scrapy.extensions.telnet.TelnetConsole": None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   "librascraper.pipelines.LibrascraperPipeline": 100,
  # "librascraper.pipelines.SaveToMySQLPipeline": 200,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = "httpcache"
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = "scrapy.extensions.httpcache.FilesystemCacheStorage"

# Set settings whose default value is deprecated to a future-proof value
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"
