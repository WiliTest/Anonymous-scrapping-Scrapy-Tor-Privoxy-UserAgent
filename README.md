# Anonymous-scrapping-Scrapy-Tor-Privoxy-UserAgent
A tuto showing how to use scrapy in anonymous way (ex: changing IP)




#### Here is just _a draft_ of informations I would have loved to find in one place:
_Sorry the formatting is messed up (no time), you are very welcome to improve it !_

■■■ **About port number & proxy**

● `9051` :  If ControlPort is set ( with this port, in torrc file), Tor will accept connections on this port and allow those connections to control the Tor process using the Tor Control Protocol. 
Unless you also specify one or more of HashedControlPassword or CookieAuthentication, setting this option will cause Tor to allow any process on the local host to control it. This option is required for many Tor controllers; most use the value of 9051.
	
● `9050` (it's the socks5 port) it's the default port Tor uses for listening for SOCKS5 proxy connections. You use it if you want to proxy something through Tor.	SOCKS proxy only deal with the connection (notwork protocol IP, port) it doesn't see the infoormation of the request (such as HTML). (9050 needs the tor win32 services running )  
		
● `9150` is the same thing, only it's the default for Tor Browser Bundle. Since the TBB has to run Tor in the background, it might as well make the port available for you to use outside of the browser while it is running. (9150 only work when tor bronwser run, it doesnt need the service). 


● Proxy looks like: `https://<proxy>:<port>/`
	
	
● _What's the difference between privoxy/tor htpps vs socks?_
https://security.stackexchange.com/questions/45606/how-tor-privoxy-vidalia-and-polipo-are-getting-together
		
● tor is a SOCKS proxy (doesnt understand TCP traffic) but privoxy (and polipo) are HTTP proxies

● Privoxy is a proxy server that (pay attention here) uses application-layer filtering. HTTP traffic passed through Privoxy will have certain privacy-oriented rules applied to them. For example, Privoxy will block ads, detect and disable click-tracking scripts, disabling pop-ups, etc.
		
● _What's the difference between ControlPort and SocksPort?_
https://tor.stackexchange.com/questions/12627/whats-the-difference-between-controlport-and-socksport

● Info set tor IP change: https://stackoverflow.com/questions/30286293/make-requests-using-python-over-tor/30440372#30440372

	
■■■ **Using Tor Expert Bundle (see bellow for Tor Brownser)**

● dwd it here: https://www.torproject.org/download/download.html.en
	
	
1) Set a password in using cmd prompt:

`C:\Users\User\Desktop\Tor\Tor>tor.exe --hash-password "dz#X2nB%LJHGF0sB9DnZWv#E0nJR" | more `

It will give you a hash (looks like: `16:4E9AE...`) Copy it, you'll need it for the torrc file.
(You could also set a cookie https://stem.torproject.org/tutorials/the_little_relay_that_could.html )
		
2)  Create the "torrc" file (without any extension) in C:\Users\User\Desktop\Tor\torrc
				
3) Add that to the torrc file:
```
ControlPort 9051
If you enable the controlport, be sure to enable one of these
authentication methods, to prevent attackers from accessing it.
HashedControlPassword 16:04C7A70H876B7BS6B69EE768NV7375CA2B7493414372
```			
● some info about torrc + list of option you can enable on it : 			https://tor.stackexchange.com/questions/6712/using-the-tor-expert-bundle-on-windows
					
● to refresh tor, you need to remove + recreate the service `Tor Win32`. Using the cmd prompt (the path point to the torrc file) 
run one after the other:
```
C:\Users\User\Desktop\Tor\Tor>tor.exe --service remove
C:\Users\User\Desktop\Tor\Tor>tor.exe --service install -options -f "C:\Users\user\Desktop\Tor\torrc"
C:\Users\User\Desktop\Tor\Tor>tor.exe --service install -options -f "C:\Users\user\Desktop\tor-win32-0.3.1.7\torrc"
```

if `StartService() failed : Access is denied` see: https://stackoverflow.com/a/47291114/1486850 

			
**to test it:**
		
● If you type `netstat -ano` (`-an` = witout pid) you will now see that port 9051 is open
			
● to check your exit ip write these code:
	https://stackoverflow.com/a/33875657/1486850
			
● to try you need:
	`pip install stem` (in Conda )
	`pip install request` 
	
+ if you have `error " Missing dependencies for SOCKS support` try: 
`pip install -U requests[socks]` . ( `pip install request[socks]` did not work for me)

(alternative: https://github.com/aivarsk/scrapy-proxies )
	
■■■ **Privoxy**

● why do I need privoxy: https://security.stackexchange.com/a/45610/90756 
	
● a socks proxy can't see what the request contains (ge. it can't see the HTML), an HTTP proxy can see the HTML and it can filter (remove stuff inside such as adds, java that spy you ...)

● install privoxy from here https://www.privoxy.org/
run the .exe, follow the instruction
then follow that https://superuser.com/a/1130890/235752 

● use them in a scrapy project: https://stackoverflow.com/questions/45009940/scrapy-with-privoxy-and-tor-how-to-renew-ip/45010141 

● in Privoxy, config.txt uncomment:

`forward-socks5   /               127.0.0.1:9050`

(By default it listens at port 8118)

	
■■■ **Auto switch user agent**

● pip install scrapy-fake-useragent

● Follow the steps:  https://github.com/alecxe/scrapy-fake-useragent  (need to write in settings.py)
	
● to check it:

``` 
def parse(self, response):
   print response.request.headers['User-Agent']
```
		
		
■■■ **If you use tor brownser (bad idea):**

● just write these code : 	https://stackoverflow.com/a/33875657/1486850  *but change all 9050 into 9150 !*
			
● you don't need the password authentication option since it will use cookie auth.
https://tor.stackexchange.com/questions/16014/windows-tor-browser-error-after-editing-torrc-file/16015?noredirect=1#comment18169_16015 
	● to try you need:
			pip install request[socks] 
	
		
