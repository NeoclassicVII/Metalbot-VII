# Created by Neoclassic VII
# This program is for Metalheads only.
#
#
# INFO: Neoclassic VII is a great composer and creator of the genre called "Magical Death Metal". This program is his first
# biggest program he ever created. Before this he created some calculators etc. So please keep this in mind 
# and don't judgе too harshly. 
# For any questions and/or ideas, please contact him оn Telegram: @MetalheadDumbledore
#
# Check out the Telegram translation by Neoclassic VII called "Metalgram" (it's in russian). Metalgram is a custom Telegram language created for Metalheads.
# Link for Metalgram: https://t.me/setlanguage/metalgramm
# Good luck by using and modifying!
#
# (C) Neoclassic VII
#
# Stage One: [complete]
# Stage Two: [in procces]
# Stage Three: ?
# Stage Four: ?
# ...
#
# [NOTES ONLY FOR NEOCLASSIC VII:]
# #Pafiksit error s vikipediey (kagda statya nesushestvuet). Nayti sposob
# #paluchit ssilku ot vikipedii i redirektnuca srazu v vikipediyu a ne v brauzer. !(Vsyo resheno v ume, 10.03.22, 20:05)!
# 
# Astalnoe uznaem v pracesse vsivo etovo, ibo stopracentna v processe budut poyavlyaca novie bagi i errori. Vot. [9.03.22, 17:32]
# !A, blya. Zabil. Yisho nada papolnit spiski grupp i janrov. Vot. [9.03.22, 17:35]
# !Rabotat s dizaynom v celom. Vot. [9.03.22, 17:42] (uje est kakieto karektirovki [10.03.22, 20:06])
# 
# [10.03.22, 20:06] 1)!Pafiksil GRUBEYSHIY bag v mudole vikipedii, tiper vsyo vrodibi daljno narmalno rabotat (bag ne v mayom kode a v samom module).
# Esli vsyoje budut kasyaki, doljen budu nayti drugoy modul dlya raboti s dannimi i s informaciey. 
# 2) Poigralsa s dizaynom. Vsyo norm, no doljen rabotat dalshe. 
#
# P.S: Vcherashnie zadachi [a imenno, zadachi [9.03.22, 17:32/17:35/i otchasti 17:42] vsyo yisho v sile. Toyest nad nimi predstait yisho rabotat]
# P.S [2]: !Ya daje ne gavaryu a tom, shto novie idei dlya dalneyshey realizacii payavlyayuca nejeli v kajduyu sekundu. Tak shto da, takje nado chatelnee
# rabotat s ideyami i realizavat ix
#
# [11.03.22, 23:11] Sozdal fayl dlya raboti s randomnoy rekomendaciey grupp. Sozdal yisho takoy je dlya raboti s janrami i s vikipediey,
# no izza yobanix kasyakov samoy bibliateki (patamushta bez vikipedii vsyo rabotaet narmalno), nixuya ne vishlo. Tachnee vishlo, no s ispolzovaniem
# argumenta 'auto_suggest = False' vidayot ashibku: KeyError: 'fullurl'. Mojet budu sprashivat v forumax vsyakix, no eto nesiryozno, mojno ispolzovat
# spisok i bez fayla, sobstvenno, kak ranshe, da i kak seychas. 
#
# Plani na [BLIJAYSHEE] budushee: budu igraca s dizaynom i esli budet vozmojno, budu ispravit kasyak s vikipediey. Papolnyu spiski janrov i grupp, 
# pridumayu idei dlya novix opciy pragrammi.
#

try:
  import os, sys, requests, time, random, webbrowser, wikipedia, pyfiglet, difflib
  from colorama import Fore
  from pyfiglet import figlet_format

  # Startup Screen
  os.system("cls")
  time.sleep(0.3)

  print(Fore.RED + """
                                   ______              
                              .d$$$******$$$$c.        
                           .d$P"            "$$c      
                          $$$$$.           .$$$*$.    
                        .$$ 4$L*$$.     .$$Pd$  '$b   
                        $F   *$. "$$e.e$$" 4$F   ^$b  
                       d$     $$   z$$$e   $$     '$. 
                       $P     `$L$$P` `"$$d$"      $$ 
                       $$     e$$F       4$$b.     $$ 
                       $b  .$$" $$  VII .$$ "4$b.  $$ 
                       $$e$P"    $b     d$`    "$$c$F 
                       '$P$$$$$$$$$$$$$$$$$$$$$$$$$$  
                        "$c.      4$.  $$       .$$   
                         ^$$.      $$ d$"      d$P    
                           "$$c.   `$b$F    .d$P"     
                             `4$$$c.$$$..e$$P"        
                                 `^^^^^^^`
   """ )

# Sorry about this ugliness (if you know what I mean)
  print(Fore.GREEN +  "                             By Neoclassic VII      " + Fore.WHITE)

  time.sleep(1.5)
  os.system("cls")

except KeyboardInterrupt:
  import time
  import sys
  print("\n")
  print("_" * 25)
  print("Exiting the program...")
  print("_" * 25)
  time.sleep(0.1)
  sys.exit()  

