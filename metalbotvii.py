# Created by Neoclassic VII
# This program is for Metalheads only.
#
# Written according to the principle: "If it works - do not touch it!".
#
# INFO: Neoclassic VII is a great composer and creator of the genre called "Magical Death Metal". This program is his
# first biggest program he ever created. Before this he created some calculators etc. So please keep this in mind
# and don't judgе too harshly. 
# For any questions and/or ideas, please contact him оn Telegram: @MetalheadDumbledore
#
# Check out the Telegram translation by Neoclassic VII called "Metalgram" (it's in russian).
# Metalgram is a custom Telegram language created for Metalheads.
# Link for Metalgram: https://t.me/setlanguage/metalgramm
#
# Good luck by using and modifying!
#
# (C) Neoclassic VII
#
# Stage One: [complete]
# Stage Two: [complete]
# Stage Three: [in process]
# Stage Four: ?
# ...
#

try:
  import time
  import os
  import sys
  import random 
  import requests
  import webbrowser
  import wikipedia
  import youtube_dl
  import lyricsgenius as lg
  import pyfiglet
  import difflib 
  import colorama
  from bs4 import BeautifulSoup
  from youtubesearchpython import VideosSearch
  from colorama import Fore
  from pyfiglet import figlet_format
  from metalinjection import metalnews
  from lastfm import lastfm

  colorama.init()

  genius = lg.Genius("EF_15CbfRDACICgKOAi1DeJC5QugglpFHh-cXHd1pPUfp2Z-_pNVVli49LEjQe4W")

  # Startup Screen
  os.system("cls")
  time.sleep(0.3)

  with open("ASCII Art.txt", "r", encoding='utf-8') as asciiart:
    art = asciiart.read()
    print(Fore.RED + art + Fore.WHITE)
    print(Fore.GREEN + "By Neoclassic VII".center(75) + Fore.WHITE)
 
  time.sleep(1.5)
  os.system("cls")

except KeyboardInterrupt:
  import sys
  print("\n")
  print("_" * 25)
  print("Exiting the program...")
  print("_" * 25)
  sys.exit()  


# New-line 
def nl():
  print("\n")


# Back to menu
def back_to_menu():
  os.system("cls")
  time.sleep(1)
  nl()
  print(Fore.RED + "Back to menu..." + Fore.WHITE)
  time.sleep(1) 
  menu()


# The first option of the program
def first_option():
  def cls_cmd():
  	time.sleep(1)
  	os.system("cls")
  	nl()
  	nl()

  cls_cmd()
  print(Fore.CYAN + "The generation will start in [3]...".center(75) + Fore.WHITE)
  cls_cmd()
  print(Fore.CYAN + "The generation will start in [2]...".center(75) + Fore.WHITE)
  cls_cmd()
  print(Fore.CYAN + "The generation will start in [1]...".center(75) + Fore.WHITE)
  time.sleep(0.8)

  while True:
    os.system("cls")
      
    with open("metal_bands_2022.txt", "r", encoding='utf-8') as bands:
      read = bands.readlines()
      os.system("cls")
      nl()
      print(Fore.CYAN + pyfiglet.figlet_format("Random Bands"))
      nl()
      print(Fore.RED + "*ENTER to generate!*".center(72))
      print("*Type 666 to go back to the menu!* ".center(72))
      nl()

      for bands in range(80):
        sys.stdout.write(Fore.WHITE + random.choice(read).strip().center(70) + "\r")
        sys.stdout.flush()
        time.sleep(0.02) 
          
      input_ = input()

    if input_ == "666":
      back_to_menu()

    else:
      pass


