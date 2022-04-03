import os 
import time
import sys
import requests
from bs4 import BeautifulSoup
import difflib
import colorama
from colorama import Fore

colorama.init()

def lastfm(genre):
  url = "https://www.last.fm/tag/"+genre.strip().replace(" ","+")+"/artists"
  source = requests.get(url).text
  soup = BeautifulSoup(source, "lxml")

  bandlist = soup.find("ol", class_="big-artist-list")

  try:
    if not bandlist.text == "None": 
      print()
      time.sleep(0.5)
      print(Fore.GREEN + "[+] Last FM Page Found!")
      print(Fore.RED + "URL: " + Fore.BLUE + url)
      print()

      bandname = bandlist.find_all("h3", class_="big-artist-list-title")
      listeners = bandlist.find_all("p", class_="big-artist-list-listeners")

      print(Fore.YELLOW + "Bands:")
      print()

      for i in range(len(bandname)):
        print(Fore.RED + bandname[i].text + " " + Fore.WHITE + listeners[i].text.strip())

    else:
      pass

  except AttributeError:
    time.sleep(0.5)
    print("[-] No Last FM page found ")
    pass
