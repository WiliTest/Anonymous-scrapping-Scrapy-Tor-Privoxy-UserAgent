## set proxy to privoxy and use Tor to change Ip
# # from https://trevsewell.co.uk/scraping/anonymous-scraping-scrapy-tor-polipo/

# set your password cf line 21

from stem import Signal
from stem.control import Controller
import requests
from scrapy import signals

def retrieve_ip():
	# get info (IP...) from current connection 
	session = requests.session() 
	# Tor uses the 9050 port as the default socks port. You use it if you want to proxy something through Tor
	session.proxies = {'http':  'socks5://127.0.0.1:9050',
					'https': 'socks5://127.0.0.1:9050'}
	return session

def set_new_ip():
	with Controller.from_port(port=9051) as controller:
		controller.authenticate(password="add your Tor password here") 
		controller.signal(Signal.NEWNYM)
				
class ProxyMiddleware(object):  #ProxyMiddleware_try_with_print(object):#

	def process_request(self, request, spider):
		'''
		> short version: replace everything in this def by: 
		set_new_ip()
		request.meta['proxy'] = 'http://127.0.0.1:8118'
		
		> long verion : 
		the print display the IP address, to show that Tor change it 		
		'''
		print("\n\nProxyMiddleware: Start")		
		site = 'http://httpbin.org/ip'
		
		# get public IP
		print("my normal public IP", requests.get(site).text)
		
		# get Tor IP
		my_ip = retrieve_ip()
		print("IP visible through Tor(request)", my_ip.get(site).text) 

		# change IP, retrieve it to print it
		set_new_ip()   # ask Tor to change IP
		my_ip = retrieve_ip()
		print("IP visible through Tor (stem)", my_ip.get(site).text)
		
		# get request from spider and ask it to go through a proxy (privoxy = 'http://127.0.0.1:8118'  - privoxy acts like a man-in-the-middle in the computer
		request.meta['proxy'] = 'http://127.0.0.1:8118'
		print("proxy used: ", request.meta['proxy'])
		
		print("\n\nProxyMiddleware: End")	
