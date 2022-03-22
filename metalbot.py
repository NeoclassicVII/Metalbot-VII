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
  import pyfiglet
  import difflib 
  import colorama
  from colorama import Fore
  from pyfiglet import figlet_format
  from metalinjection import metalnews
  from lastfm import lastfm

  colorama.init()

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
    print("[" + Fore.RED + "WARNING!" + Fore.WHITE + "] " + Fore.GREEN + "Please type the name of the genre/subgenre fully and correctly! Otherwise the program may not work!")
    print(Fore.WHITE)
    nl()
    time.sleep(1)

    ask = print(Fore.YELLOW + "Which subgenre/genre? " + Fore.WHITE, end='')
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
    "Symphonic Deathcore","Folk Deathcore","Neoclassical Deathcore","Porngrind","Pornogore","Folk Deathcore","Folk Death Metal"
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
        sys.exit()

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
  try:
  	metalnews()
  except (requests.ConnectionError, requests.Timeout) as exception:
  	pass

  print("[1] Random band recomendation")
  print("[2] Info about genres/subgenres, band recomendation")
  print("[3] Contact/Info")
  print("[4] Lyrics Founder")
  print(Fore.RED + "[666] Exit")
  nl()
  print(Fore.YELLOW + "Choose option: " + Fore.WHITE, end='')

  global choice
  choice = input()

  if choice == str("1"):
    first_option()

  elif choice == str("2"):
    second_option()

  elif choice == str("3"):
    third_option()
  
  elif choice == str("4"):
  	print("minpen")

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
  
