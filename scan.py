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
	# r = requests.get(url)
	# print("Scan done..")
	# return r.headers

def get_request(url):
	r = requests.get(url)
	print("Testing information disclosure through response headers")
	# response = r.text
	# print(r.headers)
	if "Server" or "X-Powered-By" in r.text:
		return True
	else:
		# print("No Server or X-Powered-By headers found..")
		return False

def post_request(url):
	r = requests.post(url)
	print("Testing information disclosure through response headers")
	response = r.text
	if "Server" or "X-Powered-By" in r.text:
		return True
	else:
		# print("No Server or X-Powered-By headers found..")
		return False

def head_request(url):
	r = requests.head(url)
	print("Testing information disclosure through response headers")
	response = r.text
	if "Server" or "X-Powered-By" in r.text:
		return True
	else:
		# print("No Server or X-Powered-By headers found..")
		return False		

def options_request(url):
	r = requests.options(url)
	print("Testing information disclosure through response headers")
	response = r.text
	if "Server" or "X-Powered-By" in r.text:
		return True
	else:
		# print("No Server or X-Powered-By headers found..")
		return False

def trace_request(url):
	r = requests.trace(url)
	print("Testing information disclosure through response headers")
	response = r.text
	if "Server" or "X-Powered-By" in r.text:
		return True
	else:
		# print("No Server or X-Powered-By headers found..")
		return False

def put_request(url):
	r = requests.put(url)
	print("Testing information disclosure through response headers")
	response = r.text
	if "Server" or "X-Powered-By" in r.text:
		return True
	else:
		# print("No Server or X-Powered-By headers found..")
		return False

def delete_request(url):
	r = requests.trace(url)
	print("Testing information disclosure through response headers")
	response = r.text
	if "Server" or "X-Powered-By" in r.text:
		return True
	else:
		# print("No Server or X-Powered-By headers found..")
		return False

def request_methods():
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
	print("\nApplication discloses information in Server: or X-Powered-By: header via %s method\n") % (i) 	


def cookie_attributes(url):
	# headers = {"Cookie": "JSESSIONID=F0DC6310EE44C69E712B9E703CB3E724"}
	# r = requests.post(url, headers = headers)
	r = requests.get(url)
	# print(r.headers)
	print(r.cookies)
	if 'Secure' not in r.headers['Set-Cookie']:
		print ("Secure Flag not set\n")
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

	# if cookie.domain 
	# print(r.text)
	# if 'Admin' in r.text:
	# print(r.headers['Set-Cookie'])
	for cookie in r.cookies:
		if cookie.domain not in url:
			print("Domain of Session Cookie is not set appropriately")

def hsts_header(url):
  	#if 'http' in url and r.headers['Strict-Transport-Security'] not in r.headers:
  	if 'https' in url and 'Strict-Transport-Security' not in r.headers:
  		print("Strict-Transport-Security header not set")

def content_security_policy(url):
	if 'Content-Security-Policy' not in r.headers:
		print("Content-Security-Policy header not set\n")

def content_type(url):
	if 'X-Content-Type-Options' not in r.headers:
		print("Missing X-Content-Type-Options header\n")

def cache_control(url):
	cc = ['no-cache', 'no-store', 'must-revalidate','max-age']
	if 'Cache-Control' not in r.headers:
		print("Cache-control header missing")
	elif cc not in r.headers['Cache-Control']:
			print("Cache-Control header not configured correctly")

	

url = "http://demo.testfire.net/"
r = requests.get(url)

if __name__ == '__main__':
	print(r.headers)
	head(url)
	request_methods()
	cookie_attributes(url)
	hsts_header(url)
	content_security_policy(url)
	content_type(url)
	cache_control(url)

print("End")
