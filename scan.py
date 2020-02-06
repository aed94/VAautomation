import requests
import urllib
import urllib3
#for regex
import re 
import string
from requests.auth	import HTTPBasicAuth
urllib3.disable_warnings()


def head(url):
	print("Beginning scan on %s "%(url))
	print(" ")

def get_request(url):
	r = requests.get(url)
	print("Testing information disclosure through response headers")
	if "Server" or "X-Powered-By" in r.text:
		return True
	else:
		return False

def post_request(url):
	r = requests.post(url)
	print("Testing information disclosure through response headers")
	response = r.text
	if "Server" or "X-Powered-By" in r.text:
		return True
	else:
		return False

def head_request(url):
	r = requests.head(url)
	print("Testing information disclosure through response headers")
	response = r.text
	if "Server" or "X-Powered-By" in r.text:
		return True
	else:
		return False		

def options_request(url):
	r = requests.options(url)
	print("Testing information disclosure through response headers")
	response = r.text
	if "Server" or "X-Powered-By" in r.text:
		return True
	else:
		return False

def trace_request(url):
	r = requests.trace(url)
	print("Testing information disclosure through response headers")
	response = r.text
	if "Server" or "X-Powered-By" in r.text:
		return True
	else:
		return False

def put_request(url):
	r = requests.trace(url)
	print("Testing information disclosure through response headers")
	response = r.text
	if "Server" or "X-Powered-By" in r.text:
		return True
	else:
		return False

def delete_request(url):
	r = requests.trace(url)
	print("Testing information disclosure through response headers")
	response = r.text
	if "Server" or "X-Powered-By" in r.text:
		return True
	else:
		return False

def cookie_attributes(url):
	# headers = {"Cookie": "JSESSIONID=F0DC6310EE44C69E712B9E703CB3E724"}
	# r = requests.post(url, headers = headers)
	r = requests.get(url)

	if 'Secure' not in r.headers['Set-Cookie']:
		print("Secure Flag not set\n")
		print(r.headers['Set-Cookie'])
		print("\n")
	if 'HttpOnly' not in r.headers['Set-Cookie']:
		print ("HttpOnly Flag not set\n")
		print(r.headers['Set-Cookie'])
		print("\n")
	if 'Path=/' in r.headers['Set-Cookie']:
		print ("Path set to root\n")
		print(r.headers['Set-Cookie'])
		print("\n")

	for cookie in r.cookies:
		if cookie.domain not in url:
			print("Domain of Session Cookie is not set appropriately")

def strict_http(url):
	if 'https' in url and 'Strict-Transport-Security' not in r.headers:
		print("Missing Strict-Transport-Security headers\n")

def content_sec_policy(url):
	if 'Content-Security-Policy' not in r.headers:
		print("Missing Content-Security-Policy header missing")

url = "https://old.axismf.com/"
cookies = {"ASP.NET_SessionId":"c443xf3tdtqock2a1024oxxd"}
r = requests.get(url, cookies=cookies)
head(url)
#cookie_attributes(url)
strict_http(url)
content_sec_policy(url)

methods = ["GET", "POST", "HEAD", "TRACE", "OPTIONS", "PUT", "DELETE"]
for i in methods:
	if (get_request(url) == True):
		break
	elif (post_request(url) == True):
		break
	elif (head_request(url) == True):
		break
	elif (options_request(url) == True):
		break
	elif (trace_request(url) == True):
		break
	elif (put_request(url) == True):
		break
	elif (delete_request(url) == True):
		break
	else:
		print("Something went wrong.")
		break	
print("\nApplication discloses information in Server: or X-Powered-By: header via %s method") % (i) 	
