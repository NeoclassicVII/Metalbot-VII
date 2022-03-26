# Daily Metal News by Neoclassic VII
# from [metalincetion.com]

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

    findnews = soup.find("div", class_="zox-feat-ent1-cont zoxrel")
    titel = findnews.find_all("div", class_="zox-art-title")
    print(Fore.LIGHTBLACK_EX + "#" * 58)
    print(Fore.WHITE)
    print(Fore.RED + "[Latest News]".center(55) + Fore.WHITE)
    moreinfo = findnews.find_all("p", class_="zox-s-graph")

    for i in range(len(titel)):
        print(Fore.YELLOW + "  " + titel[i].text + " " + Fore.LIGHTCYAN_EX + moreinfo[i].text + Fore.WHITE)
    print()
    print(Fore.LIGHTBLACK_EX + "#" * 58)
    print(Fore.WHITE)

  except (requests.ConnectionError, requests.Timeout) as exception:
  	print(Fore.RED + "[Latest News]".center(55) + Fore.WHITE)
  	print(Fore.RED + "[-] No Internet Connection!".center(55))
  	print(Fore.WHITE)
  	pass
