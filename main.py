from urllib.request import urlopen
from urllib.error import HTTPError, URLError
from bs4 import BeautifulSoup


def gettingTitle(url):
	try:
		html = urlopen(url)
	except HTTPError as e:
		return None
	try:
		bsObj = BeautifulSoup(html.read())
		title = bsObj.body.h1
	except AttributeError as e:
		return None
	return title
title = gettingTitle("http://www.pythojvnscraping.com/pages/page1.html")
if title == None:
	print("Title could not be found")
else:
	print(title)
	# else:
	#     program continues. Note: If you return or break in the  
	#     exception catch, you do not need to use the "else" statement
   

 
# # importing modules
# import requests
# from urllib.error import URLError



# myurl = "https://www.elfinanciefsdsdfro.com.mx/"
# # myurl = "http://www.pythonsadasdcraping.com/pages/page1.html"
 
# url = 'https://www.geeksforgeeks.org/page-that-do-not-exist' 
# # url = 'https://www.geeksforgeks.org/implementing-web-scraping-python-beautiful-soup/'
 
# try:
#   response = requests.get(myurl)
#   response.raise_for_status()
# except URLError as ue:
#   print("The Server Could Not be Found")
   
# else:
#   print("No Error")