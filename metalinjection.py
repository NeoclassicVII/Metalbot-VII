import time
import requests
import webbrowser
import colorama
from bs4 import BeautifulSoup
from colorama import Fore

colorama.init()

URL = "https://metalinjection.net/"

def metalnews():
	try:
		source = requests.get(URL).text
		soup = BeautifulSoup(source, "lxml")

		findnews = soup.find("div", class_="zox-art-text")
		print(Fore.RED + findnews.div.h3.text)
		titel = findnews.find("div", class_="zox-art-title")
		print(Fore.GREEN + titel.text)
		moreinfo = findnews.find("p", class_="zox-s-graph")
		print(Fore.GREEN + moreinfo.text)
		print(Fore.WHITE)

	except ConnectionError:
		pass