# Main Program
def main():
# New-Line-Function
  def nl():
    print("\n")

  os.system("cls")
  print(Fore.GREEN + pyfiglet.figlet_format("Metalbot VII") + Fore.WHITE)
  print("[1] Random band recomendation")
  print("[2] Info about genres/subgenres, band recomendation")
  print("[3] Contact/Info")
  print(Fore.CYAN + "[666] Exit")
  nl()
  print(Fore.YELLOW + "Choose option: " + Fore.WHITE, end='')
  global choice
  choice = input()

  if choice == str("1"):
    time.sleep(1)
    while True:
      os.system("cls")
      
      with open("bands.txt", "r", encoding='utf-8') as bands:
        read = bands.readlines()

        nl()
        print(Fore.CYAN + pyfiglet.figlet_format("Random Bands"))
        nl()
        print(Fore.RED + "*ENTER to generate!*".center(72))
        print("*Type 666 to go back to the menu!* ".center(72))
        nl()
        print(Fore.YELLOW)
        print(random.choice(read).center(70))
        print(Fore.WHITE)
        randomband = input()
      
      if randomband == "666":
        os.system("cls")
        time.sleep(1)
        nl()
        print(Fore.RED + "Back to menu..." + Fore.WHITE)
        time.sleep(1) 
        main()

      else:
        pass

  elif choice == str("2"):
    while True:
      time.sleep(1)
      os.system("cls")
      nl()
      print(Fore.RED + "*Type 666 to go back to the menu!*" + Fore.WHITE)
      nl()
      print("_" * 110)
      print(Fore.RED + " WARNING! " + Fore.WHITE + "Please type the name of the genre/subgenre fully and correctly! Otherwise the program may not work!")
      print("_" * 110)
      nl()
      time.sleep(2)
      ask = print(Fore.YELLOW + "Which subgenre/genre? " + Fore.WHITE, end='')
      launch = input()
      genres = ["Deathcore","Power Metal","Heavy Metal","Death Metal","Black Metal",
      "Groove Metal","Thrash Metal","Alternative Metal","Nu Metal","Progressive Metal","Black-Death Metal","Black Death Metal",
      "Tech Death Metal","Metalcore","White Metal","Melodic Death Metal","Folk Metal","Neoclassical Death Metal",
      "Doom Metal","Industrial Metal","Gothic Metal","Djent","Avant-Garde Metal","Prog Metal","Glam Metal","Symphonic Deathcore",
      "Technical Deathcore","Blackened Tech-Death Metal","Grindcore","Trve Cvlt Norwegian Black Metal","Electronicore","Magical Death Metal",
      "Mathcore","Symphonic Black Metal","Ambient Black Metal","Folk Black Metal","Brutal Death Metal","Melodic Black Metal","Neoclassical Metal"
      ]

      if launch == "666":
        os.system("cls")
        time.sleep(1)
        nl()
        print(Fore.RED + "Back to menu..." + Fore.WHITE)
        time.sleep(1) 
        main()

      try:
        if difflib.get_close_matches(launch,genres): 
          nl()
          time.sleep(1)
          try:
            print(wikipedia.summary(difflib.get_close_matches(launch,genres,1), sentences = 5, auto_suggest = False))
            #print("Wow! {} is a great genre!".format(*difflib.get_close_matches(launch,genres), sep=''))

          except wikipedia.exceptions.PageError:
            time.sleep(0.5)
            print("[-] No Wikipedia page found ")
            pass

          time.sleep(1)
          nl()
          # Now the program will open the browser to search info about the genre etc.
          print(Fore.CYAN + "Press ENTER to search in browser:", end='') 
          print(Fore.WHITE)
          search = input()

          if search == "666":
            os.system("cls")
            time.sleep(1)
            nl()
            print(Fore.RED + "Back to menu..." + Fore.WHITE)
            time.sleep(1) 
            main()

          time.sleep(1)
          nl()
          print(Fore.BLUE + "I'll redirect you to google in a moment, so you can find information about that genre!")
          print(Fore.GREEN + "." * 86, Fore.WHITE)
          time.sleep(3)
          url="https://www.google.com/search?q="+str(difflib.get_close_matches(launch,genres,1))+""
          webbrowser.open(url)
   
          sys.exit()
    
        else:
          nl()
          time.sleep(1)
          print("I don't know such genre:(")
          time.sleep(2)
          os.system("cls")

      except (requests.ConnectionError, requests.Timeout) as exception:
        time.sleep(0.6)
        print(Fore.RED + "No Internet Connection!" + Fore.WHITE)
        time.sleep(0.8)
        main()

  elif choice == str("3"):
    time.sleep(1)
    os.system("cls")
    print(Fore.CYAN + pyfiglet.figlet_format("Contact"))
    nl()
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
      os.system("cls")
      time.sleep(1)
      nl()
      print(Fore.RED + "Back to menu..." + Fore.WHITE)
      time.sleep(1) 
      main()
    else: 
      os.system("cls")
      time.sleep(1)
      nl()
      print(Fore.RED + "Back to menu..." + Fore.WHITE)
      time.sleep(1) 
      main()

  elif choice == str("666"):
    time.sleep(0.5)
    nl()
    print(Fore.RED + "Exiting the program..." + Fore.WHITE)
    time.sleep(0.5)
    sys.exit()

  else:
    os.system("cls")
    time.sleep(0.8)
    main()

try:
  main()
except KeyboardInterrupt:
  import time
  import sys
  print("\n")
  print("_" * 25)
  print("Exiting the program...")
  print("_" * 25)
  time.sleep(0.1)
  sys.exit()  

# FUCK YEAH, I DID IT!
# FUCK YEAH, AGAIN!
# FUCK YEAH, WE HAVE ONLY ONE TRY/EXCEPT! (Now we have two... (P.S: Now three...))