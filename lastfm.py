# LastFM Web Crawler for Metalheads by Neoclassic VII
import webbrowser 
import requests
import difflib, time
from colorama import Fore
from bs4 import BeautifulSoup

def nl():
	print("\n")

def lastfm(name):

	genres = ["deathcore","power+metal","heavy+metal","death+metal","black+metal","groove+metal","thrash+metal","alternative+metal","nu+metal","folk+black+metal"]

	source = requests.get("https://www.last.fm/tag/"+str(', '.join(difflib.get_close_matches(name,genres,1)))+"/artists").text

	#url = "https://www.last.fm/tag/"+str(', '.join(difflib.get_close_matches(launch,genres,1)))+"/artists"
	#webbrowser.open(url)

	soup = BeautifulSoup(source, "lxml")
	ol = soup.find("ol", class_="big-artist-list")

	try:
		if not ol.text == "None":
			nl()
			time.sleep(0.5)
			print(Fore.GREEN + "[+] Last FM Page Found!" + Fore.CYAN)
			nl()  
          	

			ilone =	ol.find("li")
			time.sleep(0.5)
			firstband = print(ilone.h3.text)
			firstlisten = print(ilone.p.text.strip())
			firstinfo = ilone.find("div", class_="big-artist-list-bio")
			nl()
			print(firstinfo.text)

			nl()
			time.sleep(0.5)
			print(Fore.YELLOW + "_"*139 +  Fore.CYAN)
			nl()

			ilonenext = ilone.find_next("li")
			ilonenext2 = ilonenext.find_next("li")
			firstband2 = print(ilonenext2.h3.text)
			firstlisten2 = print(ilonenext2.p.text.strip())
			firstinfo2 = ilonenext2.find("div", class_="big-artist-list-bio").p
			nl()
			print(firstinfo2.text)
			time.sleep(0.5)

		else:
			pass

	except AttributeError:
		time.sleep(0.5)
		print("[-] No Last FM page found ")
		pass