# The second option of the program
def second_option():
  while True:
    time.sleep(1)
    os.system("cls")
    print(Fore.BLUE + pyfiglet.figlet_format("Genres"))
    print(Fore.RED + "*Type 666 to go back to the menu!*" + Fore.WHITE)
    nl()
    print("[" + Fore.BLUE + "!" + Fore.WHITE + "] " + Fore.GREEN + "Please type the name of the genre/subgenre fully and correctly! Otherwise the program may not work!")
    nl()
    time.sleep(0.7)
    print(Fore.RED + "[EXAMPLE]" + Fore.WHITE)
    print("Black Death " + Fore.RED + "Metal" + Fore.WHITE)
    print("Neoclassical Death " + Fore.RED + "Metal" + Fore.WHITE)
    print("Melodic Death " + Fore.RED + "Metal" + Fore.WHITE)
    print("Symphonic Deathcore")
    print(Fore.GREEN + "etc..." + Fore.WHITE)
    nl()
    time.sleep(1)

    ask = print(Fore.YELLOW + "- Which subgenre/genre? " + Fore.WHITE, end='')
    launch = input().lower()

    genres = [
    "Deathcore","Power Metal","Heavy Metal Music","Death Metal","Black Metal",
    "Groove Metal","Thrash Metal","Alternative Metal","Nu Metal","Progressive Metal","Black-Death Metal",
    "Black Death Metal","Blackened Death Metal",
    "Technical Death Metal","Metalcore","White Metal","Melodic Death Metal","Folk Metal","Neoclassical Death Metal",
    "Doom Metal","Industrial Metal","Gothic Metal","Djent","Avant-Garde Metal","Prog Metal","Glam Metal",
    "Symphonic Deathcore","Technical Deathcore","Blackened Technical Death Metal","Grindcore","Trve Kvlt",
    "Norwegian Black Metal","Electronicore","Magical Death Metal",
    "Mathcore","Symphonic Black Metal","Ambient Black Metal","Folk Black Metal",
    "Brutal Death Metal","Melodic Black Metal","Neoclassical Metal","Cyber Metal",
    "Symphonic Deathcore","Melodic Deathcore","Beatdown Deathcore","Slamming Deathcore","Slamming Beatdown Deathcore","Folk Deathcore",
    "Neoclassical Deathcore","Porngrind","Pornogore","Folk Deathcore","Folk Death Metal","Slamming Brutal Death Metal","Powerviolence","Crossover",
    "Shitgrind","Pirate Metal","Kawaii Metal","Drone Metal","Drone","Math Metal","Neue Deutsche Härte","Ndh","Blackened Deathcore"
    ]

    if launch == "666":
      back_to_menu()

    try:

      if difflib.get_close_matches(launch,genres,1):
        nl()
        time.sleep(0.6)
          
        try:

          if wikipedia.summary(", ".join(difflib.get_close_matches(launch,genres,1)), sentences = 5, auto_suggest = False):
            print(Fore.GREEN + "[+] Wikipedia Page Found!" + Fore.WHITE)
            nl()
            print(Fore.CYAN + wikipedia.summary(", ".join(difflib.get_close_matches(launch,genres,1)), sentences = 5, auto_suggest = False))  

          else:
            pass

        except wikipedia.exceptions.PageError:
          time.sleep(0.5)
          print(Fore.RED + "[-] No Wikipedia page found " + Fore.WHITE)
          pass

        lastfm(launch)

        time.sleep(1)
        nl()
        print(Fore.RED + "[+] " + Fore.WHITE + "Press ENTER to search in browser:", end='') 
        print(Fore.WHITE)
        search = input()

        if search == "666":
          back_to_menu()

        time.sleep(1)
        nl()
        print(Fore.BLUE + "I'll redirect you to google in a moment, so you can find information about that genre!")
        print(Fore.GREEN + "." * 86, Fore.WHITE)

        time.sleep(3)
        url="https://www.google.com/search?q="+str(", ".join(difflib.get_close_matches(launch,genres,1)))+""
        webbrowser.open(url)
        nl()
        startagain = print(Fore.RED + "Click [ENTER] to start again OR type \"666\" to go back to menu: " + Fore.WHITE, end="")
        startagian_ = input()

        if startagian_ == "666":
        	back_to_menu()
        else:
        	second_option()

      else:
        nl()
        time.sleep(1)
        print("I don't know such a genre. ")
        time.sleep(1)
        os.system("cls")

    except (requests.ConnectionError, requests.Timeout) as exception:
      time.sleep(0.6)
      print("[-] " + Fore.RED + "No Internet Connection!" + Fore.WHITE)
      time.sleep(0.9)
      menu()


