# LastFM Web Crawler for Metalheads by Neoclassic VII
# Written according to the principle: "If it works - do not touch it!". I could have found a better way to write this code, but it works fine as it is.
import time
import requests
import webbrowser 
import difflib
import colorama
from colorama import Fore
from bs4 import BeautifulSoup

colorama.init()

genres = [
"deathcore","power+metal","heavy+metal","death+metal","black+metal","thrash+metal","alternative+metal","nu+metal","folk+black+metal",
"trve+kvlt","symphonic+black+metal","ambient+black+metal","technical+deathcore","blackened+technical+death+metal","norwegian+black+metal","brutal+death+metal",
"neoclassical+death+metal","neoclassical+metal","electronicore","doom+metal","gothic+metal","djent","glam+metal","metalcore","groove+metal","progressive+metal",
"prog+metal","avant+garde+metal","folk+metal","grindcore","melodic+black+metal","cyber+metal","melodic+death+metal","mathcore","white+metal","industrial+metal",
"symphonic+deathcore","melodic+deathcore","slamming+deathcore","beatdown+deathcore","slamming+beatdown+deathcore","magical+death+metal",
"neoclassical+deathcore","pornogore","folk+deathcore","folk+death+metal","slamming+brutal+death+metal","powerviolence","crossover","shitgrind",
"pirate+metal","kawaii+metal","drone+metal","drone","math+metal","neue+deutsche+härte","ndh","technical+death+metal","black+death+metal"
]

def lastfm(genre):
  url = "https://www.last.fm/tag/"+str(', '.join(difflib.get_close_matches(genre,genres,1)))+"/artists"
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
