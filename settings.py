# replace DOWNLOADER_MIDDLEWARES from your settings.py  by this one  - you have to install scrapy_fake_useragent

DOWNLOADER_MIDDLEWARES = {
	## User agent
	'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
	#need pip install scrapy_fake_useragent  (in conda)
	'scrapy_fake_useragent.middleware.RandomUserAgentMiddleware': 400,

	## Proxy (privoxy + tor) 
	#cf https://trevsewell.co.uk/scraping/anonymous-scraping-scrapy-tor-polipo/
	# activate http proxy (turn on proxy)
	'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 110,
	# call the middleware to customize the http proxy  (set proxy to 'http://127.0.0.1:8118')
	'example.middlewares.ProxyMiddleware': 100,

}