# The third option of the program
def third_option():
	time.sleep(0.7)
	os.system("cls")
	print(Fore.WHITE + pyfiglet.figlet_format("Lyrics Founder"))
	nl()
	print(Fore.RED + "*Type 666 to go back to the menu!*" + Fore.WHITE)
	time.sleep(0.4)
	nl()
	time.sleep(0.6)
	print("[" + Fore.BLUE + "!" + Fore.WHITE + "] " + Fore.YELLOW + "Type the name of the band" + Fore.RED + " and " + Fore.YELLOW + "the song fully and correctly!" + Fore.WHITE)
	nl()
	time.sleep(1.7)
	print(Fore.CYAN + "[EXAMPLE]" + Fore.WHITE)
	print(" - Band name: " + Fore.RED + "Archspire" + Fore.WHITE)
	print(" - Song name: " + Fore.RED + "Drone Corpse Aviator" + Fore.WHITE)
	time.sleep(1.1)
	nl()
	thebandname = print(Fore.GREEN + "- Band name: " + Fore.WHITE, end="")
	theband = input().lower()
	
	if theband == "666":
		back_to_menu()

	thesongname = print(Fore.GREEN + "- Song name: " + Fore.WHITE, end="")
	thesong = input().lower()
	nl()

	if thesong == "666":
		back_to_menu()

	try:
		song = genius.search_song(title=thesong, artist=theband)
		lyrics = song.lyrics
		time.sleep(1)
		nl()
		print(Fore.LIGHTBLACK_EX + lyrics + Fore.WHITE)
		nl()
		repeat = print(Fore.RED + "Click [ENTER] to start again OR type \"666\" to go back to menu: " + Fore.WHITE, end="")
		repeat_= input()

		if repeat_ == "666":
			back_to_menu()
		else:
			third_option()

	except AttributeError:
		time.sleep(0.8)
		nl()
		print(Fore.WHITE + "[" + Fore.RED + "-" + Fore.WHITE + "] " + Fore.RED + "No Lyrics Found!")
		time.sleep(1.5)
		third_option()
	except (requests.ConnectionError, requests.Timeout) as exception:
		time.sleep(0.7)
		nl()
		print(Fore.RED + "[-] No Internet Connection!")
		print(Fore.WHITE)
		time.sleep(1.3)
		back_to_menu()
	except requests.exceptions.ConnectionError as exception:
		time.sleep(0.7)
		nl()
		print(Fore.RED + "[-] No Internet Connection!")
		print(Fore.WHITE)
		time.sleep(1.3)
		back_to_menu()


def music_download():
  # Song Downloader 
  def songDownloader():
    ydl_opts = {
      'format':'bestaudio/best',
      'keepvideo':False,
      'outtmpl': os.environ['USERPROFILE'] + '\\Music\\' + filename
      }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
      ydl.download([link])
      print()
      print(Fore.GREEN + "[+] " + Fore.WHITE + "Song successfully downloaded!")
      time.sleep(1.2)
      print()
      startagain = print(Fore.YELLOW + "Click ENTER to start again OR type 666 to go back to menu: " + Fore.WHITE, end="")
      again = input()

      if again == str("666"):
        back_to_menu()
      else:
        music_download()

  # LastFM URL's
  LASTFM_URL = "https://www.last.fm"
  searchURL = "https://www.last.fm/search?q="

  # Genres (Tags)
  genres = [
  "deathcore","power metal","heavy metal","death metal","black metal","thrash metal","alternative metal","nu metal","folk black metal",
  "trve kvlt","symphonic black metal","ambient black metal","technical deathcore","blackened technical death metal","norwegian black metal","brutal death metal",
  "neoclassical death metal","neoclassical metal","electronicore","doom metal","gothic metal","djent","glam metal","metalcore","groove metal","progressive metal",
  "prog metal","avant garde metal","folk metal","grindcore","melodic black metal","cyber metal","melodic death metal","mathcore","white metal","industrial metal",
  "symphonic deathcore","melodic deathcore","slamming deathcore","beatdown deathcore","slamming beatdown deathcore","magical death metal",
  "neoclassical deathcore","pornogore","folk deathcore","folk death metal","slamming brutal death metal","powerviolence","crossover","shitgrind",
  "pirate metal","kawaii metal","drone metal","drone","math metal","neue deutsche härte","ndh","technical death metal","black death metal","metal",
  "blackened deathcore"
  ]

  time.sleep(0.7)
  os.system("cls")
  print(Fore.MAGENTA + pyfiglet.figlet_format("Music Downloader"))
  print()
  print(Fore.RED + "*Type 666 to go back to the menu!*" + Fore.WHITE)
  time.sleep(0.4)
  print()
  time.sleep(0.6)
  print("[" + Fore.BLUE + "!" + Fore.WHITE + "] " + Fore.YELLOW + "Type the name of the band" + Fore.RED + " and " + Fore.YELLOW + "the song fully and correctly!" + Fore.WHITE)
  print()
  time.sleep(1.7)
  print(Fore.YELLOW + "[EXAMPLE]" + Fore.WHITE)
  print("- Lorna Shore Death Portrait")
  time.sleep(1.1)
  print()
  songSearch = print(Fore.CYAN + "- Which song? " + Fore.WHITE, end="")

  # The song
  song = input()

  if song == str("666"):
    back_to_menu()

  print()

  # Finds the song in LastFM
  try:
    source = requests.get(searchURL+song).text
  except (requests.ConnectionError, requests.Timeout) as exception:
    time.sleep(0.7)
    nl()
    print(Fore.RED + "[-] No Internet Connection!")
    print(Fore.WHITE)
    time.sleep(1.7)
    back_to_menu()

  soup = BeautifulSoup(source, "lxml")
  findSongList = soup.find("tbody")

  if findSongList == None:
    time.sleep(0.7)
    print(Fore.RED + "[-]" + Fore.WHITE + " No song found! ")
    time.sleep(1.2)
    os.system("cls")
    music_download()

  findSong = findSongList.find("tr")
  findUrl = findSong.find("td", class_="chartlist-name").a

  # The song URL (If it did find one)
  songURL = findUrl ["href"]

  # Checks the genre of song
  genreRequest = requests.get(LASTFM_URL+songURL).text
  soupCheck = BeautifulSoup(genreRequest, "lxml")
  findTag = soupCheck.find("section", class_="catalogue-tags").ul

  if findTag == None:
    time.sleep(0.7)
    print()
    print(Fore.RED + "[-] No song found!" + Fore.WHITE)
    time.sleep(1.1)
    music_download()

  tags = findTag.find_all("li", class_="tag")

  for tag in tags:
    if tag.text in genres:
      def youtubeFinder(song):
        os.system("cls")
        time.sleep(0.4)
        print(Fore.RED + pyfiglet.figlet_format("Choose the song"))
        search = VideosSearch(song, limit = 6).result()

        for results in range(6):
          songTitle = search ['result'][results]['title']
          print(Fore.BLUE + "[","{}".format(results),"] " + Fore.YELLOW,songTitle)

        print()
        choose = print(Fore.GREEN + "Choose the one, that you want to download: " + Fore.WHITE, end="")
        thechoice = input()

        if thechoice <= str(6):
          global link,filename
          link = search ['result'][int(thechoice)]['link']
          filename = f"{search ['result'][int(thechoice)]['title']}.mp3"
          print()
        else:
          print()
          time.sleep(0.6)
          print(Fore.RED + "Choose the right one!" + Fore.WHITE)
          time.sleep(0.8)
          youtubeFinder(song)

      youtubeFinder(song)

      # Downloads the song
      songDownloader()

  # If not supported genre (if not metal)
  if tags[-1].text not in genres:
    time.sleep(0.7)
    print()
    print(Fore.RED + "[-] No song found!" + Fore.WHITE)
    time.sleep(1.1)
    music_download()


# Contact/Info
def contact():
  time.sleep(1)
  os.system("cls")
  print(Fore.CYAN + pyfiglet.figlet_format("Contact"))
  print(Fore.RED + "*Type 666 or just click [Enter] to go back to the menu!*")
  nl()
  print(Fore.RED + "Telegram: " + Fore.GREEN + "@MetalheadDumbledore")
  print(Fore.RED + "Instagram: " + Fore.GREEN + "boka.musayelyan")
  print(Fore.RED + "E-Mail: " +  Fore.GREEN + "bokamusayelyanwindows@gmail.com")
  nl()
  print(Fore.RED + "Other projects:")
  nl()
  print(Fore.GREEN + "Metalgram (In procces)")
  print(Fore.CYAN + "Metalgram is a custom Telegram language (In Russian) created for Metalheads.")
  nl()
  print(Fore.RED + "LINK: " + Fore.GREEN + "https://t.me/setlanguage/metalgramm" + Fore.YELLOW)
  nl()
  print("(C) Neoclassic VII" + Fore.WHITE)

  backtomenu = input()
    
  if backtomenu == "666":
    back_to_menu()

  else: 
    back_to_menu()


# Exiting the program
def exit():
  time.sleep(0.5)
  nl()
  print(Fore.RED + "Exiting the program..." + Fore.WHITE)
  time.sleep(0.5)
  sys.exit()


# Main menu
def menu():
  os.system("cls")
  print(Fore.GREEN + pyfiglet.figlet_format("Metalbot VII") + Fore.WHITE)
  metalnews()
  print("[1] Random band recomendation")
  print("[2] Info about genres/subgenres, band recomendation")
  print("[3] Lyrics Founder (Not only Metal)")
  print("[4] Music Downloader")
  print("[99] Contact")
  print(Fore.RED + "[666] Exit")
  nl()
  print(Fore.LIGHTGREEN_EX + "Choose option: " + Fore.WHITE, end='')

  global choice
  choice = input()

  if choice == str("1"):
    first_option()

  elif choice == str("2"):
    second_option()

  elif choice == str("3"):
    third_option()
  
  elif choice == str("4"):
    music_download()

  elif choice == str("99"):
  	contact()

  elif choice == str("666"):
    exit()

  else:
    os.system("cls")
    time.sleep(0.8)
    menu()


# Exception
try:
  menu()
except KeyboardInterrupt:
  import sys
  print("\n")
  print("_" * 25)
  print("Exiting the program...")
  print("_" * 25)
  sys.exit()  
